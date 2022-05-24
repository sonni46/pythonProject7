import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
number = 1234567890
simbol = "\/|!£$%&()?^;:_-€[]{}*°§"

leng = 8

allChar = lower + upper + str(number) + simbol

passWord = ''.join(random.sample(allChar,leng))

print(f'la tua Password è: {passWord}')


