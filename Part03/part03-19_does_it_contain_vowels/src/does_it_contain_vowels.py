# Write your solution here
strii=input("Please type in a string: ")
vowels="aeo"
index=0
while index<len(vowels):
    vowel =vowels[index:index+1]
    if vowel in strii:
        print(vowel,"found")
    else:
        print(vowel,"not found")
    index+=1