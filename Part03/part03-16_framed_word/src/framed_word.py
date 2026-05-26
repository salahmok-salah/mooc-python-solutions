# Write your solution here
strii=input("Word: ")
l1=len(strii)
l2=(28-l1)//2
l3=28-l1-l2
strii="*"+" "*l2+strii+" "*l3+"*"
print("*"*30)
print(strii)
print("*"*30)