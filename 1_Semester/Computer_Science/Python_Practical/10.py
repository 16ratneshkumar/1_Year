""" WAP to perform the following operations on a string
    a. Find the frequency of a character in a string.
    b. Replace a character by another character in a string.
    c. Remove the first occurrence of a character from a string.
    d. Remove all occurrences of a character from a string"""
def count(str):
      dict={}
      for i in str:
          count=str.count(i)
          dict[i]=count
      print(dict)
      run_again()
def replace(str):
    str1=input('Which character you want to change::')
    str2=input('Which is your new character::')
    str=str.replace(str1,str2)
    print(str)
    run_again()
def remove(str):
    str1=''
    char_del=input('which first character you want to delete::')
    for i in str:
        if i==char_del:
            break
        else:
            str1+=i
    ln=len(str1)+1
    print(str.replace(str[0:ln],str1[0:ln]))
    run_again()
def remove_all(str):
    str1=''
    char_del=input('which character you want to delete::')
    for i in str:
        if i!=char_del:
            str1+=i
    print(str1)
    run_again()
def main():
    choice=int(input("1. Find the frequency of a character in a string.\n2. Replace a character by another character in a string.\n3. Remove the first occurrence of a character from a string.\n4. Remove all occurrences of a character from a string\nEnter your choice::"))
    str=input("Enter your string:: ")
    if choice==1:
        count(str)
    elif choice==2:
        replace(str)
    elif choice==3:
        remove(str)
    elif choice==4:
        remove_all(str)
    else:
        print("Wrong input!\nEnter again!!")
        main()
def run_again():
    choice=input("Did you want to run again?(y/n)::").lower()
    if choice=='y':
        main()
    elif choice=='n':
        print('Thank you for using my program')
    else:
         print('Wrong input!\nEnter again!!')
         run_again()
main()