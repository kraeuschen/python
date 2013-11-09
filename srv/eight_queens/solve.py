def solve_queens():
    board = 8
    solutions = []

    for row in range(board):
        solutions = get_solutions(row, board, solutions)

    return solutions

def get_solutions(row, columns, solutions):
    result = []

    for column in range(columns):
        if not len(solutions):
            result.append([(row, column)])
        else:
            for queens in solutions:
                if no_conflict(row, column, queens):
                    result.append(queens + [(row, column)])

    return result

def no_conflict(row, column, queens):
    for tupel in queens:
        r,c = tupel
        if r == row:
            return False

        if c == column:
            return False

        if (column - c) == (row - r):
            return False

        if (column - c) == -(row -r):
            return False

    return True


if __name__ == '__main__':
    for solution in solve_queens():
        print solution
