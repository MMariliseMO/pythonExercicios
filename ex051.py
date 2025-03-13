# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Informe o 1º termo: '))
razao = int(input('Informe a razão: '))
decimo = primeiro_termo + (10 -1) * razao # a fórmula para encontrar o n-ésimo termo da PA é an = a1 + (n - 1) * r,

for i in range(primeiro_termo, decimo + razao,  razao):
    print(f'{i}', end = " ") #o end = " " adiciona um espaço em branco ao invés de um linha
