# Write your solution here
run=True
while run:
    strii=input("Please type in a string: ")
    if len(strii)==0:
        run= False
    print(strii)
    print("-"*len(strii))