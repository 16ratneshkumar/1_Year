# Write a function that prints a dictionary where the keys are numbers between 1 and 5 and the values are cubes of the keys
def make_dct():
    dict={}
    for i in range(1,6):
        dict[i]=i**3
    print(dict)
make_dct()