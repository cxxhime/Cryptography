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
