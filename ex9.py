# Chess Board Color determination

'''
* Chess board is designed to follow a pattern
* if both column and row are even or are both odd
* then that cell is while
* if the row is even and the column is odd, then the color is black
* Also if the row is odd and the column is even, then the color is black
'''

def getChessSquareColor(column, row):
    # if(column in range(1, 9) and (row in range(1, 9))):
    if column > 0 and column < 9 and row > 0 and row < 9:
        if column % 2 == row % 2:
            return 'white'
        else:
            return 'black'
    else:
        return ''


assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''

    
