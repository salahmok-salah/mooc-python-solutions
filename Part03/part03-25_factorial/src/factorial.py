# Write your solution here
while True:
    num=int(input("Please type in a number: "))
    if num<=0:
        print("Thanks and bye!")
        break
    else:
        i=1
        acfac=1
        while i<=num:
            acfac*=i
            i+=1
        print(f"The factorial of the number {num} is {acfac}")