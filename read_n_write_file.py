# to read and write a file
fw = open("sample.txt", "w")
fw.write("writing some stuff in my text file\n")
fw.write("aigdeipo dougioeh yuefofwugiodebeewgue ewugeuoe")
fw.close()
# to read a file
fr = open("sample.txt", "r")
d_text = fr.read()
print d_text
fr.close()

input("press Enter to exit program")