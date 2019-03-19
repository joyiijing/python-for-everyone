#file = open('mbox-short.txt')
fname = input('enter file: ')
if len(fname) < 1 :
    fname = 'mbox-short.txt'
file = open(fname)
wlist = list ()
for line in file :
    if not line.startswith('From'):
        continue

    word = line.split()
    wlist.append(word[1])


wdic = dict()
for k in wlist :
    wdic[k] = wdic.get(k,0)+1
#print (wdic)
key = None
biggest = None
for k,v in wdic.items() :
    #type(v)
    if biggest == None or v > biggest:
        biggest = v
        key = k
print (key,biggest)
