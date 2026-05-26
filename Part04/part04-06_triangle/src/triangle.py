# Copy here code of line function from previous exercise
def line (x, num):
        if len(num)==0:
            num="*"
        print(num[0]*x)
def triangle(size):
    # You should call function line here with proper parameters
    fi=1
    while fi<=size:
         line(fi, "#")
         fi+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
