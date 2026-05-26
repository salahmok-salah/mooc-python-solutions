# Write your solution here
list=[]
i=0
st=""
while st!='x':
    print(f"The list is now {list}")
    st=input(f"a(d)d, (r)emove or e(x)it: ")
    if st=="d":
        list.append(i+1)
        i+=1
    elif st =="r":
        list.pop(i-1)
        i-=1
print("Bye!")