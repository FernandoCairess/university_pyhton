# #desafio5 desvenda qual numero possui um maior valor
maior = 0
for valor in range(1,5):
    valor = int(input("digite um valor para a soma:"))
    if valor > maior:
        maior = valor
print("O maior valor é:", maior)