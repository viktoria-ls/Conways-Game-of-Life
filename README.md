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
- Runs on Django server
- Updating frontend
- Fixing minor bugs with buttons
- Making update interval setting

## How to Run the Server Locally
Make sure you have Python, PIP, and Git Bash installed.
1. Clone Git repository in chosen directory
```
git clone https://github.com/viktoria-ls/Conways-Game-of-Life.git
```
2. Create virtual environment
```
py -m venv my_venv
```
3. Activate virtual environment
```
my_venv/Scripts/activate
```
4. Install Python packages
```
pip install -r requirements.txt
```
5. Navigate into Django project folder and migrate Django project
```
cd conway/
python manage.py migrate
```
6. Run server
```
python manage.py runserver
```
7. View page at localhost:8000 on web browser
