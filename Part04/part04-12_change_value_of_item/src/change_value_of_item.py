# Write your solution here
mylist=[1, 2, 3, 4, 5]
while True:
    newindex=int(input("Index: "))
    if newindex==-1:
        break
    newvalue=int(input("New value: "))
    mylist[newindex]=newvalue
    print(mylist)