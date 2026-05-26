# Write your solution here
def same_chars(x,y,z):
    if len(x)-1<y or len(x)-1<z or x[y]!=x[z]:
        return False
    elif x[y]==x[z]:
        return True
    


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("aaaa", 1, 2))