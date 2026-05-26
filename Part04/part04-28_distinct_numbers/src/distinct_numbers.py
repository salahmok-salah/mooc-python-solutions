# Write your solution here
def distinct_numbers(a:list):
    new=[]
    for i in a:
        if i not in new:
            new.append(i)
    return sorted(new)
if __name__=="__main__":
    print(distinct_numbers([1,1,39,1,43,4,1]))