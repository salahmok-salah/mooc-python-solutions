# Write your solution here
strii=input("Please type in a word: ")
cha=input ("Please type in a character: ")
index= strii.find(cha)
if len(strii)>index+2:
    print(strii[index:index+3])
#if index==-1:
  #  print("character not found")
#else: