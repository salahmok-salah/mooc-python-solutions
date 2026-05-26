# Write your solution here
year=int(input('Please type in a year:'))
n1=year%100
n2=year%400
n3=year%4
if n1 ==0 :
    if n2==0:
        print("That year is a leap year.")
    else:
        print("That is not a leap year.")
elif n3==0:
    print("That is a leap year.")
else:
    print ("That is not a leap year.")
