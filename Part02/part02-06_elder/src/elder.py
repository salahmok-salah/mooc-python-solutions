# Write your solution here
name1=input('person1')
age1=int(input('age:'))
name2=input('person2')
age2=int(input('age:'))
if age1>age2:
    print(f'the elder is {name1}')
elif age2>age1:
    print(f'The lder is {name2}')
elif age2 ==age1:
    print(f'{name1} and {name2} are the same age')