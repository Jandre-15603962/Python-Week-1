# Optimized
import time, re, os
start = time.clock()


def no_punct(a):
    punctuation_ob = re.compile(r'[^a-zA-Z0-9\s]')
    no_punct = punctuation_ob.sub('',a)
    return no_punct


file_in = open('doc1.txt')
nice_file = open('n_file.txt','w')

dic_line = []
for line in file_in:
    #print line
    line_fix = no_punct(line)
    line_np = line_fix.lower().split()
    dic_line += line_np
    if line_np:
        nice_file.write(' '.join(line_np)+' ')

#print dic_line, '\n'       

nice_file.close()
file_in.close()


def sms(a_string):
    replace_ob  = re.compile(r'\B[aeiou]\B')
    double_char_ob = re.compile(r'([a-z])\1+')
    #punctuation_ob = re.compile(r'[^a-zA-Z0-9\s]')
    
    #punctuation = punctuation_ob.sub('',a_string)
    double_char = double_char_ob.sub(r'\1',a_string)
    replace = replace_ob.sub('',double_char)

    return replace

end_file = open('n_file.txt')
sms_text = open('sms_text.txt','w')
dic_sms = ""
for i in end_file:
     sms_text.write(sms(i))
     dic_sms += sms(i)
     #print sms(i)

dictionary_sms = dic_sms.split()
final_dict = {}
insert = map(lambda k, v: final_dict.update({k: v}), dictionary_sms, dic_line)




#print dictionary_sms

re_translate = ''

for i in dictionary_sms:
    re_translate += final_dict[i] + " "

re_translated_file = open('retrans.txt','w')
for n in re_translate:
    re_translated_file.write(n)


end_file.close()

re_list = re_translate.split()

def compare(a,b):
    counter = 0
    counter2 = 0
    counter3 = 0
    for i in a:
        if a[counter] == b[counter]:
            counter += 1
            counter2 += 1
        else:
            counter3 += 1
            counter += 1

    print counter, counter2, counter3
    answer = str(counter2/float(counter) * 100)+'%'
    return answer
print compare(dic_line,re_list),'comparison'

print len(dic_line),len(re_list)



elapsed = (time.clock() - start)
print elapsed, 'seconds'
