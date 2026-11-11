board = [None,None,None,None,None,None,None,None,None]
WINNING_LINES = [(0, 1, 2),(3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6)]

def show_board(listi,player)-> int:
    print(f"""
        [1]{listi[0] if listi[0] else ' '} | [2] {listi[1] if listi[1] else ' '} | [3]{listi[2] if listi[2] else ' '}
        [4]{listi[3] if listi[3] else ' '} | [5]{listi[4] if listi[4] else ' '} | [6]{listi[5] if listi[5] else ' '}
        [7]{listi[6] if listi[6] else ' '} | [8]{listi[7] if listi[7] else ' '} | [9]{listi[8] if listi[8] else ' '}
    """)
    choi = input(f"Player {player}  , choose a cell (1-9):")
    return choi
def update_board(player,index):
    board[index] = player


def chek_win(listi,board,player):
    for i in listi:
        if board[i[0]] == player and board[i[1]] == player and board[i[2]] == player:
            return "You win"