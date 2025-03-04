#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Informe o nome da cidade: ')) .strip() #o strip() para eliminar os espaços desnecessários
print(f'{cidade[:5].upper() == "SANTO"}') #[:5], pois "Santo tem 5 letras", upper() para converter para maiúsculo e o == "SANTOS" depois de converter tudo para maiúsculo ele informa que é igual ao "SANTO"


cid = str(input('Digite o nome da cidade: ')) .strip()
print(f'A cidade {cidade[:5]. capitalize() == " Santo"}')