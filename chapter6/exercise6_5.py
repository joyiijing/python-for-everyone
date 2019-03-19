# This first line is provided for you
#text = "X-DSPAM-Confidence:    0.8475";

text = "X-DSPAM-Confidence:    0.8475"
#pos = text.find('0')
pos = text.find(':')
num = float(text[pos+1:])
print (num)
