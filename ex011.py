#faça um programa que leia um numero qualquer e mostre na tela a sua tabuada.

n = int( input('Digite um número: '))

for cont in range(1, 11):
    print('{} x {} = {}'.format(n, cont, (n * cont)))