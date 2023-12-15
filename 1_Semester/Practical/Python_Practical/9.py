""" WAP to swap the first n characters of two strings."""
def swap_str():
    str1=input("Enter your 1 string:: ")
    str2=input("Enter your 2 string:: ")
    num=int(input('Enter how many character you want to exchange:: '))
    sav=str1[0:num]
    str1=str1.replace(str1[0:num],str2[0:num])
    str2=str2.replace(str2[0:num],sav)
    print(" After swapping the string your first string is",str1," \nAfter swapping the string your second string is",str2)
    run_again()
def run_again():
    choice=input("Did you want to run again?(y/n)::").lower()
    if choice=='y':
        swap_str()
    elif choice=='n':
        print('Thank you for using my program')
    else:
         print('Wrong input!\nEnter again!!')
         run_again()
swap_str()