# should be followed and tested well to checks should be later created.
from cmath import sqrt

a = (input("enter the value for a "))
b = (input("enter the value for b "))
c = (input("enter the value for c "))
# recall that X = -b + or - sqrt(b ** 2 - 4 * a * c)/ 2 * a
# the formula for quadratic equations
determinant = (b ** 2 - (4 * a * c))
di_num = 2 * a
deter = determinant
sqr_d = sqrt(deter)
pos = -b + sqr_d
neg = -b - sqr_d
# Formula for the sqrt
# div dem in2 group

print ' Your discriminant', determinant

if deter > 0:
    ans1 = pos / di_num
    ans2 = neg / di_num
    print "Real & Different"
    print "for [+] %s, for [-] %s," % (ans1, ans2)

elif deter == 0:
    sqr_d = sqrt(deter)
    ans01 = pos / di_num
    ans01 = ans02 = -b / di_num
    print "The root are Real & Equal"
    print "so your Ans is ", ans01

elif deter < 0:
    sqr_d = sqrt(deter)
    deter = -b / di_num
    ans11 = -b / di_num + sqr_d / di_num
    ans12 = -b / di_num - sqr_d / di_num
    print "Complex & Different"
    print "for [+] %s, for [-] %s," % (pos, neg)

else:
    print "Check your values properly"

input("press Enter to exit program")