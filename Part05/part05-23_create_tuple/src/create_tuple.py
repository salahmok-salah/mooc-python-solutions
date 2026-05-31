# Write your solution here
def create_tuple(x: int, y: int, z: int):
    list= sorted([x,y,z])
    tuplee=(list[0],list[2],sum(list))
    return tuplee
if __name__=="__main__":
    print(create_tuple(3,4,5))