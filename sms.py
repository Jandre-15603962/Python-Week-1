# Unoptimzed

import re, time
start = time.clock()
input_file = open('doc1.txt')
sms_text = ''
for i in input_file:
    sms_text += i
    

def sms(sms_text):
    if sms_text.isalpha():
        """If block checks to see if
            letters are alphabetical and kicks out any punctuation."""
        return sms_text
    elif sms_text == " ":
        return " "
    else:
        return ""

lower_str = ""
for i in sms_text:
    lower_str += sms(i).lower()                 # Passes each character through sms() one by one and also makes it lower case
#print lower_str +"\n"

replace = re.sub(r'\B[aeiou]\B', '',lower_str)  # Only replaces vowels that have not-word-boundry, or vowels completely inside a word.

#print replace + "\n"

double_char = re.sub(r'([a-z])\1+',r'\1',replace)
"""The () around the [a-z] specify a capture group,
and then the \1 (a backreference) in both the pattern
and the replacement refer to the contents of the first
capture group. Thus, the RE reads "find a letter,
followed by one or more occurrences of that same letter"
and then entire found portion is replaced with a single
occurrence of the found letter."""
sms_output = open('sms_output.txt','w')
for i in double_char:
    sms_output.write(i)

elapsed = (time.clock() - start)
print elapsed, 'seconds'

sms_output.write(str(elapsed))


sms_output.close()
