# Write your solution here
def shortest(a: list):
    short=a[0]
    for i in a:
        if len(i)<len(short):
            short=(i)
    return short
if __name__=="__main__":
    print(shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))