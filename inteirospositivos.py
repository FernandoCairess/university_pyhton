#algoritmo que recebe um inteiro positivo n e imprime todos os divisores positivos de n.
n=int(input("Digite um valor para saber seus divisores positivos"))
for c in range(1,n+1):
    if (n%c)==0:
        print(c)
    else:
        continue