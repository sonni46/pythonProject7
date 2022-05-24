import  string
import random

def PassWord_generator():
    char = string.ascii_lowercase + string.ascii_uppercase + string.digits
    size = 8
    return ''.join(random.choice(char) for i in range(size))

n = 0

while n < 20:
    print(PassWord_generator())
    n = n + 1