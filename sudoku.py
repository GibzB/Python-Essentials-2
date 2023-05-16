# Sudoku is a number-placing puzzle played on a 9x9 board

# The goal of Sudoku is to fill in a 9x9 grid with digits so that each column,
# row, and 3x3 section contain the numbers between 1 to 9. At the beginning of the game,
# the 9x9 grid will have some of the squares filled in. Your job is to use logic
# and process of elimination to fill in the missing digits and complete the grid.

# The program tasks:
# Ask the user to enter the numbers one by one. The empty cells should be marked with a zero (0).
# The program should check whether the entered numbers are valid in accordance with the rules of Sudoku.
# If the number is valid, the program should write it in its place on the board.
# If the number is not valid, the program should reject it and ask the user to enter another one.
# The program should print the updated board each time a new number is entered.


def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


# A list of rows representing the sudoku.
rows = [ ]
for r in range(9):
    ok = False
    while not ok:
        row = input("Enter row #" + str(r + 1) + ": ")
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print("Incorrect row data - 9 digits required")
    rows.append(row)

ok = True

# Check if all rows are good.
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Check if all columns are good.	
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# Check if all sub-squares (3x3) are good.
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            # Make a string containing all digits from a sub-square.
            for i in range(3):
                sqr += rows[r+i][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

# Print the final verdict.
if ok:
    print("Yes")
else:
    print("No")
    