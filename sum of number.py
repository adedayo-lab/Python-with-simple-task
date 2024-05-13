a = 1
s = 0
print ('enter numbers to add to the sum.')
print ('enter 0 to quit. ')
while a != 0:
    print ('current Sum: ', s)
    a = float(input('Number ? '))
    a = float(a)
    s += a
print ('Total Sum = ', s)
input("press Enter to exit program")
