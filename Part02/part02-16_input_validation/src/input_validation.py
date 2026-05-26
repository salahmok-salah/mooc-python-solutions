
# Write your solution here
from math import sqrt
while True:
    m=float(input('Please type in a number:'))
    if m>0:
        print(m**.5)
    elif m<0:
        print('Invalid number')
    elif m==0:
        break
print('Exiting...')