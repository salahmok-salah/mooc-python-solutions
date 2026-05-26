# Write your solution here
#defining for entry
summ=0
mean=0
count=0
neg=0
print('Please type in integer numbers. Type in 0 to finish.')
while True:
    num=int (input("Number:"))
    if num==0:
        break
    summ +=num
    count +=1
    mean=summ /count
    if num <0:
        neg+=1
print("Numbers typed in", count)
print ("The sum of the numbers is", summ)
print ("The mean of the numbers is", mean)
print("Negative numbers", neg)
print("Positive numbers", count-neg)
 