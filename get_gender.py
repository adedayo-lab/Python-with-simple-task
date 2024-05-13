# program for getting and storing the gender of a user
def get_gender(sex="Unknown"):
    if sex is "m":
        sex = "Male"
    elif sex is "f":
        sex = "Female"
    print(sex)

get_gender(input("enter m for 'male' or f for 'female'"))
input("press Enter to exit program")


