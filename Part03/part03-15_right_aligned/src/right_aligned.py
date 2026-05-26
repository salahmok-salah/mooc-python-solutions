# Write your solution here
strii=input("Please type in a string: ")
l1=20-len(strii)
if l1>0:
    strii= "*"*l1 +strii
    print(strii)
elif l1==0:
    print(strii)
