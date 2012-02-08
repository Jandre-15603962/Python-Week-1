# Optimized
import time, re, os
start = time.clock()

file_in = open('doc1.txt')
big_list = ''
for i in file_in:
    big_list += i

clean_list = big_list.split()
print clean_list
#!"#$%&()*+,-./:;<=>?@[\]^_`{|}~
#^a-zA-Z0-9-\s

def sms(a_string):
    original = ""
    sms_txt = ""
    replace_ob  = re.compile(r'\B[aeiou]\B')
    double_char_ob = re.compile(r'([a-z])\1+')
    punctuation_ob = re.compile(r'[^a-zA-Z0-9\s]')
    lower_str = ""
    for i in a_string:
        lower_str += i.lower()                  # Passes each character through sms() one by one and also makes it lower case
    #print lower_str +"\n"
    punctuation = punctuation_ob.sub('',lower_str)
    #print o_list
    replace= replace_ob.sub('',punctuation)       # Only replaces vowels that have not-word-boundry, or vowels completely inside a word.
    #print replace + "\n"
    double_char = double_char_ob.sub(r'\1',replace)
    #print double_char +'\n'
    #print s_list
    return double_char

end_file = open('end_file.txt','w')
end_list = ''
for i in clean_list:
       end_file.write(sms(i).strip().rstrip('\n'))
       end_list += sms(i).strip()+' '

print end_list.split()
dic = dict(zip(end_list,clean_list))

print dic

"""The () around the [a-z] specify a capture group,s
and then the \1 (a backreference) in both the pattern
and the replacement refer to the contents of the first
capture group. Thus, the RE reads "find a letter,
followed by one or more occurrences of that same letter"
and then entire found portion is replaced with a single
occurrence of the found letter."""





elapsed = (time.clock() - start)
print elapsed, 'seconds'

