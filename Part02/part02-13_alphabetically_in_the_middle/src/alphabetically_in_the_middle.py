# Write your solution here
l1=input ('1st letter:')
l2=input ('2nd letter:')
l3=input ('3rd letter:')
if l1>l2:
    if l1<l3:
        mid=l1
    elif l2>l3:
        mid=l2
    else:
        mid=l3
elif l2>l3:
    if l1>l3:
        mid=l1
    else:
        mid=l3
else:
    if l1>l2:
        mid=l1
    else:
        mid=l2
print(f'The letter in the middle is {mid}')

