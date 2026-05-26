# Write your solution here
strii=input("Please type in a string: ")
if len(strii)>0:
    if strii[1]==strii[-2]:
        print(f"The second and the second to last characters are {strii[1]}")
    else:
        print("The second and the second to last characters are different")