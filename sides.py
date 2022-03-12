x=int(input("enter 1st side of the triangle\n"))
y=int(input("enter 2nd side of the triangle\n"))
z=int(input("enter 3rd side of the triangle\n"))
if x+y>z or y+z>x or z+x>y:
    print("its a triangle")
else:
    print("not a triangle")