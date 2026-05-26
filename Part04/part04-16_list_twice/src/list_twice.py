# Write your solution here
list=[]
while True:
    st=int(input("New item: "))
    if st==0:
        print("Bye!")
        break
    list.append(st)
    print ("The list now:", list)
    print ("The list in order:", sorted(list))