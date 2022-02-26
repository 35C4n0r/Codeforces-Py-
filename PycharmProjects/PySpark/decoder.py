import random
from Crypto.Cipher import AES

# generate key
gpList = [[13, 19], [7, 17], [3, 31], [13, 19], [17, 23], [2, 29]]
#g, p = random.choice(gpList)
for dd in gpList:
    g, p = dd
    for a in range(1, p):
        #a = random.randint(1, p)
        for b in range(1, p):
            #b = random.randint(1, p)
            k = pow(g, a * b, p)
            k = str(k)
            key = ""
            i = 0
            padding = "uiuctf2021uiuctf2021"
            while (16 - len(key) != len(k)):
                key = key + padding[i]
                i += 1
            key = key + k
            key = bytes(key, encoding='ascii')

            flag = 'b31699d587f7daf8f6b23b30cfee0edca5d6a3594cd53e1646b9e72de6fc44fe7ad40f0ea6'
            #flag = bytearray.fromhex('b31699d587f7daf8f6b23b30cfee0edca5d6a3594cd53e1646b9e72de6fc44fe7ad40f0ea6').decode('ascii')

            iv = bytes("kono DIO daaaaaa", encoding='ascii')
            cipher = AES.new(key, AES.MODE_CFB, iv)
            ciphertext = cipher.decrypt(flag)

            print(ciphertext)
            print()
