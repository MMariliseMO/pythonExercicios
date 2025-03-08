#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: - Se ele ainda vai se alistar ao serviço militar obrigatório; - Se é a hora de se alistar; - Se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nascimento = int(input('Informe o ano do nascimento: '))
ano_atual = date.today().year #ano atual
idade = ano_atual - ano_nascimento
if idade == 18:
    print(f'Você possui {idade} anos. Está na hora do alistamento.')
elif idade < 18:
    saldo = 18 - idade 
    ano_alistamento = ano_atual + saldo
    print(f'Você possui {idade} anos. Vai se alistar no ano de {ano_alistamento}.')
else:
    saldo = idade - 18
    ano_alistamento = ano_nascimento + 18 
    print(f'Você tem {idade} anos. Já passou do tempo de se alistar. Era para ter feito o alistamento no ano de {ano_alistamento}.')





    #https://docs.python.org/pt-br/3.10/library/functions.html#abs