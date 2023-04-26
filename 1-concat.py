# Crie uma nova lista que contenha o 0º item de índice de ambas as listas, 
# depois o 1º item de índice e assim por diante até o último elemento. 
# Quaisquer itens restantes serão adicionados no final da nova lista.

list_1 = ["M", "na", "i", "Mar"]
list_2 = ["y", "me", "s", "co"]
list_words = []

for index in range(len(list_1)):
    list_words.append(list_1[index] + list_2[index])
#print(list_words)


# Crie uma string com todas as palavras encontradas
frase = " "
for i in range(len(list_words)):
    frase += list_words[i] + " "

#print(frase)


# jeito supimpa 

print(" ".join(list_words))