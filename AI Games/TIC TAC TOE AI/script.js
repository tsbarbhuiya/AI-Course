// Create an empty 3x3 board using an array of 9 spaces
let board = Array(9).fill(' ');

// Variables to store the player's and AI's chosen symbols (X or O)
let player = null;
let ai = null;

// Tracks whether the game is currently active
let gameActive = false;

// Get DOM elements for the board, message display, and restart button
const boardDiv = document.getElementById('board');
const message = document.getElementById('message');
const restartBtn = document.getElementById('restart');

// Called when player chooses X or O
function setPlayerSymbol(symbol) {
  player = symbol;                  // Save player's symbol
  ai = symbol === 'X' ? 'O' : 'X';  // Assign the opposite to AI

  // Hide the symbol choice buttons and show the game board
  document.getElementById('symbol-choice').classList.add('hidden');
  boardDiv.classList.remove('hidden');

  renderBoard();    // Display the game board
  gameActive = true; // Game starts

  if (player === 'O') {
    aiMove(); // If player chose O, AI plays first
  }
}

// Render the board on the screen
function renderBoard() {
  boardDiv.innerHTML = ''; // Clear the board first

  // Loop through each cell and create clickable divs
  board.forEach((cell, i) => {
    const cellDiv = document.createElement('div');
    cellDiv.className = 'cell';         // Add CSS class
    cellDiv.textContent = cell;         // Show symbol (X, O, or blank)
    cellDiv.onclick = () => handleMove(i); // Handle click
    boardDiv.appendChild(cellDiv);      // Add cell to the board
  });
}

// Called when the player clicks a cell
function handleMove(index) {
  // Ignore if game is over, cell is already used, or no symbol chosen
  if (!gameActive || board[index] !== ' ' || !player) return;

  board[index] = player; // Mark cell with player's symbol
  renderBoard();         // Update board visually

  if (checkWinner(board, player)) {
    endGame('You Win!'); // Player wins
    return;
  } else if (isFull(board)) {
    endGame('Its a tie!'); // Board is full — tie
    return;
  }

  aiMove(); // Let AI take its turn
}

// AI plays its move
function aiMove() {
  const move = bestMove(); // Get best move using Minimax
  if (move !== null) {
    board[move] = ai; // Place AI's symbol
    renderBoard();    // Update board

    if (checkWinner(board, ai)) {
      endGame('Computer Win!'); // AI wins
    } else if (isFull(board)) {
      endGame('Tie!'); // No empty spaces — tie
    }
  }
}

// Display end game message and show restart button
function endGame(msg) {
  gameActive = false;          // Stop game
  message.textContent = msg;  // Show win/tie message
  restartBtn.classList.remove('hidden'); // Show restart button
}

// Reset everything to start a new game
function restartGame() {
  board = Array(9).fill(' '); // Clear board
  player = null;              // Reset player
  ai = null;                  // Reset AI
  gameActive = false;         // Set game to inactive

  message.textContent = '';                     // Clear message
  restartBtn.classList.add('hidden');           // Hide restart button
  boardDiv.classList.add('hidden');             // Hide board
  document.getElementById('symbol-choice').classList.remove('hidden'); // Show symbol choice
}

// Get a list of empty cells (their indexes)
function availableMoves(board) {
  return board
    .map((val, idx) => (val === ' ' ? idx : null)) // Keep index if empty
    .filter(i => i !== null);                     // Remove nulls
}

// Check if a player (p) has won on board (b)
function checkWinner(b, p) {
  // All winning positions (rows, cols, diagonals)
  const wins = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
    [0, 4, 8], [2, 4, 6],            // diagonals
  ];

  // Return true if any winning pattern is filled by player 'p'
  return wins.some(pattern => pattern.every(i => b[i] === p));
}

// Check if the board is full (no empty spaces)
function isFull(board) {
  return board.every(cell => cell !== ' ');
}

// Minimax algorithm for AI decision-making
function minimax(b, depth, isMax) {
  // Check for terminal states
  if (checkWinner(b, ai)) return 1;     // AI wins
  if (checkWinner(b, player)) return -1; // Player wins
  if (isFull(b)) return 0;              // Tie

  // Initialize best score depending on maximizing or minimizing
  let bestScore = isMax ? -Infinity : Infinity;

  // Loop through all possible moves
  for (let move of availableMoves(b)) {
    b[move] = isMax ? ai : player; // Simulate move
    let score = minimax(b, depth + 1, !isMax); // Recurse
    b[move] = ' '; // Undo move (backtrack)

    // Choose the best score
    bestScore = isMax ? Math.max(score, bestScore) : Math.min(score, bestScore);
  }

  return bestScore; // Return best score for this path
}

// Get the best possible move for AI using minimax
function bestMove() {
  let bestScore = -Infinity; // Start with worst possible score
  let move = null;

  // Check all available moves
  for (let i of availableMoves(board)) {
    board[i] = ai; // Try AI move
    let score = minimax(board, 0, false); // Evaluate with minimax
    board[i] = ' '; // Undo move

    if (score > bestScore) {
      bestScore = score; // Update best score
      move = i;           // Save best move
    }
  }

  return move; // Return the move with highest score
}

// remove all comments once done