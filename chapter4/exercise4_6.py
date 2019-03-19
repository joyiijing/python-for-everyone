def computepay(a,b):
    if a > 40 :
        return (a-40)*b*1.5+40*b
        #print('pay:',(a-40)*b*1.5 + 40*b)
    else:
        return a*b
        #print('pay:',a*b)

shours = input("enter hours:")
srate = input("enter rate:")
hours = float(shours)
rate = float(srate)
print('the pay is:',computepay(hours,rate))
