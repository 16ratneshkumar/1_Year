#1. WAP to find the roots of a quadratic equation.
def cal_root():
    a=float(input("Enter the coefficient of x²::"))
    b=float(input("Enter the coefficient of x::"))
    c=float(input("Enter the constant term::"))
    det=b**2-4*a*c
    if det>=0:
        root1=float(-b+det**0.5)/(2*a)
        root2=float(-b-det**0.5)/(2*a)
        print("Root of this quadratic equation is \n",root1,'and',root2)
    else:
        print("Root of this quadratic equation is not possible")
    choice=input("Did you want to run again?(y/n)::").lower()
    if choice=='y':
        cal_root()
    else:
        print("Thank you for using my program")
cal_root()
