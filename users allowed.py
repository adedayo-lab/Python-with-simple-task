# family permisssion program
# program to check the list of users allowed to log in
database = [
    ['fadipe','1234'],
    ['ayzee','2244'],
    ['ayomide','7687'],
    ['timi','5641'],
    ['omolola','4534']
    ]


user_name = raw_input("please enter your user name here : ")

# lets make it really robust,len() & str() using the if statement, no uppercase, all in lower,
# also the max & min of user name allowed to be inputed

pass_word = raw_input("Enter password : ")

# password len(), int(), not more than 4. if more than,
# prompt user to re-input
if [user_name, pass_word] in database:
    sentence = "Welcome Access Granted"

    screen_width = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_width - box_width) / 2
    print
    print ' ' * left_margin + '+'   +'-' * (box_width-2) +  '+'
    print ' ' * left_margin + '|  ' +' ' * text_width    +'  |'
    print ' ' * left_margin + '|  ' +      sentence      +'  |'
    print ' ' * left_margin + '|  ' +' ' * text_width    +'  |'
    print ' ' * left_margin + '+'   +'-' * (box_width-2) +  '+'
    print

elif[user_name, pass_word] != database:
    sentence = "Access Denied !!!"

    screen_width = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_margin = (screen_width - box_width) / 2
    print
    print ' ' * left_margin + '+'   +'-' * (box_width-2) +  '+'
    print ' ' * left_margin + '|  ' +' ' * text_width    +'  |'
    print ' ' * left_margin + '|  ' +      sentence      +'  |'
    print ' ' * left_margin + '|  ' +' ' * text_width    +'  |'
    print ' ' * left_margin + '+'   +'-' * (box_width-2) +  '+'
    print

input ("press enter TO EXIT ")


