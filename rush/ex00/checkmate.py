

def checkmate(board):##checks for board
    if not board: 
        return
   

    kx = ky = -1 ## checks king inside board
    for i, row in enumerate(board):
        if 'K' in row:
            kx, ky = i, row.index('K')
            break
            
    if kx == -1: return


    ways_to_die = [ ##how each piece can kill
        (0, 1, 'RQ'), (0, -1, 'RQ'), (1, 0, 'RQ'), (-1, 0, 'RQ'), # Straight
        (1, 1, 'BQ'), (1, -1, 'BQ'), (-1, 1, 'BQ'), (-1, -1, 'BQ') # Diagonal
    
    ]

    for dx, dy, lethal in ways_to_die: ##checks every direction for lethal piece
        x, y = kx + dx, ky + dy
        while 0 <= x < len(board) and 0 <= y < len(board[0]):
            piece = board[x][y]
            if piece != '.':
                if piece in lethal:
                    print("Success")
                    return
                break
            x += dx
            y += dy


    for px, py in [(kx+1, ky-1), (kx+1, ky+1)]: ##pawn attack
        if 0 <= px < len(board) and 0 <= py < len(board[0]):
            if board[px][py] == 'P':
                print("Success")
                return




    print("Fail")
