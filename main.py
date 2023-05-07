import math
def encrypt(text, key):
    def cesar_inv(text, key):
        cesar_enc = ""
        for letra in text:
            if letra.isalpha():
                cesar_enc += chr((ord(letra) + key - 65) % 26 + 65)
            else:
                cesar_enc += letra
        return cesar_enc

    def rail(text, key):
        rail_enc = ""
        for i in range(key):
            for j in range(i, len(text), key):
                rail_enc += text[j]
        return rail_enc

    cesar_text = cesar_inv(text, key)
    rail_text = rail(cesar_text, key)
    return rail_text
def decrypt(text, key):
    def cesar_inv(text, key):
        cesar_dec = ""
        for letra in text:
            if letra.isalpha():
                cesar_dec += chr((ord(letra) - key - 65) % 26 + 65)
            else:
                cesar_dec += letra
        return cesar_dec

    # Desloca a mensagem criptografada de acordo com o número de linhas
    n = len(text)
    rail_len = key
    n_rails = (n // (2 * rail_len - 2) + 1) if (n % (2 * rail_len - 2) != 0) else (n // (2 * rail_len - 2))
    rail_seq = [0] * n
    for i in range(n_rails):
        for j in range(rail_len):
            if i * (2 * rail_len - 2) + j < n:
                rail_seq[i * (2 * rail_len - 2) + j] = j
            if i * (2 * rail_len - 2) + (2 * rail_len - j - 2) < n:
                rail_seq[i * (2 * rail_len - 2) + (2 * rail_len - j - 2)] = j

    # Divide a mensagem em blocos do tamanho de cada linha e ordena os blocos
    rail_blocks = [''] * rail_len
    for i in range(rail_len):
        for j in range(n):
            if rail_seq[j] == i:
                rail_blocks[i] += text[j]
    rail_text = ''.join(rail_blocks)

    # Aplica o inverso da cifra de César na mensagem desordenada
    cesar_text = cesar_inv(rail_text, key)

    return cesar_text

text = 'trabalho de sexta feira'
key = 3
enc = encrypt(text,key)
print(enc)
dec = decrypt(enc, key)
print(dec)