const fs = require('fs');
const pdf = require('pdf-parse');

// Función para extraer el texto del PDF
async function extractMazeFromPDF(pdfPath) {
    const dataBuffer = fs.readFileSync(pdfPath);
    const data = await pdf(dataBuffer);
    const lines = data.text.split('\n');
    const maze = lines.map(line => {
        return line.split('').map(char => {
            if (char === ' ') return '0';
            if (char === 'S' || char === 'N') return char;
            return '1';
        });
    });
    return maze;
}

// Implementación del algoritmo BFS
function bfsSolveMaze(maze) {
    const rows = maze.length;
    const cols = maze[0].length;
    let start = null;
    let end = null;

    // Encontrar posiciones de inicio (S) y fin (N)
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (maze[i][j] === 'S') {
                start = [i, j];
            } else if (maze[i][j] === 'N') {
                end = [i, j];
            }
        }
    }

    if (!start || !end) return null;

    const directions = [
        [-1, 0], [1, 0], [0, -1], [0, 1]
    ];
    const queue = [[start, [start]]];
    const visited = new Set();
    visited.add(start.toString());

    while (queue.length > 0) {
        const [current, path] = queue.shift();
        const [currRow, currCol] = current;

        if (currRow === end[0] && currCol === end[1]) {
            return path;
        }

        for (const [dRow, dCol] of directions) {
            const nextRow = currRow + dRow;
            const nextCol = currCol + dCol;

            if (
                nextRow >= 0 && nextRow < rows &&
                nextCol >= 0 && nextCol < cols &&
                maze[nextRow][nextCol] !== '1' &&
                !visited.has([nextRow, nextCol].toString())
            ) {
                queue.push([[nextRow, nextCol], path.concat([[nextRow, nextCol]])]);
                visited.add([nextRow, nextCol].toString());
            }
        }
    }

    return null;
}

// Ruta del archivo PDF
const pdfPath = 'Rectangular-maze.pdf';

// Extracción del laberinto y resolución
(async () => {
    try {
        const maze = await extractMazeFromPDF(pdfPath);
        const solutionPath = bfsSolveMaze(maze);

        if (solutionPath) {
            console.log("Solución encontrada:");
            solutionPath.forEach(step => {
                console.log(step);
            });
        } else {
            console.log("No se encontró solución para el laberinto.");
        }
    } catch (err) {
        console.error("Error al procesar el PDF:", err);
    }
})();
