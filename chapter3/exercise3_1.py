shours = input("enter hours:")
srate = input("enter rate:")
hours = float(shours)
rate = float(srate)
if hours > 40:
    rate2 = 1.5 * rate
    pay = (hours - 40) * rate2 + 40 * rate
else :
    pay = hours * rate
print(pay)
