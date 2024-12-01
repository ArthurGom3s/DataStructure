lista = [1, 2, 2, 2, 3, 3]
contagem = {}
for item in lista:
    contagem[item] = contagem.get(item, 0) + 1


"""
# Iterar pelo dicionário e imprimir cada chave-valor
for chave, valor in contagem.items():
    print(f"{chave}: {valor}")
"""
print(contagem) 