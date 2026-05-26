# Write your solution here
s1=input("Please type in string 1: ")
s2=input("Please type in string 2: ")
l1=len(s1)
l2=len(s2)
if l1<l2:
    print(s2," is longer")
elif l1>l2:
    print(s1," is longer")
else:
    print("The strings are equally long")