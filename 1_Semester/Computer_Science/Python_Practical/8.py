""" WAP to accept a number ‘n’ and
         a. Check if ’n’ is prime
         b. Generate all prime numbers till ‘n’
         c. Generate first ‘n’ prime numbers"""
def check_prime(num):
    count=0
    for i in range(1,num//2+1):
        if num%i==0:
            count+=1
    if num==1:
        print(num,"is not a prime nor composite number.")
    elif count>1:
            print(num,"is not a prime number.")
    else:
            print(num," is a prime number.")
    run_again()
def generate_n_prime(num):
    start=2
    lst=[]
    while num>len(lst):
        count=0
        for i in range(1,start+1):
            if start%i==0:
                count+=1
        if count<=2:
            lst.append(start)
        start+=1
    print(lst)
    run_again()
def generate_prime_till_n(num):
    start=2
    lst=[]
    while num>start:
        count=0
        for i in range(1,start+1):
            if start%i==0:
                count+=1
        if count<=2:
            lst.append(start)
        start+=1
    print(lst)
    run_again()
def main():
    choice=int(input("1. Check if ’n’ is prime.\n2. Generate all prime numbers till ‘n’.\n3. Generate first ‘n’ prime numbers.\nEnter your choice what do you want to do?::"))
    num=int(input("Enter your 'n'::"))
    if choice==1:
        check_prime(num) 
    elif choice==2:
        print("Your all required prime number are::")
        generate_prime_till_n(num) 
    elif choice==3:
        generate_n_prime(num)
    else:
        print("worng input!,Enter again")
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