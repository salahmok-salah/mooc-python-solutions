# Write your solution here
def all_the_longest(a: list):
    long=['']
    for i in a:
        if len(i)>len(long[0]):
            long=[i]
        elif len(i)==len(long[0]):
            long.append(i)
    return long
if __name__=="__main__":
    print(all_the_longest(['Alan', 'Steve', 'Seymour', 'Kim', 'Susan']))