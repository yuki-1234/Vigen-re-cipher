# Decode plaintext
cipher = input("input Ciphertext : ")
key = input("input key : ")
cipher = cipher.upper()
cipher = cipher.replace(' ', '')
key = key.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher_shift = []
key_shift = []
plain = []

for i in range(len(cipher)):
    for j in range(len(alphabet)):
        if cipher[i] == alphabet[j]:
            cipher_shift.append(j)

for i in range(len(key)):
    for j in range(len(alphabet)):
        if key[i] == alphabet[j]:
            key_shift.append(j)

for i in range(len(cipher)):
    if i == 0:
        print("plaintext is : ", end ="")
    plain.append((cipher_shift[i] - key_shift[i % len(key)]) % 26)
    print(alphabet[(cipher_shift[i] - key_shift[i % len(key)]) % 26], end="")




