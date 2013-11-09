def solve_queens():
    board = 8
    solutions = []

    for row in range(board):
        solutions = get_solution(row, board, solutions)

    return solutions

def get_solution(row, columns, solutions):
    result = []

    for column in range(columns):
        if not len(solutions):
            result.append([(row, column)])
        else:
            for solution in solutions:
                if no_conflict(row, column, solution):
                    result.append(solution + [(row, column)])

    return result

def no_conflict(row, column, solutions):
    for solution in solutions:
        r,c = solution
        if r == row:
            return False

        if c == column:
            return False

        if (column - c) == (row - r):
            return False

        if (column -c) == -(row -r):
            return False

    return True


if __name__ == '__main__':
    for solution in solve_queens():
        print solution
