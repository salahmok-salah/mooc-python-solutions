# Write your solution here

passs=input('Password:')
while True:
    repas=input('Repeat password:')
    if passs==repas:
        break
    else:
        print('They do not match!')
print('User account created!')