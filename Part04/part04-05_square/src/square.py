# Copy here code of line function from previous exercise
def line (x, num):
        if len(num)==0:
            num="*"
        print(num[0]*x)
def square(size, character):
    # You should call function line here with proper parameters
    sizee=size
    while sizee>0:
         line(size,character)
         sizee-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")