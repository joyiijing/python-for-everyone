file = open('mbox-short.txt')
count = 0
for line in file :
    line = line.strip()
    if line.startswith('From'):
        #print(line)
        word = line.split()
        print(word[1])
        count = count + 1
print(count)
