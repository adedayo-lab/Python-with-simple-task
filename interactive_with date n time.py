# confidence boost program
from datetime import datetime
now = datetime.now()
current_year = now.year
current_month = now.month
current_day = now.day
# getting user's basic info
name = raw_input("What is your name? ")
quest = raw_input("What is your quest? ")
color = raw_input("What is your favorite color? ")

def get_gender(sex="Unknown"):
    if sex is "m":
        sex = "Male"
    elif sex is "f":
        sex = "Female"

get_gender(input("enter m for 'male' or f for 'female'"))

print "Hello %s, are you sure you want %s,." % (name, quest)
print "This has been registered for you in your 'To Be' list", name
print "As todays Date is %sth, In the %sth month, of the year %s." % (current_day, current_month, current_year)
print name, "I would like to inform you that"
print quest, "you have to spend more time in knowing a lot about your wants and likes,", name
# getting the user's age to specify questions and answer....
age = (input("How old are you"))
if age <= 12:
    my_frnd = "young and smart"
    story = "Bla Bla bla bal...."
    trk_quest = (input("Can i ask you a question %s, "), name)

elif age >= 13:
    my_frnd = "smart and intelligent"
    trk_quest = (input(" what am i if i keep asking questions"))
    if trk_quest == "questionnaire":
        print "corret"
        print "you are truly ", my_frnd

    else:
        print "that was wrong"
    story = "Bla Bla bla bal...."

else:
    print " please enter your correct age", name

likes = (input("can you pleas tell me your like's "))
print "whoa that's very interesting,"
print "I never knew %s could do so much at even %s," % (name, likes)
print "I like you a lot cause you are", my_frnd
# getting the use's gender....
input("press Enter to exit program")



