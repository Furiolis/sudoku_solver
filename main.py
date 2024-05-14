def sudoku(puzzle):
    while any(0 in row for row in puzzle):
        possibility = {}
        for i, row in enumerate(puzzle):
            for j, cell in enumerate(row):
                if cell == 0:
                    for k in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                        row_bool, col_bool, scq_bool = False, False, False

                        # check what number is possible according to row restriction
                        if k not in row:
                            row_bool = True

                        # # check what number is possible according to column restriction
                        if k not in (puzzle[0][j], puzzle[1][j], puzzle[2][j], puzzle[3][j], puzzle[4][j],
                                     puzzle[5][j], puzzle[6][j], puzzle[7][j], puzzle[8][j]):
                            col_bool = True

                        # check what number is possible according to square restriction
                        m, n = i // 3, j // 3
                        if k not in (puzzle[3 * m + 0][3 * n + 0], puzzle[3 * m + 0][3 * n + 1], puzzle[3 * m + 0][3 * n + 2],
                                     puzzle[3 * m + 1][3 * n + 0], puzzle[3 * m + 1][3 * n + 1], puzzle[3 * m + 1][3 * n + 2],
                                     puzzle[3 * m + 2][3 * n + 0], puzzle[3 * m + 2][3 * n + 1], puzzle[3 * m + 2][3 * n + 2]):
                            scq_bool = True
                        if not possibility.get((i, j)):
                            possibility[(i, j)] = []
                        if row_bool and col_bool and scq_bool:
                            possibility[(i, j)].append(k)
        for cell, value in possibility.items():
            if len(value) == 1:
                puzzle[cell[0]][cell[1]] = value[0]
    return puzzle
