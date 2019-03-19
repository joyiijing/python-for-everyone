#largest = -1
largest = None
smallest = None
while True :
    snum = input('enter a number: ')
    if snum == 'done' :
        break
    try :
        num = float(snum)
    except :
        print ('Invalid input')
        continue
    #print (num)
    #if  :
    #    smallest = num
    if smallest == None or num > largest :
        largest = num
    if smallest == None or num < smallest :
        smallest = num

print ("Maximum is: ",largest)
print ("Minimum is: ",smallest)
