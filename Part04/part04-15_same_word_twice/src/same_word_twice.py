# Write your solution here
list=[]
i=0
ext=0
while True:
    st=input("Word: ")
    while i<len(list) and len(list)!=0:
        if st==list[i]:
            print(f"You typed in {len(list)} different words")
            ext=1
            break
        elif st!=list[i]:
            i+=1
    if ext  ==1:
        break
    elif ext==0:
        list.append(st)
        i=0