# Write your solution here
def length_of_longest(a: list):
    longest=0
    for i in a:
        if len(i)>longest:
            longest=len(i)
    return longest
if __name__=="__main__":
    print(length_of_longest(['ffa','fadfa']))