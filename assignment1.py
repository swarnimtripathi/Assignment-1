#Code
print("Is every human a good grader")
P=[1,1,0,0]    #Every human does not study well
Q=[0,1,0,1]    #Good graders study well
R=[]           #Is every human good grader
j=0            #position variable
for i in P:
    if i==0:
        R.append(1 and Q[j])
    else:
        R.append(0 and Q[j])
    j+=1
if R.count(1)==4:   #check for tatutology
    print("Yes")
else:
    print("No")
