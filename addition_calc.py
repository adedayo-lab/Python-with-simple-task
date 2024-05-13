# using for loops in unlimited argument of function lesson 17
def add_number(*args):
    total = 0
    for a in args:
        total+= a
    print (total)

# add_number(input("enter your number here : "))//// we should get to figure out y this isn't working
add_number(3, 34, 34)


"""
a = (input("pls enter first val"))
b = (input("pls enter second val"))
ans = a + b
print ans,"is the sum of the input value"
"""
input("press Enter to exit program")