# Write your solution here
stor=""
preword=""
while True :
    word=input("Please type in a word:")
    if preword==word:
        break
    elif word=="end":
        break
    else:
        preword= word
        stor+=" "+ word
print(stor)