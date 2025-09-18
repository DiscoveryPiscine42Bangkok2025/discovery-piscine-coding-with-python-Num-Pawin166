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

def suggest_best_move(board):
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

    # Define potential moves for pieces
    directions = {
        'P': [(1, -1), (1, 1)],
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],
    }

    # Check for the best move
    for piece, moves in directions.items():
        for move in moves:
            x, y = king_position[0] + move[0], king_position[1] + move[1]
            if 0 <= x < size and 0 <= y < size and rows[x][y] == piece:
                print(f"Best Move: Move {piece} at ({x+1}, {y+1}) to check the King")
                return
    print("No immediate move to check the King")

def generate_threat_map(board):
    rows = board.split("\n")
    size = len(rows)
    threat_map = [['.' for _ in range(size)] for _ in range(size)]

    # ทิศทางการเดินของแต่ละชิ้นส่วน
    directions = {
        'P': [(1, -1), (1, 1)],  # Pawn คุกคามทแยง
        'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],  # Bishop คุกคามทแยง
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],  # Rook คุกคามแนวนอนและแนวตั้ง
        'Q': [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)],  # Queen คุกคามทุกทิศทาง
    }

    for i in range(size):
        for j in range(size):
            piece = rows[i][j]
            
            if piece in directions:
                # ถ้าชิ้นส่วนคือ Rook, Bishop, หรือ Queen ต้องคำนวณการคุกคามในทิศทางที่ถูกต้อง
                if piece in ['R', 'B', 'Q']:
                    for move in directions[piece]:
                        x, y = i, j
                        while True:
                            x += move[0]
                            y += move[1]
                            # ตรวจสอบขอบเขตของกระดาน
                            if not (0 <= x < size and 0 <= y < size):
                                break
                            # ทำเครื่องหมายเป็นพื้นที่ที่ถูกคุกคาม
                            if threat_map[x][y] == '.':
                                threat_map[x][y] = 'X'
                            # หยุดหากพบชิ้นส่วนอื่น
                            if rows[x][y] != '.':
                                break

                # คำนวณการคุกคามของ Pawn (P) ที่เดินแค่หนึ่งก้าวในทแยง
                if piece == 'P':
                    for move in directions['P']:
                        x, y = i + move[0], j + move[1]
                        if 0 <= x < size and 0 <= y < size:
                            threat_map[x][y] = 'X'

    # แปลงแผนที่การคุกคามให้เป็นรูปแบบที่พิมพ์ได้
    return "\n".join("".join(row) for row in threat_map)

