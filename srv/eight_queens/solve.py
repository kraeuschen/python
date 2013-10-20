def solve_queens():
    rows = 8
    columns = 8
    solutions = []
    failes = []

    start_row = 0
    start_column = 0

    while (start_column < columns):
        for row in range(rows):
            for column in range(columns):
                if not has_failed(row, column, failes) and no_conflict(row, column, solutions):
                    solutions.append({'row': row, 'column': column})


        if len(solutions) < rows:
            solutions = []
            failes.append({'row': start_row, 'column': start_column})
            start_row += 1

            if (start_row == rows):
                start_row = 0
                start_column += 1
        else:
            break

    return solutions


def has_failed(row, column, failes):
    for fail in failes:
        if fail['row'] == row and fail['column'] == column:
            return True

    return False


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

        if (solution['column'] - 1) == column and (solution['row'] + 1 == row):
            #print 'prev'
            return False

    return True


if __name__ == '__main__':
    for solution in solve_queens():
        print solution