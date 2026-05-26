# Write your solution here


def palindromes(a: str):
     b=0
     for i in range(len(a)//2):
         if a[i]!=a[(len(a)-i-1)]:
              return False
     return True
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
while True:
       st=input("Please type in a palindrome: ")

       if palindromes(st)== 1:
            print(st+" is a palindrome!")
            break
       else:
           print("that wasn't a palindrome")