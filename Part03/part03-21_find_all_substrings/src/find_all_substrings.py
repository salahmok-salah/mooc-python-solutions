# Write your solution here
strii=input("Please type in a word: ")
cha=input ("Please type in a character: ")
index=0
while index+3 <= len(strii):
    if strii[index] ==cha:
        print (strii[index:index+3])
    index+=1
        
