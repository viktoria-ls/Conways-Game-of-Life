from operator import truediv

from attr import has


SIZE = 10
grid = [[0 for i in range(SIZE)] for j in range(SIZE)]
live = [
    [2, 4],
    [2, 5],
    [3, 4],
    [4, 4]
]

def init_grid():
    for coord in live:
        grid[coord[0]][coord[1]] = 1

def has_change():
    has_change = True
    # Checks if changes can be made on grid given current config
    return has_change

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
        

def main():
    init_grid()
    display_grid()

if __name__ == '__main__':
    main()