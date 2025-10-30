const rows = 10;
const cols = 10;
const mazeEl = document.getElementById('maze');
const grid = [];
let start = null;
let end = null;

// Create grid
for (let y = 0; y < rows; y++) {
  const row = [];
  for (let x = 0; x < cols; x++) {
    const cell = document.createElement('div');
    cell.className = 'cell path';
    cell.dataset.x = x;
    cell.dataset.y = y;

    // Left click: wall toggle or set end
    cell.addEventListener('click', e => {
      if (e.shiftKey) {
        if (end) end.classList.remove('end');
        if (cell.classList.contains('start')) return;
        cell.className = 'cell end';
        end = cell;
      } else {
        if (cell.classList.contains('start') || cell.classList.contains('end'))
          return;
        if (cell.classList.contains('wall')) {
          cell.className = 'cell path';
        } else {
          cell.className = 'cell wall';
        }
      }
    });

    // Right click: set start
    cell.addEventListener('contextmenu', e => {
      e.preventDefault();
      if (cell.classList.contains('end')) return;
      if (start) start.classList.remove('start');
      cell.className = 'cell start';
      start = cell;
    });

    mazeEl.appendChild(cell);
    row.push(cell);
  }
  grid.push(row);
}

// BFS Maze Solver
function solve() {
  if (!start || !end) return alert('Set start and end points!');

  const sx = parseInt(start.dataset.x);
  const sy = parseInt(start.dataset.y);
  const ex = parseInt(end.dataset.x);
  const ey = parseInt(end.dataset.y);

  // Clear previous solution path
  document.querySelectorAll('.solution').forEach(cell => {
    cell.classList.remove('solution');
  });

  const visited = Array.from({ length: rows }, () => Array(cols).fill(false));
  const prev = Array.from({ length: rows }, () => Array(cols).fill(null));
  const queue = [[sy, sx]];
  visited[sy][sx] = true;

  const dirs = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
  ];

  while (queue.length > 0) {
    const [y, x] = queue.shift();
    if (y === ey && x === ex) break;

    for (let [dy, dx] of dirs) {
      const ny = y + dy;
      const nx = x + dx;

      if (
        ny >= 0 &&
        ny < rows &&
        nx >= 0 &&
        nx < cols &&
        !visited[ny][nx] &&
        !grid[ny][nx].classList.contains('wall')
      ) {
        visited[ny][nx] = true;
        prev[ny][nx] = [y, x];
        queue.push([ny, nx]);
      }
    }
  }

  // Reconstruct path
  let path = [];
  let cur = [ey, ex];
  while (cur && !(cur[0] === sy && cur[1] === sx)) {
    path.push(cur);
    cur = prev[cur[0]][cur[1]];
  }

  if (!cur) {
    alert('No path found.');
    return;
  }

  path.forEach(([y, x]) => {
    const cell = grid[y][x];
    if (!cell.classList.contains('start') && !cell.classList.contains('end')) {
      cell.classList.add('solution');
    }
  });
}

function restart() {
  console.log('Restarting...');

  for (let y = 0; y < rows; y++) {
    for (let x = 0; x < cols; x++) {
      const cell = grid[y][x];
      cell.classList.remove('start', 'end', 'wall', 'solution');
      cell.classList.add('path');
    }
  }

  start = null;
  end = null;
}
