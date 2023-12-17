''' WAP to read a file and
    a. Print the total number of characters, words and lines in the file.
    b. Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.
    c. Print the words in reverse order.
    d. Copy even lines of the file to a file named ‘File1’ and odd lines to another file named ‘File2’.'''
def main():
    with open(r'.\1_Semester\Practical\Python_Practical\ratnesh.txt','r') as file_obj:
        dict={}
        file1=''
        file2=""
        count=1
        str=file_obj.read()
        lst=str.split(' ')
        for i in str:
          if i.isalpha():
              count=str.count(i)
              dict[i]=count
        char=sum(dict.values())
        word=len(lst)
    with open(r'.\1_Semester\Practical\Python_Practical\ratnesh.txt','r') as file_obj:
        read=file_obj.readlines()
        line=len(read)
        for i in read:
            if count%2==0:
                file1+=i
            else:
                file2+=i
            count+=1
    choice=int(input("1.Print the total number of characters, words and lines in the file.\n2.Calculate the frequency of each character in the file. Use a variable of dictionary type to maintain the count.\n3.Print the words in reverse order.\n4.Copy even lines of the file to a file named ‘File1’ and odd lines to another file named ‘File2’.\nEnter your choice:: "))
    if choice==1:
        print("\nDetails of file are shown here::\ncharacters::\t",char,"\nwords::\t",word,"\nlines::\t",line," \n\n")
    elif choice==2:
        print("\nFrequency of each character of file is::\n",dict,"\n\n")
    elif choice==3:
        str1=''
        lst=str.split('\n')
        print('\nFile data in reverse are shown below::\n')
        for i in lst:
            if i=="":
                pass
            else:
                lst=i.split(" ")
                for i in lst:
                    str1=i+" "+str1
                str1="\n"+str1
        print(str1," \n\n")
    elif choice==4:
        with open(r".\1_Semester\Practical\Python_Practical\File1.txt","w") as file_1:
            file_1.writelines(file1)
        with open(r".\1_Semester\Practical\Python_Practical\File2.txt","w") as file_2:
            file_2.writelines(file2)
        print("Files are separated successfully!!\nFile1 for odd lines\nFile2 for even lines")
    else:
        print("\nwrong input!\nEnter again!!\n")
        main()
    run_again()
def run_again():
    choice=input("Did you want to run again?(y/n)::").lower()
    if choice=='y':
        main()
    elif choice=='n':
        print('Thank you for using my program')
    else:
         print('\nWrong input!\nEnter again!!\n')
         run_again()
main()
