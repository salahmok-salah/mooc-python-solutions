# Write your solution here
def squared(cha,v):
    ind=0
    if len(cha)<v:
        rcha=cha*((v//len(cha)+1)*v)
    else:
        rcha=cha*v
    while ind<v*v:
        print(rcha[ind:ind+v])
        ind+=v
# Testing the function
if __name__ == "__main__":
    squared("ab", 3)
