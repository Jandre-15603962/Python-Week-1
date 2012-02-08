# Unoptimized

import re, time

start = time.clock()

input_file = open('doc1.txt')

sms_text = ''

for i in input_file:
    sms_text += i.lower()                           # Lower case


replace_ob  = re.compile(r'\B[aeiou]\B')            # Removes vowels within borders
double_char_ob = re.compile(r'([a-z])\1+')          # Removes double characters
punctuation_ob = re.compile(r'[^a-zA-Z0-9\s]')      # Removes punctuation

                       
replace= replace_ob.sub('',sms_text)  # Only replaces vowels that have not-word-boundry, or vowels completely inside a word.



double_char = double_char_ob.sub(r'\1',replace)
"""The () around the [a-z] specify a capture group,
and then the \1 (a backreference) in both the pattern
and the replacement refer to the contents of the first
capture group. Thus, the RE reads "find a letter,
followed by one or more occurrences of that same letter"
and then entire found portion is replaced with a single
occurrence of the found letter."""
#print double_char +'\n'

punctuation = punctuation_ob.sub('',double_char)        # Substitutes punctuation with empty string
#print punctuation

end = punctuation.split()
#print end
sms_opt = open('sms_opt.txt','w')
for i in end:
    sms_opt.write(''.join(i)+' ')                   # Writes output to file

elapsed = (time.clock() - start)
sms_opt.write(str(elapsed))
