import string
import random

def generate_salt(passwd):
    chars=string.ascii_letters+string.digits+string.punctuation
    chars_tupled=chars.split()
    charslist=list(chars)
    rand=[]
    while len(rand)<len(passwd):
        rand+=random.choice(charslist)
    # newList=[x for x in charslist)]
    return rand