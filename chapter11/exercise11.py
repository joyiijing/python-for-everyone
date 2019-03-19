import re

#total = 0
sum = 0

file = open('regex-text-data.txt')
for line in file:
    line = line.rstrip()
    nums = re.findall('[0-9]+',line)
    for num in nums :
        sum = sum + int(num)
print(sum)

#file_data = file.read()
#numbers_str = re.findall('[0-9]+',file_data)
#total = 0
#for number_str in numbers_str:
#    total = total + int(number_str)
#print(total)
