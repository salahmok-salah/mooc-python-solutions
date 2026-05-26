# Write your solution here
strii=input("Please type in a string: ")
cha=input ("Please type in a substring: ")
index = strii.find(cha)
if index!=-1:
    index= index +len(cha)
    while index+len(cha) <= len(strii):
        if strii[index:index+len(cha)]==cha:
            print(f"The second occurrence of the substring is at index {index}.") 
            index=-2
            break
        else:
            index =index+1
if index!=-2:
        print("The substring does not occur twice in the string.")
            