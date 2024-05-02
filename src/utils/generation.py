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
    return "".join(rand)

def generate_key(passwd):
    key=[]
    # while len(key)<=2*len(passwd):
    randnumb=[random.randint(0, 10) for _ in range(2*len(passwd))]
    key+=randnumb
    return tuple(key)
