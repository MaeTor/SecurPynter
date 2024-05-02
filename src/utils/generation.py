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
    randnumb=[random.randint(1, 10) for _ in range(2*len(passwd))]
    key+=randnumb
    return tuple(key)

def cat_passwd(passwd):
    return f"{passwd}{generate_salt(passwd)}"

def chiffrer_passwd(passwd):
    chiffred=[]
    for i,elt in enumerate(cat_passwd(passwd)):
        chiffred += ( ord(elt) + int(generate_key(passwd)[i]) ) % 128
    return chiffred

def afficher_passwd_chiffred():
    for x in chiffrer_passwd():
        print(f"{x} ")


