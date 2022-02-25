board = []

def create_board():
    for i in range(3):
        row = []
        for j in range(3):
            row.append([False])
        board.append(row)
    print(board)