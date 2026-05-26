# Write your solution here
def chessboard(v):
    stri=""
    i=1
    while i<=v+1:
        if i%2>0: 
            o='1'
        if i%2 == 0:
            o='0'
        stri=stri+o
        i+=1
    ii=1
    while ii<=v:
        if ii%2!=0:
            print(stri[0:v])
        else:
            print(stri[1:v+1])
        ii+=1
# Testing the function
if __name__ == "__main__":
    chessboard(4)
