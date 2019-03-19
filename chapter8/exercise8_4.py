file = open('romeo.txt')
wlist = list()
for line in file :
    words = line.split()
    for word in words:
        #print(word)
        if word in wlist :
            #print(word)
            continue
        wlist.append(word)
wlist.sort()
print(wlist)
