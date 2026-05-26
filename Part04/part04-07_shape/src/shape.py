# Copy here code of line function from previous exercise and use it in your solution
def line (x, num):
        if len(num)==0:
            num="*"
        print(num[0]*x)
def shape(a,b,c,d):
     fi=1
     while fi<=a:
         line(fi,b)
         fi+=1
     while c>0:
          line(a,d)
          c-=1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")