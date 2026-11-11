import logic
import validation

def main():
    player = "x"
    while True:
        choice = int(logic.show_board(logic.board,player))
        a = validation.chek_num(choice)
        if a:
            logic.update_board(player,choice-1)
            win = logic.chek_win(logic.WINNING_LINES,logic.board,player)
            print(win)
        player = "o" if player == "x" else "x"




main()
