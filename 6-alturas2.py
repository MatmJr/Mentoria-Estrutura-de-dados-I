alturas = [1.85, 1.62, 1.75, 1.71, 1.55, 1.98, 2.03, 1.89, 1.60, 1.57, 1.73]

# 1 - Crie uma nova lista passando de metros para pés (multiplicas por 3.28).
mudanca_unidades = [round(alt*3.28,2) for alt in alturas]
#print(mudanca_unidades)

# 2 - Faça a mudança unidade trocando para 0 os valores menores ou iguais a 1.70
print([round(alt*3.28, 2) if alt >= 1.7 else 0 for alt in alturas])