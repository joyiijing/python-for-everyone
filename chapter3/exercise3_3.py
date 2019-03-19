s_score = input('enter the score:')
score = float(s_score)
if score < 0 or score > 1 :
    print('this score is out of range')
    exit()
elif score >= 0.9 :
    print('A')
elif score >= 0.8 :
    print('B')
elif score >= 0.7 :
    print('C')
elif score >= 0.6 :
    print('D')
else :
    print('F')
