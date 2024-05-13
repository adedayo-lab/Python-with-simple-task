import random
sequence = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
seq = list(sequence)
codelist = []
counter = 0
while len(codelist) < 500:
    code = ""
    counter = counter +1
    print(counter)
    while len(code) < 12:
        code = code + str(random.choice(seq))

    try:
        codelist.index(code)
    except ValueError:
        codelist.append(code)


file = open('codefile.txt','w')
for item in codelist:
    file.write("%s\n" % item)
