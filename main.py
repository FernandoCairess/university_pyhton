# desafio3
# for i in range(0,25+1):
#     for t in range(0,25+1):
#         tabuada=i*t
#         print(f"{i} x {t} = {tabuada}\n")

# desafio4
# numeros=0
# numerosoma=0
# for i in range(0,5):
#     numeros=int(input("digite um valor para a soma:"))
#     numerosoma+=numeros
# print(numerosoma)

# #desafio5
# maior = 0
# for valor in range(1,5):
#     valor = int(input("digite um valor para a soma:"))
#     if valor > maior:
#         maior = valor
# print("O maior valor é:", maior)

# # desafio 6
# numuser=int(input("digite um valor para dizer até onde vai o contador"))
# for c in range(2,numuser,2):
#     print(c)

# desafio 7
# somatotal=0
# numusuario= float(input("digite um valor inteiro"))
# while numusuario < 0:
#     print("numero invalido")
#     numusuario = float(input("digite um valor inteiro"))
# for c in range(0,numusuario+1):
#     somatotal+=c
# print(somatotal)

#desafio 8
# n=int(input("Digite um valor para saber seus divisores positivos"))
# for c in range(1,n+1):
#     if (n%c)==0:
#         print(c)
#     else:
#         continue
#desafio 9:
for w in range(2,2001):
    primo=True
    for a in range(2,w):
        if w%a==0:
            primo=False
            break
    if primo:
        print(w)

