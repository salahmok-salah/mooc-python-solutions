# Write your solution here
def mainrun():
    phone_book={}
    while True:
        a=int(input("command (1 search, 2 add, 3 quit): "))
        if a==1:
            search_fun(phone_book)
        if a==2:
            add_fun(phone_book)
        if a==3:
            print("quitting...")
            break

def add_fun(pb: dict):
    name=input("name: ")
    numb=input("number:")
    print("ok!")
    pb[name]=numb

def search_fun(pb: dict):
    name=str(input("name: "))
    if not name in pb:
        print("no number")
    else:
        print(pb[name])

mainrun()
    