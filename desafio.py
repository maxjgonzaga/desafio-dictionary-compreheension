'''# Desafio 4 
Usando a lista seguir como base:
sorteios = ['sorteio1','sorteio2','sorteio3']
participantes = ['joel','jessica', 'maria','cris','Larissa', 'rafael', 'marcus', 'john']
crie a seguir, selecionando o ganhador aleatóriamente um nomes da lista de participantes. A ideia é simular quem irá ganhar cada sorteio, sua lista deve gerar a seguinte estrutura(porém o nome pode vir a ser diferente, já que estamos selecionando os nomes aleatóriamente)

{
    sorteio1: 'cris',
    sorteio2: 'rafael',
    sorteio3: 'marcus',

}'''
import random
from pprint import pprint

sorteios = ['sorteio1', 'sorteio2', 'sorteio3']
participantes = ['joel', 'jessica', 'maria',
                 'cris', 'Larissa', 'rafael', 'marcus', 'john']
pprint({sorteio: random.choice(participantes) for sorteio in sorteios})

'''
# Desafio 5 

Precisamos de dados de testes para criar contas temporárias,no momento precisamos de gerar 5 valores de 1 a 100, 
e esses valores precisam  Precisamos gerar 5 valores de 1 a 100 aleatóriamente. E estes valores precisam ser 
gerados para cada grupo na lista abaixo grupos 

grupos = ['grupo 1', 'grupo 2', 'grupo 3']

O resultado esperado é o dicionário com a estrutura a seguir(os valores entre contindos dentro da lista 
estarão diferentes, uma vez que os valores abaixo foram geradores aleatóriamente)

{
 'grupo 1': [93, 97, 63, 36, 34],
 'grupo 2': [81, 24, 22, 46, 52],
 'grupo 3': [5, 35, 6, 86, 37]
}'''
# RESOLUÇÃO DESAFIO
grupos = ['grupo 1', 'grupo 2', 'grupo 3']
pprint({grupo: [random.randint(1, 101) for i in range(5)] for grupo in grupos})
