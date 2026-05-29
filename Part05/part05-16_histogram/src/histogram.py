# Write your solution here
def histogram(word:str):
    letters_dict={}
    for i in word:
        if i not in letters_dict:
            letters_dict[i]=0
        letters_dict[i]+=1
    for letter in letters_dict:
        print(letter, "*"*letters_dict[letter])

if __name__=="__main__":
    histogram("sdfaipfiajf")