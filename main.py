def show(grid):
    print(' ' * 3, ' 123 456 789 ')
    print(' ' * 3, '+---+---+---+')
    for row in range(9):
        line = repr(row).rjust(3) + ' '
        for col in range(9):
            v = grid[row][col]
            if (col % 3 == 0):
                line += '|'
            if (v == -1):
                line += '.'
            else:
                line += repr(v)
        line += '|'
        print( line)
    print('   +---+---+---+')

if __name__ == '__main__':
    grid = [[ -1 for col in range(9)] for row in range(9)]
    for row in range( 9):
        for col in range(9):
            grid[row][col] = -1

    show( grid)

