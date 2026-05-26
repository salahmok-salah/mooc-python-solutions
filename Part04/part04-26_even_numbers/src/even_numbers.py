# Write your solution here
def even_numbers(a:list):
    sum=[]
    for i in a:

        if i%2==0:
            sum.append(i)
    return sum
if __name__=="__main__":
    st=list(input("lista"))
    print(even_numbers(st))