''' WAP to create a list of the cubes of only the even integers appearing in the input list (may
have elements of other types also) using the following:
    a. 'for' loop
    b. list comprehension'''
input_lst=list(map(int,input("Enter the number of list with ',' ::").split(',')))
def by_loop():
    lst=[]
    for i in input_lst:
        if i%2==0:
            lst.append(i**3)
    print("List for all even number cube from the given or input list",lst)
def by_comp():
    lst=[i**3 for i in input_lst if i%2==0]
    print(lst)