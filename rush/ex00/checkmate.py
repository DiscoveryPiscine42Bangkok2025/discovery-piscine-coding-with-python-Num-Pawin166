def checkmate(board):
    # Split the board into rows
    rows = board.split("\n")
    size = len(rows)
    king_position = None

    # Find the position of the King (K)
    for i in range(size):
        for j in range(size):
            if rows[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if not king_position:
        print("Error: King not found")
        return

    king_row, king_col = king_position

    # Define directions for each piece's movement
    directions = {
        'P': [(1, -1), (1, 1)],  # Pawn captures diagonally
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # Bishop moves diagonally
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # Rook moves in straight lines
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],  # Queen combines Bishop and Rook
    }

    # Check each piece's attack pattern
    for piece, moves in directions.items():
        for move in moves:
            x, y = king_row, king_col
            while True:
                x += move[0]
                y += move[1]
                if not (0 <= x < size and 0 <= y < size):  # Out of bounds
                    break
                if rows[x][y] == piece:
                    print("Success")
                    return
                if rows[x][y] != '.':  # Blocked by another piece
                    break

    # Check for Pawns separately since they only move one step
    for move in directions['P']:
        x, y = king_row + move[0], king_col + move[1]
        if 0 <= x < size and 0 <= y < size and rows[x][y] == 'P':
            print("Success")
            return

    print("Fail")