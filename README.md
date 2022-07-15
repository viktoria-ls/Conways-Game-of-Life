# Conway's Game of Life
Conway's Game of Life was created by John Horton Conway in 1970. The game consists of a grid where each cell is either "alive" or "dead". The configuration of the grid is given by the user upon starting the game. Cells become alive or dead depending on the state of its neighboring cells. Read more about the game [here](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Rules
The rules of Conway's Game of Life can be generalized to the following:
- A live cell lives if it has 2 or 3 live neighbors.
- A dead cell becomes a live cell if it has 3 live neighbors.
- All other cells die or stay dead.

## Current Progress
- The above rules have been implemented.
- The program is limited to a finite grid size.
- Only a text UI is available for now.

## How to Configure and Run the Program
Note that all configurations have to be made directly in the main.py file.
- Change grid size by updating the `SIZE` value.
- Change the interval of displaying grid changes by updating the `update_speed` value.
- Set the initial "live cells" of the grid by updating the `live` value which is a list of grid coordinates (Base this off of inputted `SIZE` value). Make sure these are **VALID COORDINATES**.
- Run using `python main.py` on the command line in the same folder as the file.

## To do
- Make a proper GUI with direct user input.
- Implement "infinite" grid sizing.
