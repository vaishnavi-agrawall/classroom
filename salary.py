bp=int(input("enter the basic pay of the employee"))
hra=0.15*bp
ta=0.20*bp
salary=bp+hra+ta
print("salary: {}".format(salary))