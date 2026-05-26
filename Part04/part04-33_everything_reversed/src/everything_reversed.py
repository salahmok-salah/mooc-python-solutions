# Write your solution here
def everything_reversed(a:list):
    new=[]
    for i in a:
        new.append(i[::-1])
    return new[::-1]

if __name__=="__main__":
    print(everything_reversed(['fdfa','fsdfsg']))