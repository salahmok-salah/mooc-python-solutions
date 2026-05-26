# Write your solution here
def no_vowels(a:str):
    vowels="aeoiu"
    b=a
    for i in vowels:
        if i in a:
            b=b.replace(i,"")
    return b
if __name__=="__main__":
    print(no_vowels("hey how are you?"))