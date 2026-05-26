# Write your solution here
grad=int(input("How many points [0-100]:"))
if grad< 0:
    print ('Grade: impossible!')
elif grad<50:
    print ('Grade: fail')
elif 50<=grad<60:
    print('Grade: 1')
elif 60<= grad<70:
    print('Grade: 2')
elif 70<=grad<80:
    print(' Grade: 3')
elif 80<= grad <90:
    print('Grade: 4')
elif 90<= grad<=100:
    print ('Grade: 5')
else:
    print('Grade: impossible!')