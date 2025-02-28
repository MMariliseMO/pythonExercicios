#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# com f-string
algo = input('Digite algo: ')
print(f'\n0 tipo primitivo desse valor é: {type(algo)}')
print(f'O valor contém apenas espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É uma combinação de letras e números? {algo.isalnum()}')
print(f'Todas as letras são maiúsculas? {algo.isupper()}')
print(f'Todas as letras são minúsculas? {algo.islower()}')
print(f'A 1º letra está maiúscula e o restante minúscula? {algo.istitle()}')


# com o .format()
a = input('Digite algo: ')
print('\nO tipo primitivo desse valor é: ', type(a))
print('O valor contém apenas espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É uma combinação de letras e números? ', a.isalnum())
print('Todas as letras são maiúsculas? ', a.isupper())
print('Todas as letras são minúsculas? ', a.islower())
print('A 1º letra está maiúsculas e o restante minúscula? ', a.istitle())


