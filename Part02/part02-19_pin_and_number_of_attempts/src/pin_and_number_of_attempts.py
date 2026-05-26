# Write your solution here
att=0
success=False
while True:
    pin=input('Pin:')
    att+=1
    if pin=="4321":
        success=True
        break
    else :
        print("Wrong")
if  att==1:
    print("Correct! It only took you one single attempt!")
elif att>1:
    print (f"Correct! It took you {att} attempts")