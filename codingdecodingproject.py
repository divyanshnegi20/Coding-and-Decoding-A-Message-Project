import random
import string

def random_str(length=3):
    return ''.join(random.sample(string.ascii_lowercase, length))

message = input("enter a message : ")
words = message.split(" ")
choice = int(input("enter 1 for Coding the message \nAnd 0 for Decoding:  "))
if(choice == 1):
    r1 = random_str()
    r2 = random_str()
    nwords = []
    for word in words:
        if(len(word)>=3):
            newstr = r1 + word[1:] + word[0] + r2
            nwords.append(newstr)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            newstr = word[3:-3]
            newstr = newstr[-1] + newstr[:-1]
            nwords.append(newstr)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))