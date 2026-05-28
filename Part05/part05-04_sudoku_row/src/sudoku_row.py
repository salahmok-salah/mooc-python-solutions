# Write your solution here
#func to validate row have all values

def row_correct(sudoku: list, row_no: int):
    compare_list=sorted(sudoku[row_no])
    for i in range(len(compare_list)-1,-1,-1):
        if compare_list[i-1]-compare_list[i]==0 and compare_list[i]!=0:
            return False
        else:
            continue
    return True


if __name__=="__main__":
    sudoku = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],   # rivi 0
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],   # rivi 1
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],   # rivi 2
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],   # rivi 3
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],   # rivi 4
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],   # rivi 5
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],   # rivi 6
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],   # rivi 7
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],   # rivi 8
    ]
    row_correct(sudoku, 0)


