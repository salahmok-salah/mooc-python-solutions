def find_word(str, whatth):
    index = 0
    word = ""
    counter = 0
    while index < len(str):
    	if str[index] == " ":
    	    counter += 1
    	    if counter == whatth:
    	        break
    	    word = ""
    	else:
    	    word += str[index]
    	index += 1
    return word
 
def first_word(mjono):
    return find_word(mjono, 1)
 
def second_word(mjono):
    return find_word(mjono, 2)
 
def last_word(mjono):
    return find_word(mjono, 0)
sentence = "once upon a time there was a programmer"
print(first_word(sentence))
print(second_word(sentence))
print(last_word(sentence))