# Write your solution here
strii=" "+input("Please type in a sentence: ")
index=1
while index<len(strii):
    if strii[index-1:index]==" " and strii[index:index+1] !=" ":
        print(strii[index:index+1])
    index+=1
