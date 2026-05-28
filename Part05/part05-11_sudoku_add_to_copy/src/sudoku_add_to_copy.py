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


def copy_and_add(sudoku1: list,row_num:int,col_num:int, elem:int):
    sudoku_copy=[]
    for i in range(len(sudoku1)):
        sudoku_copy.append([])
        for ii in range(len(sudoku1)):
            sudoku_copy[i].append(sudoku1[i][ii])
    sudoku_copy[row_num][col_num]=elem
    return sudoku_copy


if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)