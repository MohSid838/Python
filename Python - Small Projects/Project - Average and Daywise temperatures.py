#read data from temps.txt
f=open('temps.txt',mode='r')
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
#operations
temps=[]
for line in f:
    temps.append(float(line[:-1]))
temps_dict=dict(zip(days,temps))
print(temps_dict)
def day_wise():
    for temp in temps_dict:
        print(f"{temp} ---> {temps_dict[temp]}")
def average():
        sum1=0
        for temp in temps:
             sum1=sum1+temp
        return sum1/len(days)
def min1():
    min1=temps_dict['monday']
    day='monday'
    for temps in temps_dict:
         if temps_dict<=min1:
            min1=temps_dict[temps]
            day=temps
    return min1,day
def max1():
    max1=temps_dict['monday']
    day='monday'
    for temps in temps_dict:
         if temps_dict>=max1:
            max1=temps_dict[temps]
            day=temps
    return max1,day
def below_zero():
    print("below are days having temp less than or equal to zero")
    for temp in temps_dict:
        if temps_dict[temp]<=0:
            print(temp)
def seperate_temps():
    sep=float(input("enter temperatur for seperation:"))
    below_sep=[]
    above_eq_sep=[]
    for temp in temps_dict:
        if temps_dict[temp]<sep:
            below_sep.append(temp)
        else:
            above_eq_sep.append(temp)
    print("days having temperature above or equal to",sep)
    for t in above_eq_sep:
        print(t)
while True:
    print("select from the following")
    print("1.Show average of temp\n1.show daywise temperatures\n2.show average of all temperatures\n3.show minimum temperatur\n4.show maximum temperatures\n5.show days having below zero temp\n6.show days")
    ch=int(input("enter your choice:"))
    if ch==1:
       day_wise()
    elif ch==2:
        print("avg temp for curent week is", average())
    elif ch==3:
        minimum=min1()
        print(f"minimi temp is {minimum[0]} for day {minimum[1]}")
    elif ch==4:
        maximum=max1()
        print(f"max temp is {maximum[0]} for day {maximum[1]}")
    elif ch==5:
        below_zero()
    elif ch==6:
        seperate_temps()
    else:
        print("invalid selection")
    ans=input("Do you want to continue (y/n):").lower()
    if ans!='y':
        break
f.close()