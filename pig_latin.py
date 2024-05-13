# A program that converts words to pig latin
pyg = 'ay'
original = raw_input("Enter a word: ")
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print "Here is the output in Pig Latin:- ", new_word
else:
    print "Empty"

input("press Enter to exit program")

