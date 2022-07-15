import time

SIZE = 10
update_speed = 1
grid = [[0 for i in range(SIZE)] for j in range(SIZE)]
live = [
    [4, 2],
    [5, 3],
    [6, 1],
    [6, 2],
    [6, 3]
]

def init_grid():
    for coord in live:
        grid[coord[0]][coord[1]] = 1

def get_neighbors(row, col):
    # returns list of coords of neighbors of a given cell's indices
    neighbors = []

    if row - 1 >= 0 and col - 1 >= 0:
        neighbors.append([row-1, col-1])    # Upper left
    if row - 1 >= 0:
        neighbors.append([row-1, col])      # Up
    if row - 1 >= 0 and col + 1 < SIZE:
        neighbors.append([row-1, col+1])    # Upper right
    if col - 1 >= 0:
        neighbors.append([row, col-1])      # Left
    if col + 1 < SIZE:
        neighbors.append([row, col+1])      # Right
    if row + 1 < SIZE and col - 1 >= 0:
        neighbors.append([row+1, col-1])    # Lower left
    if row + 1 < SIZE:
        neighbors.append([row+1, col])      # Down
    if row + 1 < SIZE and col + 1 < SIZE:
        neighbors.append([row+1, col+1])    # Lower right


    return neighbors

def update_grid():
    # Will return true if changes can still be made to grid
    global grid
    can_update = False
    local_grid = [x[:] for x in grid]

    for i in range(SIZE):
        for j in range(SIZE):
            cell_val = grid[i][j]
            neighbors = get_neighbors(i, j)
            live_neighbors = 0

            for n in neighbors:
                if grid[n[0]][n[1]] == 1:
                    live_neighbors += 1

            if grid[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    continue
                else:
                    local_grid[i][j] = 0
            elif grid[i][j] == 0:
                if live_neighbors == 3:
                    local_grid[i][j] = 1
                else:
                    local_grid[i][j] = 0

            if local_grid[i][j] != cell_val:
                can_update = True
    grid = local_grid
    return can_update

    

def display_grid():
    divider = "\n  " + ("-" * (SIZE * 4 + 1))
    print("    ", end="")

    for i in range(SIZE):
        print(str(i), end="   ")
    print(divider)

    for i in range(SIZE):
        print(str(i) + " | ", end="")
        for j in range(SIZE):
            print(grid[i][j], end=" | ")
        print(divider)
    
    print()
        
def main():
    init_grid()
    display_grid()
    while update_grid():
        time.sleep(update_speed)
        display_grid()
    

if __name__ == '__main__':
    main()