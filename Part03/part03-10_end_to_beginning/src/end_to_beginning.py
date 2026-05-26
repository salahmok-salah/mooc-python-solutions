# Write your solution here
stri=input("Please type in a string: ")
l1=len(stri)
itt=1
rev=-1
while itt<=l1:
    if l1==0:
        break
    print(stri[rev])
    itt+=1
    rev-=1
