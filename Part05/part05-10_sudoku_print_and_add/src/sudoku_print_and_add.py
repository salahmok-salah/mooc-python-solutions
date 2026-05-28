# Write your solution here
def print_sudoku(sudoku: list):
    line=""
    for i in range(len(sudoku)):
        for ii in range(len(sudoku)):
            if sudoku[i][ii]==0:
                line+="_"
            else:
                line+=f"{sudoku[i][ii]}"
            if ii in [2,5]:
                line+="  "
            elif ii !=8:
                line+=" "
        print(line)
        if i in  [2,5]:
            print()
        line=""


def add_number(sudoku: list,row_num:int,col_num:int, elem:int):
    sudoku[row_num][col_num]=elem






if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)