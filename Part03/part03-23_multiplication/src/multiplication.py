# Write your solution here
num=int(input("Please type in a number: "))
i=1
while i<=num:
    ii=1
    while ii<=num:
        print(f"{i} x {ii} = {i*ii}")
        ii+=1
    i+=1