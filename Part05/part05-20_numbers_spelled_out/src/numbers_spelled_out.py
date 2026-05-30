# Write your solution here
def dict_of_numbers():
    unit_dic={1:'one',2:'two',3:'three',4:'four',5:'five',
        6:'six', 7:'seven', 8:'eight',9:'nine'}
    tenth_dic={0:'zero',10:'ten',11:'eleven',12:'twelve',13:'thirteen', 14:'fourteen'
            ,15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
    pack_dic={20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',
         70:'seventy',80:'eighty',90:'ninety'}

    full_dic_num={}
    for i,ii in unit_dic.items():
        full_dic_num[i]=ii
    for i,ii in tenth_dic.items():
        full_dic_num[i]=ii
    for i,ii in pack_dic.items():
        full_dic_num[i]=ii
    for acc,accval in pack_dic.items():
        for i,ii in unit_dic.items():
            full_dic_num[acc+i]=f'{accval}-{ii}'

    return full_dic_num
if __name__=="__main__":
    print(dict_of_numbers())
