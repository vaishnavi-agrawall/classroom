u=int(input("enter the numer of units consumed\n"))
if(u<=50):
    bill=u*0.50
elif(u>50 and u<=150):
    bill=u*0.50+u*0.75
elif(u>150 and u<=250):
    bill= u*1.20+(u*0.50+u*0.75)
else:
    bill= u*1.50+(u*1.20+u*0.50+u*0.75)
b=0.20*bill
bill=bill+b
print("Total bill: %d"%bill)