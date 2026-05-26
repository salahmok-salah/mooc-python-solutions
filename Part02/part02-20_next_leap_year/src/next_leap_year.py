# Write your solution here
leap=0
year=int(input("Year:"))
nyear=year
while True:
    nyear+=1
    if nyear%4==0:
        if (nyear%100==0 and nyear%400==0) or (nyear%100!=0) :
            leap=1
            break
print (f"The next leap year after {year} is {nyear}")
        