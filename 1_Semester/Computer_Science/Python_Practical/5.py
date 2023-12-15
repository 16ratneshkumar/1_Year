""" Write A Program To Accept A Name From A User. Raise And Handle Appropriate Exception(S) If The Text Entered By The User Contains Digits And/Or Special Characters."""
def name():
    user_input=input("Enter your name:: ")
    if user_input.isalpha():
        print("Thank you for providing your correct name.")
    else:
        raise ValueError("Invalid name. Please enter only alphabets.")
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
