# WAP to create a pyramid of the character ‘*’ and a reverse pyramid.
def upper_pyramid(num):
    con=num-1
    for i in range(num):
        for j in range(num):
            if j<con:
                print(" ",end="")
            else:
                print("*",end="")
        num+=1
        con-=1
        print()
def lower_pyramid (num):
    num1=num*2-1
    con=0
    for i in range(num):
        for j in range(num1):
            if j<con:
                print(" ",end="")
            else:
                print("*",end="")
        con+=1
        num1-=1
        print()
def run_again():
    choice=input("Did you want to run again?(y/n)::").lower()
    if choice=='y':
        main()
    elif choice=='n':
        print('Thank you for using my program')
    else:
         print('Wrong input!\nEnter again!!')
         run_again()
def main():
    choice=int(input(" Which type of pyramid you want?::\n1.upper pyramid \n2.lower pyramid.\n3.Both pyramid \nEnter your choice:: "))
    num=int(input("Enter how many row's triangle you want?:: "))
    if choice==1:
        upper_pyramid(num)
        run_again()
    elif choice==2:
        lower_pyramid(num)
        run_again()
    elif choice==3:
        upper_pyramid(num)
        lower_pyramid(num)
        run_again()
    else:
        print('wrong input!\nEnter again!!')
        main()
main()