# Write your solution here
def first_word(st):
    i=0
    index=0
    sens=""
    while i<len(st):
        if st[index]!= " ":
            sens+= st[index]
            index+=1
        else:
            break
    return sens
def second_word(st):
    i=0
    index=st.find(" ")+1
    sens=""
    while index<len(st):
        if st[index]!= " ":
            sens+= st[index]
            index+=1
        else:
            break
    return sens
def last_word(st):
    index=st.rfind(" ")+1
    sens=""
    while index<len(st):
        if st[index]!= " ":
            sens+= st[index]
            index+=1
        else:
            break
    return sens

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))