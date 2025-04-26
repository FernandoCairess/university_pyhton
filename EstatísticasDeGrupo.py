somaidade=0
hmaisvelho=0
nomemaisv= ''
totmulher=0
for p in range (1,5):
    print("-----{}Pessoa-----".format(p))
    nome = str(input('qual o seu nome?')).strip()
    idade = int(input('qual a sua idade?'))
    sexo = str(input('Qual o seu sexo? [M/F]')).strip()
    somaidade+=idade
    media=somaidade/4
    if idade == 1 and sexo in 'Mm':
        hmaisvelho=idade
        nomemaisv=nome
    if sexo in 'Mm' and idade>hmaisvelho:
        hmaisvelho=idade
        nomemaisv=nome
    if sexo in 'Ff' and idade<20:
        totmulher+=1
print('A média das idades é de {}'.format(media))
print('O homem mais velho tem {}anos e o seu nome é {}'.format(hmaisvelho,nomemaisv))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
