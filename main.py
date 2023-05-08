import random

# Cifra de César
def cesar(text, key):
    cesar_enc = ""
    for letra in text:
        if letra.isalpha():
            if letra.isupper():
                cesar_enc += chr((ord(letra) - 65 + key) % 26 + 65)
            else:
                cesar_enc += chr((ord(letra) - 97 + key) % 26 + 97)
        else:
            cesar_enc += letra
    return cesar_enc

# Vernam-Mauborgne
def vernam(text, key):
    vernam_enc = ""
    for i in range(len(text)):
        byte = ord(text[i]) ^ ord(key[i])
        vernam_enc += chr(byte)
    return vernam_enc

# Gera chave aleatória para Vernam-Mauborgne
def generate_key(length):
    key = ""
    for i in range(length):
        key += chr(random.randint(0, 255))
    return key

# Camada 1: Cifra de César
def layer1_encrypt(text, key):
    return cesar(text, key)

def layer1_decrypt(text, key):
    return cesar(text, -key)

# Camada 2: Vernam-Mauborgne
def layer2_encrypt(text, key):
    vernam_key = generate_key(len(text))
    return vernam(vernam(text, vernam_key), key), vernam_key

def layer2_decrypt(text, key, vernam_key):
    return vernam(vernam(text, key), vernam_key)

# Entrada
text = "trabalho do lucas e do bruno"
key1 = 5
key2 = generate_key(len(text))

# Criptografia
layer1_enc = layer1_encrypt(text, key1)
layer2_enc, vernam_key = layer2_encrypt(layer1_enc, key2)

# Saída
print("Texto original:", text)
print("Texto criptografado:", layer2_enc)
print("Chave de Vernam-Mauborgne:", [ord(c) for c in vernam_key])
print("Texto descriptografado:", layer1_decrypt(layer2_decrypt(layer2_enc, key2, vernam_key), key1))