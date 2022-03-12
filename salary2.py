bp=int(input("enter the basic pay of the employee"))
if(bp<10000):
    hra=0.80*bp
    ta=0.80*bp
    salary=bp+hra+ta
    print("salary: %d"%salary)
elif(10000<bp<20000):
    hra=0.85*bp
    ta=0.80*bp
    salary=bp+hra+ta
    print("salary: %d"%salary)
else:
    hra = 0.90*bp
    ta = 0.95*bp
    salary = bp + hra + ta
    print("salary: %d" %salary)
