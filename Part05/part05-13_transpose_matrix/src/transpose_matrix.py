# Write your solution here
def transpose(matrix: list):
    #matrix structure clone
    rows=len(matrix)
    col=len(matrix[0])
    new_list=[[] for _ in range(col)]

    #filling the new list
    for i in range (rows):
        for ii in range(col):
            new_list[ii].append(matrix[i][ii])

    #storing in matrix not new_list
    for i in range(col):
        matrix[i]=new_list[i]

if __name__=="__main__":
    game_board = [[10, 100], [10, 100]]
    print(transpose(game_board))
    print(game_board)  


#model answer (def transpose(matrix: list):
   # n = len(matrix)
    #for i in range(n):
     #   for j in range(i, n):
      #      temp = matrix[i][j]
       #     matrix[i][j] = matrix[j][i]
        #    matrix[j][i] = temp)