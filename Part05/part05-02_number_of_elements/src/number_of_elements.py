# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    countt=0
    for row in my_matrix:
        for elem in row:
            if elem== element:
                countt+=1
    return countt

if __name__=="__main__":
    print(count_matching_elements([[1,3,4],[3,4,5]]))