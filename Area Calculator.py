print("Area calculator")
Z = int (input("1 for triangle, 2 for rectangle,3 for circle ="))

if Z == 1:
    a = float(input("lenght of triangle="))
    b = float(input("Breadth of triangle="))
    print("area=", 0.5*a*b) 
elif Z == 2:
    c= float(input("Breadth of rectangle="))
    d= float(input("Breadth of triangle="))
    print("area", c*d)
elif Z == 3: 
    e= float(input("Radius of circle="))
    print("area", 3.14*e*e)
else:
    print("invalid output")