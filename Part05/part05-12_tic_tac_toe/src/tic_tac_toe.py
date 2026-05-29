# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x in [0,1,2] and y in [0,1,2]:
        if game_board[y][x]=="":
            if piece in ['X','O']:
                game_board[y][x]=piece
                return True
            else:
                return False
        else:
            return False
    else:
        return False

if __name__=="__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "x"))
    print(game_board)