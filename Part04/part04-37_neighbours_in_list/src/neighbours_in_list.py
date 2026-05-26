# Write your solution here
def longest_series_of_neighbours(a: list):
    count=1
    result=0
    for i in range(len(a)-1):
        
        if a[i+1]-a[i]==1 or a[i]-a[i+1]==1  :
            count+=1
        elif a[i+1]-a[i]!=1 or a[i]-a[i+1]!=1 :
            count=1
        result=max(count,result)
    return result

if __name__=='__main__':
    print(longest_series_of_neighbours([1, 2, 3, 5, 6, 7, 6, 5, 6, 7, 10, 11, 10]))