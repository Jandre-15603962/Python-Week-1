# Optimized
import time, re, os
start = time.clock()

file_in = open('doc1.txt')
nice_file = open('n_file.txt','w')
for line in file_in:
    print line
    line_fix = line.lower().split()
    if line_fix:
        nice_file.write(' '.join(line_fix)+' ')

nice_file.close()
file_in.close()

def sms(a_string):
    replace_ob  = re.compile(r'\B[aeiou]\B')
    double_char_ob = re.compile(r'([a-z])\1+')
    punctuation_ob = re.compile(r'[^a-zA-Z0-9\s]')
    
    punctuation = punctuation_ob.sub('',a_string)
    double_char = double_char_ob.sub(r'\1',punctuation)
    replace = replace_ob.sub('',double_char)

    return replace

end_file = open('n_file.txt')
sms_text = open('sms_text.txt','w')
for i in end_file:
     sms_text.write(sms(i))
     print sms(i)

end_file.close()
