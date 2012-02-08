# Unoptimized
import re, time
start = time.clock()
sms_text = ""
file_in = open('pg76.txt')

def sms(sms_text):
    if sms_text.isalpha():
        """If block checks to see if
            letters are alphabetical and kicks out any punctuation."""
        print sms_text
        return sms_text
    elif sms_text == " ":
        return " "
    else:
        return ""

lower_str = ""
for line in file_in:
    for i in line:
        lower_str += sms(i).lower()                 # Passes each character through sms() one by one and also makes it lower case
#print lower_str +"\n"

replace = re.sub(r'\B[aeiou]\B', '',lower_str)  # Only replaces vowels that have not-word-boundry, or vowels completely inside a word.

#print replace + "\n"

double_char = re.sub(r'([a-z])\1+',r'\1',replace)

print double_char.strip() + "\n"



elapsed = (time.clock() - start)
print elapsed


"""The () around the [a-z] specify a capture group,
and then the \1 (a backreference) in both the pattern
and the replacement refer to the contents of the first
capture group. Thus, the RE reads "find a letter,
followed by one or more occurrences of that same letter"
and then entire found portion is replaced with a single
occurrence of the found letter."""
