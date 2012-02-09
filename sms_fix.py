# Fixed and commented
import time, re, os
start = time.clock()


def no_punct(a):
    """ Removes all punctuation from file input"""
    punctuation_ob = re.compile(r'[^a-zA-Z0-9\s]')
    no_punct = punctuation_ob.sub('',a)
    return no_punct                             # Returns string w/o punctuation


file_in = open('doc1.txt')
nice_file = open('n_file.txt','w')

dic_line = []
for line in file_in:
    #print line
    line_fix = no_punct(line)                   # Removes punctuation line by line
    line_np = line_fix.lower().split()          # Lower case and splits into string
    dic_line += line_np                         # String is saved to be used in dictionary for comparison
    if line_np:
        nice_file.write(' '.join(line_np)+' ')  # Creates normalized file

#print dic_line, '\n'       

nice_file.close()
file_in.close()


def sms(a_string):
    """ Removes double characters and inner vowels"""
    replace_ob  = re.compile(r'\B[aeiou]\B')
    double_char_ob = re.compile(r'([a-z])\1+')
    double_char = double_char_ob.sub(r'\1',a_string)
    replace = replace_ob.sub('',double_char)

    return replace                              # Returns string w/o double characters or inner vowels

end_file = open('n_file.txt')
sms_text = open('sms_text.txt','w')
dic_sms = ""
for i in end_file:
     sms_text.write(sms(i))                     # Writes translated text to file
     dic_sms += sms(i)                          # Creates string for dictionary and comparison
     #print sms(i)

dictionary_sms = dic_sms.split()                # Converts string into list for dictionary use           
final_dict = {}                                 # Empty dictionary
insert = map(lambda k, v: final_dict.update({k: v}), dictionary_sms, dic_line)  #Takes values from two list and updates empty dictionary
                                                                                # The first value of the first list becomes the index of the 
                                                                                # second list's first value. Creates a dictionary w/o repitition


#print dictionary_sms

re_translate = ''                               # Empty string to concatenate sms text translated back to English

for i in dictionary_sms:
    re_translate += final_dict[i] + " "         # Looks for English version of sms text

re_translated_file = open('retrans.txt','w')
for n in re_translate:
    re_translated_file.write(n)                 # Writes translated to file


end_file.close()

re_list = re_translate.split()                  # Creates list for comparison

def compare(a,b):
    """ Counts each word translated, the amout of correctly translated words and the amout of non-matches"""
    counter = 0
    counter2 = 0
    counter3 = 0
    for i in a and b:
        if a[counter] == b[counter]:
            counter += 1
            counter2 += 1
        else:
            counter3 += 1
            counter += 1

    #print counter, counter2, counter3
    answer = str(counter2/float(counter) * 100)+'%'
    return answer                               # Returns % accuracy of back-translation
print compare(dic_line,re_list),'accuracy'

print len(final_dict), len(dic_line),len(re_list)



elapsed = (time.clock() - start)
print elapsed, 'seconds'
