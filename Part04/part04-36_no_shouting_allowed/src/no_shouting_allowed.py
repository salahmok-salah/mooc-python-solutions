# Write your solution here
def no_shouting(a:list):
    new_list=[]
    for i in a:
        if i.isupper()==0:
            new_list.append(i)
    return new_list
if __name__=="__main__":
    print(no_shouting(['fsgf','gweri','HIPNMOPK']))