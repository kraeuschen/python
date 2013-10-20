def solve_queens():
    rows = 8
    columns = 8
    solutions = []

    for row in range(rows):
        for column in range(columns):
            if no_conflict(row, column, solutions):
                solutions.append({'row': row, 'column': column})

    return solutions


def no_conflict(row, column, solutions):
    for solution in solutions:
        # horizontal
        if solution['row'] == row:
            return False

        # vertical
        if solution['column'] == column:
            return False

        # diagonal
        if (solution['column'] + 1) == column and (solution['row'] + 1 == row):
            #print 'next'
            return False

        if (solution['column'] - 1) == column  and (solution['row'] + 1 == row):
            #print 'prev'
            return False

    return True


if __name__ == '__main__':
    for solution in solve_queens():
        print solution