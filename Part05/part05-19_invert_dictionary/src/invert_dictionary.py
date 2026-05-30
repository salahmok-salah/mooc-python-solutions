# Write your solution here
def invert(dictionary: dict):
    new_dic={}
    for tag,val in dictionary.items():
        new_dic[val]=tag
    dictionary.clear()
    for i,ii in new_dic.items():
        dictionary[i]=ii
    print(dictionary)
    

if __name__=="__main__":

    invert({1: 10, 2: 20, 3: 30})

#def invert(dictionary: dict):
	#copy = {}
	#for key in dictionary:
	#	copy[key] = dictionary[key]
	#for key in copy:
	#	del dictionary[key]
	#for key in copy:
	#	dictionary[copy[key]] = key