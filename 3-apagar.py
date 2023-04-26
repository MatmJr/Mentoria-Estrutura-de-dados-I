# Crie uma nova lista retirando as Strings vazias da lista a seguir:
list_emp = ["Nome1", "", "Nome2", "Nome3", "", "Nome4"]
#lista_nomes = []
#for nome in list_emp:
#    if nome != "":
#        lista_nomes.append(nome)
#print(lista_nomes)
        

# jeito supimpa
print(list(filter(None, list_emp)))