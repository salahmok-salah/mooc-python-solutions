# Write your solution here
def spruce(base):
    print("a spruce!")
    wscount=(base*2-1)//2
    starinc=1
    while wscount>=0:
        print(f"{" "*wscount}{"*"*starinc}")
        wscount-=1
        starinc+=2
    print(f"{" "*((base*2-1)//2)}*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)