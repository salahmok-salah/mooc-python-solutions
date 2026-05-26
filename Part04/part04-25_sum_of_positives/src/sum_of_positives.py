# Write your solution here
def sum_of_positives(a: list):
    sum=0
    for i in a:
        if i>0:
            sum+=i
    return sum
if __name__=="__main__":
    lisst=[-1, 3,43 , 842,-4234]
    sum_of_positives(lisst)