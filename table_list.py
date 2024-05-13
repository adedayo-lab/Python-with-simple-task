# program to calculate tables taken in a restaurant database.

num_sit_taken = [2, 33, 13, 14, 4, 45]
print ("Here are the numbers of site still available")

for x in range(0, 50, 1):
    if x in num_sit_taken:
        continue
    print (x)

print "This are the one's taken already"
for sit in num_sit_taken:

    print (sit)

# with the use of set... this program can be re-modified
num_sit_taken ={2, 33, 13, 14, 4, 45}
print num_sit_taken

if 2 in num_sit_taken:
    print "table num 2 is already taken"

elif 33 in num_sit_taken:
    print "table num 33 is already taken"

elif 13 in num_sit_taken:
    print "table num 13 is already taken"

elif 14 in num_sit_taken:
    print "table num 14 is already taken"

elif 4 in num_sit_taken:
    print "table num 4 is already taken"


elif 45 in num_sit_taken:
    print "table num 45 is already taken"

else:
    print "Do check manually please"

input("press Enter to exit program")

