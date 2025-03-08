#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO! - Média entre 5.0 e 6.9: RECUPERAÇÃO! - Média 7.0 ou superior: APROVADO!.

nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print(f'A média {media:.1f}, indica que você está REPROVADO!')
elif media >= 5 and media < 7:
    print(f'A média {media:.1f}, indica que você está em RECUPERAÇÃO!')
else:
    print(f'A média {media:.1f}, indica que você está APROVADO!')