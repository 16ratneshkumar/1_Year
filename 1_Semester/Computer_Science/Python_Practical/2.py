""" WAP that accepts a character and performs the following:
    a. print whether the character is a letter or numeric digit or a special character.
    b. if the character is a letter, print whether the letter is uppercase or lowercase.
    c. if the character is a numeric digit, prints its name in text (e.g., if input is 9, output is NINE)."""
def check_input():
    char=input("Enter your input either character, number or special character::")
    dct={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:'Zero'}
    if len(char)!=1:
        print("Enter only 1 input")
        check_input()
    elif char.isalpha():
        print("Your input is character")
        if char.isupper():
            print("Your input is in uppercase")
        else:
            print("Your inpur is in lower case")
    elif char.isdigit():
        print("Your input is digit and there numeric digit is",dct[int(char)])
    else:
        print("Your input is special character")
    run_again()
def run_again():
    choice=input("Did you want to run again?(y/n)::").lower()
    if choice=='y':
        check_input()
    elif choice=='n':
        print('Thank you for using my program')
    else:
         print('Wrong input!\nEnter again!!')
         run_again()
check_input()