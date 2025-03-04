#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Informe o nome da cidade: ')) .strip() #o strip() para eliminar os espaços desnecessários
print(f'{cidade[:5].capitalize() == "Santo"}') #[:5], pois "Santo tem 5 letras", capitalize() para converter para a primeira letra maiúscula e o restante minúscula, e o == "Santo" depois de converter tudo ele informa que é igual ao "Santo"

