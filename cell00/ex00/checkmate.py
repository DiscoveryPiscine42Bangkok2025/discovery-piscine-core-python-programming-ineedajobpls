def checkmate(board):
    if not board: return
    
    # Get king coords - people often use simple nested loops for this
    kx = ky = -1
    for i, row in enumerate(board):
        if 'K' in row:
            kx, ky = i, row.index('K')
            break
            
    if kx == -1: return

    # Combine all sliding logic into one loop
    # (dx, dy, what_pieces_can_kill_from_here)
    ways_to_die = [
        (0, 1, 'RQ'), (0, -1, 'RQ'), (1, 0, 'RQ'), (-1, 0, 'RQ'), # Straights
        (1, 1, 'BQ'), (1, -1, 'BQ'), (-1, 1, 'BQ'), (-1, -1, 'BQ') # Diagonals
    ]

    for dx, dy, lethal in ways_to_die:
        x, y = kx + dx, ky + dy
        while 0 <= x < len(board) and 0 <= y < len(board[0]):
            piece = board[x][y]
            if piece != '.':
                if piece in lethal:
                    print("Success")
                    return
                break # Hit a friendly or non-threatening piece, stop looking
            x += dx
            y += dy

    # Pawn check - usually just written out plainly
    for px, py in [(kx-1, ky-1), (kx-1, ky+1)]:
        if 0 <= px < len(board) and 0 <= py < len(board[0]):
            if board[px][py] == 'P':
                print("Success")
                return

    print("Fail")


def main():
    board = [
        ".R..",
        ".K..",
        "....",
        "...."
    ]
    checkmate(board)

if __name__ == "__main__":
    main()