exerpoint_lists=[55,656,33,22,11,23,525]
newexerciespoints=[i // 10 for i in exerpoint_lists]
print(newexerciespoints)
points_average=float(f"{sum(exerpoint_lists)/len(exerpoint_lists) :0.1f}")
print(points_average)


def grader(ast: list):
     thresfolds=[14,17,20,23,27,30]
     counter=0
     display=5
     for i in range(len(thresfolds) - 1, -1, -1):
        counter=0
        for ii in range(len(ast)):
             if ast[ii] <=thresfolds[i] and ast[ii] > thresfolds[i-1] :
                  counter+=1
        print(display,": ","*"*counter, sep="")
        display-=1
grader([13,15,18,20,24,27])

def statis(asta: list):
     points_average=float(f"{sum(asta)/len(asta) :0.1f}")
     print("Points average:",points_average)
     passs=0
     for i in asta:
          if i>14:
               passs+=1
     print("Pass perecentage:", passs/len(asta))
     statis([13,15,18,20,24,27])