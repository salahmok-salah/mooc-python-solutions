# Write your solution here
n1=int(input('Number:'))
n2=n1%3
n3=n1%5
if n2 ==0 and n3==0:
    print('FizzBuzz')
elif n2==0:
    print('Fizz')
elif n3==0:
    print('Buzz')