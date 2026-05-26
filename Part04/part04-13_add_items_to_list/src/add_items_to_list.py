# Write your solution here
itemscount=int(input("How many items: "))
i=1
list=[]
while i<=itemscount:
    list.append(int(input(f"Item{i}: ")))
    i+=1
print(list)

