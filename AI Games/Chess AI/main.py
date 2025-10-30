import pygame
import chess
import sys
import os

# Constants
WIDTH, HEIGHT = 480, 520  # Extra height for turn display
SQ_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
PIECE_IMAGES = {}

# Load piece images
def load_images():
    piece_images = {
        'wP': 'white pawn.jpeg',
        'wR': 'white rook.jpeg',
        'wN': 'white knight.jpeg',
        'wB': 'white bishop.jpeg',
        'wQ': 'white queen.jpeg',
        'wK': 'white king.jpeg',
        'bP': 'black pawn.jpeg',
        'bR': 'black rook.jpeg',
        'bN': 'black knight.jpeg',
        'bB': 'black bishop.jpeg',
        'bQ': 'black queen.jpeg',
        'bK': 'black king.jpeg'
    }

    for piece, filename in piece_images.items():
        image_path = os.path.join('images', filename)
        PIECE_IMAGES[piece] = pygame.transform.scale(
            pygame.image.load(image_path), (SQ_SIZE, SQ_SIZE)
        )

# Highlight selected square and possible moves
def highlight_squares(screen, board, selected_square):
    if selected_square is None:
        return
    s = selected_square
    col = chess.square_file(s)
    row = 7 - chess.square_rank(s)

    pygame.draw.rect(screen, (255, 255, 0),
                     pygame.Rect(col * SQ_SIZE, row * SQ_SIZE + 40, SQ_SIZE, SQ_SIZE), 5)
    #pygame.Rect(x, y, WIDTH, Height)

    for move in board.legal_moves:
        if move.from_square == selected_square:
            dest = move.to_square
            dc = chess.square_file(dest)
            dr = 7 - chess.square_rank(dest)
            center = (dc * SQ_SIZE + SQ_SIZE // 2, dr * SQ_SIZE + SQ_SIZE // 2 + 40)
            pygame.draw.circle(screen, (0, 255, 0), center, 10)

# Draw the current player's turn at top
def draw_turn_text(screen, board):
    pygame.draw.rect(screen, (220, 220, 220), pygame.Rect(0, 0, WIDTH, 40))  # Background bar
    font = pygame.font.SysFont(None, 32)    #name, size
    turn_text = "White's Turn" if board.turn == chess.WHITE else "Black (AI)'s Turn"
    text = font.render(turn_text, True, (0, 0, 0))
    rect = text.get_rect(center=(WIDTH // 2, 20))
    screen.blit(text, rect)

# Draw board and pieces
def draw_board(screen, board, selected_square):
    colors = [WHITE, GRAY]
    for r in range(8):
        for c in range(8):
            color = colors[(r + c) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(c * SQ_SIZE   , r * SQ_SIZE + 40    , SQ_SIZE,     SQ_SIZE))
            #pygame.Rect(x, y, WIDTH, Height)
    highlight_squares(screen, board, selected_square)
    draw_pieces(screen, board)
    draw_turn_text(screen, board)

def draw_pieces(screen, board):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = 7 - chess.square_rank(square)
            piece_str = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().upper() 
            #piece.symbol() means pown is p bishop is b etc
            screen.blit(PIECE_IMAGES[piece_str],
                        pygame.Rect(col * SQ_SIZE, row * SQ_SIZE + 40, SQ_SIZE, SQ_SIZE)) #pygame.Rect(x, y, WIDTH, Height)

# Evaluation (material count)
def evaluate(board):
    values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9
    }
    eval = 0
    for piece in board.piece_map().values():
        value = values.get(piece.piece_type, 0)
        eval += value if piece.color == chess.BLACK else -value
    return eval

# Minimax
def minimax(board, depth, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board), None

    best_move = None
    if maximizing:
        max_eval = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_move = move
        return min_eval, best_move

# Show game result
def display_game_over(screen, board):
    font = pygame.font.SysFont(None, 48)
    if board.is_checkmate():
        winner = "Black" if board.turn == chess.WHITE else "White"
        text = font.render(f"{winner} wins by Checkmate!", True, (255, 0, 0))
    # elif board.is_stalemate():
    #     text = font.render("Stalemate!", True, (255, 0, 0))
    # elif board.is_insufficient_material():
    #     text = font.render("Draw: Insufficient Material", True, (255, 0, 0))
    # elif board.is_seventyfive_moves():
    #     text = font.render("Draw: 75-Move Rule", True, (255, 0, 0))
    # elif board.is_fivefold_repetition():
    #     text = font.render("Draw: Repetition", True, (255, 0, 0))
    else:
        text = font.render("Game Over", True, (255, 0, 0))

    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)
    pygame.display.flip()
    pygame.time.wait(5000)

# Main loop
def main():
    pygame.init()
    pygame.font.init()  # ✅ Ensure fonts are initialized
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess: You vs AI")
    board = chess.Board()
    clock = pygame.time.Clock()
    load_images()

    selected_square = None
    running = True

    while running:
        draw_board(screen, board, selected_square)
        pygame.display.flip()

        if board.is_game_over():
            display_game_over(screen, board)
            running = False
            continue

        if board.turn == chess.BLACK:
            pygame.time.delay(2000)
            _, move = minimax(board, 2, True)
            if move:
                board.push(move)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and board.turn == chess.WHITE:
                x, y = event.pos
                if y < 40:
                    continue  # Ignore clicks on top text bar
                col = x // SQ_SIZE
                row = 7 - ((y - 40) // SQ_SIZE)
                square = chess.square(col, row)

                if selected_square is None:
                    if board.piece_at(square) and board.piece_at(square).color == chess.WHITE:
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None

        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
