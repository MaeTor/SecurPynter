import string
import random
from typing import Tuple

def generate_salt(passwd):
    chars=string.ascii_letters+string.digits+string.punctuation
    rand=[]
    while len(rand)<len(passwd):
        rand+=random.choice(chars)
    return "".join(rand)

def generate_key(passwd):
    key=[]
    # while len(key)<=2*len(passwd):
    randnumb=[random.randint(1, 10) for _ in range(2*len(passwd))]
    key+=randnumb
    return tuple(key)

def cat_passwd(passwd):
    return f"{passwd}{generate_salt(passwd)}"

def chiffrer_passwd(string="",t=()):
    result = ''
    for i in range(len(string)):
        result += chr((ord(string[i]) + t[i]) % 127)
    return result


def generate_string(longueur: int = 0) -> str:
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longueur))


def generate_tuple_number(longueur: int = 0) -> Tuple[int]:
    return tuple(random.randrange(1, 10) for _ in range(longueur))

