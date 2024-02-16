# Dictionary Comprehensions 
São uma forma concisa e poderosa de criar dicionários em Python. Elas permitem que você crie um dicionário com base em outro dicionário, iterando sobre seus elementos e aplicando uma expressão a cada um deles.

# A sintaxe básica de uma Dictionary Comprehension é a seguinte:


novo_dicionario = {chave: valor for chave, valor in dicionario_original.items()}

Aqui, chave e valor são as chaves e valores do dicionário original, e a nova_lista novo_dicionario conterá as chaves e valores transformados.

Por exemplo, se você tiver um dicionário de números e quiser criar um novo dicionário contendo o quadrado de cada número, você pode fazer isso com uma Dictionary Comprehension:


numeros = {'um': 1, 'dois': 2, 'tres': 3, 'quatro': 4, 'cinco': 5}
quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}

Aqui, valor ** 2 é a expressão que eleva cada valor ao quadrado, e o novo_dicionario quadrados conterá os quadrados de todos os valores no dicionario_original numeros.

Você também pode adicionar uma condição para filtrar os elementos do dicionário original. Por exemplo, se você quiser criar um novo dicionário contendo apenas os números pares do dicionário original, você pode fazer isso com uma Dictionary Comprehension:


numeros = {'um': 1, 'dois': 2, 'tres': 3, 'quatro': 4, 'cinco': 5}
pares = {chave: valor for chave, valor in numeros.items() if valor % 2 == 0}
Aqui, valor % 2 == 0 é a condição que filtra os números pares, e o novo_dicionario pares conterá apenas os números pares do dicionario_original numeros.

As Dictionary Comprehensions são uma ferramenta poderosa e versátil em Python, e são frequentemente usadas para criar dicionários de forma concisa e eficiente. Elas são uma parte essencial do kit de ferramentas de qualquer programador Python.