# Write your solution here
limit=int(input("Limit: "))
itera=1
acc=1
stri="1 "
while acc<limit:
    itera+=1
    acc+=itera
    stri+= f"+ {itera} "

print("The consecutive sum: ",stri,"=",acc)
