fname = input ('enter filename: ')
fh = open(fname)
count = 0
sum = 0.0
for line in fh :
#    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    #print(line)
    pos = line.find(':')
    num = float(line[pos+1:])
    sum = sum + num
    count = count + 1

print('Average spam confidence:',sum/count)
