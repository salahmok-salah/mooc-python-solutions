# Write your solution here

def row_correct(sudoku: list, row_no: int):
    row_list=[]
    for i in sudoku[row_no]:
        if i in row_list and i !=0:
            return False
        row_list.append(i)
    return True


#follow function full rows check
def full_row_correct(sudoku : list):
    for i in range(0,9):
        if row_correct(sudoku, i) is False:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    col_list=[]
    for row in sudoku:
        if row[column_no] in col_list and row[column_no] != 0:
                        return False
        col_list.append(row[column_no])
    return True

#follow function full columns check
def full_column_correct(sudoku : list):
    for i in range(0,9):
        if column_correct(sudoku, i) is False:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    exlud_list=[]
   
    for  ro in range(row_no,row_no+3):
        for  co in range(column_no,column_no+3):
            if sudoku[ro][co] in exlud_list and sudoku[ro][co]!=0:
                return False
            exlud_list.append(sudoku[ro][co])
    return True

#follow function to define suduko certian blocks to be checked ((0, 0), (0, 3),
#  (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6))
def blocks_check(sudoku : list):
    helper=[0,3,6]
    for i in helper:
        for ii in helper:
            if block_correct(sudoku, i, i) is False:
                return False
    return True

# accummulate all functions

def sudoku_grid_correct(sudoku: list):
    a=full_row_correct(sudoku)
    b=full_column_correct(sudoku)
    c=blocks_check(sudoku)    
    if a*b*c==1:
        return True
    else: 
        return False



if __name__=="__main__":
     
    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))
            