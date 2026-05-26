# Write your solution here
def most_common_character(a: str):
    str1=a[0]
    count=a.count(str1)
    for i in a:
        if i!=str1 and count< a.count(i):
            str1=(i)
    return str1
if __name__=="__main__":
    print(most_common_character("fDKFNVpvnio"))