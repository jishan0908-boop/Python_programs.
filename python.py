def root(a,b,c):
    D=((b**2)+(4*a*c))
    if D>0:
        root_1=((-b)+(D**(0.5)))/(2*a)
        root_2=((-b)-(D**(0.5)))/(2*a)
        print("Roots of the quadratic  equations are : ", root_1, root_2)
    else:
        print("Roots are not possible")

a=int(input("enter the x2 value "))
b=int(input("enter the x value "))
c=int(input("enter the constant value"))

root(a,b,c)
