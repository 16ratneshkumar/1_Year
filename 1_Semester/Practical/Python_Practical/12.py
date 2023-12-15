# Write a function that accepts two strings and returns the indices of all the occurrences of the second string in the first string as a list. If the second string is not present in the first string then it should return -1.
def count(str1,str2):
    count=0
    lstr1=len(str1)
    lstr2=len(str2)
    for i in range(lstr1):
        if str2 in str1[i:i+lstr2]:
            count+=1
    if count==0:
        return -1
    else:
        return [count]
choice="y"
while choice=="y":
    str1=input("Enter any string:: ")
    str2=input("Enter those string you want to count occurrences:: ")
    print(count(str1,str2))
    choice=input("Do you want to use again(y/n):: ").lower()
print("Thank you for using my program!!")
