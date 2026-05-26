# Write your solution here
num=int(input("Please type in a number: "))
i=1
if i==num:
    print(i)
while i!=num:
    print(i)
    print(num)
    i+=1
    if num==i:
        break
    elif num-i==1:
        print(i)
        break
    elif num<i:
        break
    num-=1
