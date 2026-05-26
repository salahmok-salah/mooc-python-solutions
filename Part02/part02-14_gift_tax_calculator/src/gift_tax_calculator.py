# Write your solution here
x= float(input('Value of gift:'))
tax=0
if x>=1000000:
    tax=(142100+(x-1000000)*.17)
elif x<1000000:
    if x>= 200000:
        tax=(22100+(x-200000)*.15)
    elif x>=55000:
        tax=(4700+(x-55000)*.12)
    elif x>= 25000:
        tax=(1700+(x-25000)*.1)
    elif x>= 5000:
        tax= (100+(x-5000)*.08)
    elif x>=0:
        print('No tax!')
    else:
        print('wrong entry')
if tax !=0:
    print(f"Amount of tax: {tax} euros")

    


