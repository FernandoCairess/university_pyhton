#desafio4: calcula e imprime a soma de todos os números inteiros entre 1 e n
somatotal=0
numusuario= int(input("digite um valor inteiro"))
while numusuario < 0:
    print("numero invalido")
    numusuario = int(input("digite novamente, mas dessa vez um valor inteiro"))
for c in range(0,numusuario+1):
    somatotal+=c
print(somatotal)