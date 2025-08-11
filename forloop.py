#Write a Python program to find the sum of all the numbers except odd numbers 
#between 1 and 20 using a loop. Can you also do this using a while loop?
x=0
for i in range(1, 21):
    if i%2==0:
        x += i
print(x)

#After throwing the dice several times, you got this result,

dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
#Using a for loop find out the followings:

#How many times have you got 6s
y=0
for x in range(len(dice_result)):
    if x==6:
        y1=y+1
    for z in range(len(dice_result)):
        if z==1:
           y2=y+1
print(y1,y2)

#How many times have you got 1s

#How many times have you got 6s two times in a row

     
