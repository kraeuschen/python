
def solve_queens():
    rows = 8
    columns = 8
    solutions = []

    for row in range(rows):
        for column in range(columns):
            if no_conflict(row, column, solutions):
                solutions.append({'row': row, 'column': column})

    return solutions

def no_conflict(row, colum, solutions):
    return True


for solution in solve_queens():
    print solution