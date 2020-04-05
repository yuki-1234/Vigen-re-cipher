plain = input("input Plaintext : ")
key = input("input key : ")
plain = plain.upper()
plain = plain.replace(' ', '')
key = key.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plain_shift = []
key_shift = []
cipher = []

for i in range(len(plain)):
    for j in range(len(alphabet)):
        if plain[i] == alphabet[j]:
            plain_shift.append(j)

for i in range(len(key)):
    for j in range(len(alphabet)):
        if key[i] == alphabet[j]:
            key_shift.append(j)

for i in range(len(plain)):
    if i == 0:
        print("ciphertext is : ", end="")
    cipher.append((plain_shift[i] + key_shift[i % len(key)]) % 26)
    print(alphabet[(plain_shift[i] + key_shift[i % len(key)]) % 26], end="")
