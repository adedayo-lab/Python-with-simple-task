# the age for dating: if male is 22yrs old den we div by 2  and add 7. to know d age for dating bae.
def allowed_dating_age(my_age):
    if my_age <= 18:
        print (" Guy is to young too date")
    girls_age = my_age / 2 + 7
    return girls_age

age_limit = allowed_dating_age input("enter ur males age"))
print ("The guy can date girl's", age_limit, "years of age or older if he wants")
input("press Enter to exit program")


