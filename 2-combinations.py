import itertools
# Apresente todas as combinações possíveis para as duas 
# listas a seguir mantendo a ordem saudação + nome:

saudacoes = ["Olá, ", "Oi, "]
nomes = ["Nome1" , "Nome2", "Nome3", "Nome4"]

#for i in range(len(saudacoes)):
    #for j in range(len(nomes)):
        #print(saudacoes[i] + nomes[j])

# jeito supimpa


for saudacao, nome in itertools.product(saudacoes, nomes):
    print(saudacao + nome)