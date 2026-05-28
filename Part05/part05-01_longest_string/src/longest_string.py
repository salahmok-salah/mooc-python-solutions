# Write your solution here
def longest(strings: list):
    a=""
    for string in strings:
        if len(string)>len(a):
            a=string
    return a

if __name__=="__main__":
    print(longest(['sfsd','fsfsifweif']))