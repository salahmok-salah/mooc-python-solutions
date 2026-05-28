# Write your solution here
def who_won(game_board: list):
    couni=0
    counii=0
    for row in game_board:
        for elem in row:
            if elem==1:
                couni+=1
            elif elem==2:
                counii+=1
    if counii==couni:
        return 0
    elif counii<couni:
        return 1
    else:
        return 2
    
if __name__=="__main__":
    print(who_won([[1,2,1,2,0],[1,2,1,1,0]]))