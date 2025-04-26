#algoritmo que mostra todos os números primos no intervalo de 2 a 2000.
for w in range(2,2001):
    primo=True
    for a in range(2,w):
        if w%a==0:
            primo=False
            break
    if primo:
        print(w, end="/")