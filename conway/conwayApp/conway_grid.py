def get_neighbors(row, col, size):
    # returns list of coords of neighbors of a given cell's indices
    neighbors = []

    if row - 1 >= 0 and col - 1 >= 0:
        neighbors.append([row-1, col-1])    # Upper left
    if row - 1 >= 0:
        neighbors.append([row-1, col])      # Up
    if row - 1 >= 0 and col + 1 < size:
        neighbors.append([row-1, col+1])    # Upper right
    if col - 1 >= 0:
        neighbors.append([row, col-1])      # Left
    if col + 1 < size:
        neighbors.append([row, col+1])      # Right
    if row + 1 < size and col - 1 >= 0:
        neighbors.append([row+1, col-1])    # Lower left
    if row + 1 < size:
        neighbors.append([row+1, col])      # Down
    if row + 1 < size and col + 1 < size:
        neighbors.append([row+1, col+1])    # Lower right

    return neighbors

def update_grid(curr_grid):
    can_update = False
    size = len(curr_grid[0])
    next_grid = [x[:] for x in curr_grid]

    for i in range(size):
        for j in range(size):
            cell_val = curr_grid[i][j]
            neighbors = get_neighbors(i, j, size)
            live_neighbors = 0

            for n in neighbors:
                if curr_grid[n[0]][n[1]] == 1:
                    live_neighbors += 1

            if curr_grid[i][j] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    continue
                else:
                    next_grid[i][j] = 0
            elif curr_grid[i][j] == 0:
                if live_neighbors == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0

            if next_grid[i][j] != cell_val:
                can_update = True
    if can_update != None:
        return next_grid
    return None