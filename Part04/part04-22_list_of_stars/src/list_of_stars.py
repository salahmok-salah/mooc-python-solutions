# Write your solution here
print(__name__)
def list_of_stars(a):
    for b in a:
        print("*"*b)
if __name__ == "__main__":
    print(list_of_stars(list(range(5))))
