def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None

def is_valid(grid, num, pos):
    row, col = pos
    # Check row
    if num in grid[row]:
        return False
    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False
    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num:
                return False
    return True

def solve_sudoku(grid):
    empty = find_empty(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def main():
    print("Enter the Sudoku puzzle row by row, use 0 for empty cells:")
    grid = []
    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ")
            if len(row.split()) == 9 and all(x.isdigit() and 0 <= int(x) <= 9 for x in row.split()):
                grid.append([int(x) for x in row.split()])
                break
            else:
                print("Please enter 9 numbers (0-9) separated by spaces.")
    print("\nUnsolved Sudoku:")
    print_grid(grid)
    if solve_sudoku(grid):
        print("\nSolved Sudoku:")
        print_grid(grid)
    else:
        print("No solution exists for the given puzzle.")

if __name__ == "__main__":
    main()
