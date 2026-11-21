#Escreva um programa em metros e o exiba em centimetros e milímetros.

metros = float( input('Digite um valor em metros: '))
cent = metros * 100
mil = metros * 1000

print('O valor de {} metros em centimetros é {} e em milimetros é {}'.format(metros, cent, mil))