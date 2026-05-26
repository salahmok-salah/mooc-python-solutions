# Write your solution here
def list_sum(a:list,b:list):
    out=a
    i=0
    while i<len(a) and i<len(b):
         out[i]+=b[i]
         i+=1
    return out
if __name__=="__main__":
    print(list_sum([34,534,64,54],[54,543,-53,-53]))