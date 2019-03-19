fname = input('enter file: ')
if len(fname) < 1 : fname =  ('mbox-short.txt')
file = open (fname)
#words = list()
#times = list()
hdic = dict()

for line in file :
    if not line.startswith('From'):
        continue
    words = line.split()
    if len(words) > 5 :
        times = words[5].split(':')
    #print (words)

#        times.append(words[5])
#print(times)
#hours = list()
#for i in times :
#    words = i.split(':')
        hours = times[0]
#    print(hours)
#for i in hours :
        hdic[hours] = hdic.get(hours,0) + 1


#sorted(hdic)
#print(hdic)
l =list()
for k,v in hdic.items():
    tuple = (k,v)
    l.append(tuple)
l.sort()
for k,v in l:
    print(k,v)
#print(srt)

#print (srt)
