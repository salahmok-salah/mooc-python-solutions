# Write your solution here
hw=0
hwo=0
hw= float(input("Hourly wage:"))
hwo=float(input('Hours worked: '))
day=input("Day of the week: ")
if day == 'Sunday':
    hw*=2

print(f"Daily wages: {hw*hwo} euros")