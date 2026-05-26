# Write your solution here

#function to store points in exam,exercises secq and to be processed
def point_store():
    recieving_split=[]
    while True:
        input_points=input("Exam points and exercises completed: ")
        if input_points=="":
              break
        recieving_split+=input_points.split(" ",1)
    return recieving_split

#function to process exercises points after spliting
def excer_pts (nspoint: list):
    exerpoint_lists=[]
    exampoint_lists=[]
    for i in range(len(nspoint)):
        if i % 2 != 0:
                exerpoint_lists.append(int(nspoint[i]))
    #tranforming exercises points
    new_exe_pt=[ix // 10 for ix in exerpoint_lists]
    return new_exe_pt
#function to process exam points after spliting
def exam_pts (nspoint: list):
    exerpoint_lists=[]
    exampoint_lists=[]
    for i in range(len(nspoint)):
        if i % 2 == 0:
                exampoint_lists.append(int(nspoint[i]))
    return exampoint_lists


#fun to cal total points with case less than 10 =0 , a is exam

def total_points_case (a: list , b: list ):
    total_points_list=[]
    for i in range(len(a)):
        if a[i]<10:
             total_points_list.append(1)
        else:
             total_points_list.append(a[i]+b[i])
    return total_points_list


#fun to cal total points without case, a is exam
def total_points_stat(a: list , b: list ):
    total_points_list=[]
    for i in range(len(a)):
             total_points_list.append(a[i]+b[i])
    return total_points_list


#statistics function to cal average and pass
def statis(asta: list,b):
     print('Statistics:')
     points_average=float(f"{sum(asta)/len(asta):0.1f}")
     print("Points average:",points_average)
     passs=0
     for i in b:
          if i>14:
               passs+=1
     
     print(f"Pass percentage: {passs/len(b)*100:0.1f}")

#grader fun to present the count of each grade section
def grader(ast: list):
     thresfolds=[14,17,20,23,27,30]
     counter=0
     display=5
     print('Grade distribution:')
     for i in range(len(thresfolds)-1,-1,-1):
        counter=0
        for ii in range(len(ast)):
             if i==0:
               if ast[ii] <=thresfolds[i] :
                    counter+=1   
             elif i>0:
                if ast[ii] <=thresfolds[i] and ast[ii] > thresfolds[i-1] :
                    counter+=1
        print(display,": ","*"*counter, sep="")
        display-=1



res1=point_store()
res2=exam_pts(res1)
res3=excer_pts(res1)
totforstat=total_points_stat(res2,res3)

totforgrader=total_points_case(res2,res3)

stat=statis(totforstat, totforgrader)

final=grader(totforgrader)