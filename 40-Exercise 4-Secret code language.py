#coding:
# if the word contains atleast 3 characters,remove the first letter and append it at the end 
# now append three random characters at the starting and the end
# else:
# simply reverse the String

# Decoding
# if the word contains less than 3 characters,reverse it else:
# remove 3 random characters from start and end.now remove the last letter and
# append it to the beginning

# program should ask whether you code or decode

import random
import string

c=str(input("Do you want to code or you want to decode: "))
if c=="code":
    code=str(input('Enter the word: '))
    main_text=code[1:]+code[0]
    starts_with = ''.join(random.sample(string.ascii_lowercase,3))
    ends_with = ''.join(random.sample(string.ascii_lowercase,3))
    print(starts_with+main_text+ends_with)

elif c=="decode":
    decode=str(input('Enter the word: '))
    if len(decode)<3:
        print(decode[::-1])
    else:
        remove=decode[3:-3]
        decoded=remove[-1:]+remove[:-1]
        print(decoded)
else:
    print("Enter the valid word")