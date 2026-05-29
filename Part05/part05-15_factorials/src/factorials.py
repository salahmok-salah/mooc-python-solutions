# Write your solution here
def factorials(n: int):
    factorials_dict={}
    transiant=1
    for i in range(1,n+1):
        transiant*=i
        factorials_dict[i]=transiant
    return factorials_dict
if __name__=="__main__":
    print(factorials(10)[4])
    