fname = input ('enter the file name: ')
fhand = open(fname)
for line in fhand :
    line = line.strip()
#    line = line.upper()
    print(line.upper())
