#13. WAP to accept a name from a user. Raise and handle appropriate exception(s) if the text entered by the user contains digits and/or special characters.
def name():
    user_input=input("Enter your name:: ")
    if user_input.isalnum():
        print("Thank you for providing you name.")
    else:
        print("Please right correct name without using special character.")
        name()
    run_again()
def run_again():
    choice=input("Did you want to run again?(y/n)::").lower()
    if choice=='y':
        name()
    elif choice=='n':
        print('Thank you for using my program')
    else:
         print('Wrong input!\nEnter again!!')
         run_again()
name()