# finding the magic number using a while loop
magic_num = input("do enter your magic num: ")
for x in range(101):
    if x is magic_num:
        print x, 'this is the magic number'
        break
    else:
        print(x)

input("press Enter to exit program")
