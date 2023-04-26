alturas = [1.85, 1.62, 1.75, 1.71, 1.55, 1.98, 2.03, 1.89, 1.60, 1.57, 1.73]

# 1 - Busque uma altura específica na lista. Se a altura estiver na lista 
# retorne o aviso "Achamos a altura!", caso contrário 
# retorne "A altura não está na lista!"
#if 1.78 in alturas:
    #print("Achamos a altura!")
#else:
#    print("A altura não está na lista!")


# 2 - Crie uma nova lista com pessoas com pelo menos 1.85
#altos = []
#for alt in alturas:
#    if alt >= 1.85:
#        altos.append(alt)
#altos.sort()
#print(altos)


# 2.1 - Jeito Supimpa
altos = [alt for alt in alturas if alt >= 1.85]
print(altos)