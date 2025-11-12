# Chiffrement de César
def cesar(string, decalage):
    string = [char.lower() if char.isupper() else char for char in string]
    result = ""
    for char in string:
        if char.isalpha():
            shifted = ord(char) + decalage
            if shifted > ord('z'):
                shifted = shifted - 26
            elif shifted < ord('a'):
                shifted = shifted + 26
            result += chr(shifted)
        else:
            result += char
    return result


# Déchiffrement de césear
def decesar(string, decalage):
    return cesar(string, -decalage)



# Brute Force du chiffrement de César
def brute_force(string):
    for decalage in range(26):
        print(f'Décalage {decalage} : {decesar(string, decalage)}')
        

def normalize_input(word):
    lower_word = [element.lower() if type(element) == str else element for element in word]
    return lower_word 

print("----- César -----")
print(cesar("Panda du Zoo", 3))
print(decesar("oh edperr hvw od qrxuulwxuh idyrulwh ghv sdqgdv", 3))
print("----- Brute Force -----")
brute_force("Snowi le ragdoll")


# Chiffrement de Vigenère
def vigenere(string, key):
    string = string.lower()
    key = key.lower()
    
    if not key:
        raise ValueError('La clé ne peut pas être vide')
    if not key.isalpha():
        raise ValueError('La clé ne doit contenir que des lettres')
    
    result = "" 
    key_length = len(key)  
    
    for i, char in enumerate(string):
        if char.isalpha():
            indice = ord(char) - ord('a') 
            indice_key = ord(key[i % key_length]) - ord('a')  
            indice_crypted = (indice + indice_key) % 26  
            result += chr(indice_crypted + ord('a'))  
        else:
            result += char
    
    return result  


# Déchiffrement de Vigenère
def devigenere(string, key):
    string = string.lower()
    key = key.lower()
    
    if not key:
        raise ValueError('La clé ne peut pas être vide')
    if not key.isalpha():
        raise ValueError('La clé ne doit contenir que des lettres')
    
    result = "" 
    key_length = len(key)
    
    for i, char in enumerate(string):
        if char.isalpha():
            indice = ord(char) - ord('a')
            indice_key = ord(key[i % key_length]) - ord('a')
            indice_decrypted = (indice - indice_key + 26) % 26
            result += chr(indice_decrypted + ord('a'))  
        else:
            result += char
    
    return result

print("----- Vigenère -----")
print(vigenere("Snowi le ragdoll", "chat"))
print(devigenere("ccascoi hbdg cf zxbxv", "bonjour"))
