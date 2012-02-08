# Optimized
import time, re
start = time.clock()

file_in = open('pg76.txt')

#!"#$%&()*+,-./:;<=>?@[\]^_`{|}~
#^a-zA-Z0-9-\s

def sms(a_string):
    replace_ob  = re.compile(r'\B[aeiou]\B')
    double_char_ob = re.compile(r'([a-z])\1+')
    punctuation_ob = re.compile(r'[^a-zA-Z0-9\s]')
    lower_str = ""
    for i in a_string:
        lower_str += i.lower()                 # Passes each character through sms() one by one and also makes it lower case
    #print lower_str +"\n"

    replace= replace_ob.sub('',lower_str)  # Only replaces vowels that have not-word-boundry, or vowels completely inside a word.
    #print replace + "\n"
    double_char = double_char_ob.sub(r'\1',replace)
    #print double_char +'\n'
    punctuation = punctuation_ob.sub('',double_char)
    return punctuation

end_file = open('end_file.txt','w')
for i in file_in:
       end_file.write(sms(i).strip())
       print sms(i).strip()

"""The () around the [a-z] specify a capture group,s
and then the \1 (a backreference) in both the pattern
and the replacement refer to the contents of the first
capture group. Thus, the RE reads "find a letter,
followed by one or more occurrences of that same letter"
and then entire found portion is replaced with a single
occurrence of the found letter."""





elapsed = (time.clock() - start)
print elapsed, 'seconds'

