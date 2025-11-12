
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



