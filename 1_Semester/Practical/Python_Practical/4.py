""" Consider a tuple t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10). WAP to perform following operations:
    a) Print half the values of the tuple in one line and the other half in the next line.
    b) Print another tuple whose values are even numbers in the given tuple.
    c) Concatenate a tuple t2=(11,13,15) with t1.
    d) Return maximum and minimum value from this tuple"""
t1=(1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
t2=(11,13,15)
t=()
print("First half tuple are::\n",t1[0:5])
print("Other half tuple are::\n",t1[5:len(t1)])
for i in t1:
    if i%2==0:
        t=t+(i,)
print("All the even number from given tuple are::\n",t)
print("After concatenation the tuple are::\n",t1+t2)
print("Maximum value of tuple t1 is::\n",max(t1),"\nMinimum value of tuple t1 is::\n",min(t1))