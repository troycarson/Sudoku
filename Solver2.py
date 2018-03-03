def solveSudoku(grid, i, j):
    i, j = findNextCell(grid, i, j)
    print(i, j)
    possibleX = []
    possibleY = []
    counter = 0
    if i == -1:
        return True
    for e in range(1, 10):
        if isValid(grid, i, j, e):
            possibleX.append(i)
            possibleY.append(j)
    if len(possibleX) == 1:
        grid[possibleX[0]][possibleY[0]] = e
    if i < 9:
        solveSudoku(grid, i + 1, j + 1)
    else:
        counter += 1
        solveSudoku(grid, 0, 0)
    return False


def findNextCell(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def isValid(grid, i, j, e):
    rowOk = all([e != grid[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([e != grid[x][j] for x in range(9)])
        if columnOk:
            boxX, boxY = (int)(3 * (i / 3)), (int)(3 * (j / 3))
            for x in range(boxX, boxX + 3):
                for y in range(boxY, boxY - 3):
                    if grid[x][y] == e:
                        return False
            return True
        return False
    return False


if __name__ == '__main__':
    grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    solveSudoku(grid, 0, 0)
    print(grid)
