#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite seu nome completo: ')) .strip()

print(f'Seu nome {nome} tem "Silva"?\n {"SILVA" in nome.upper()}')