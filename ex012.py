#crie um programa que leia quantos dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

din = float( input('Quanto dinheiro você tem na carteira? '))

dolar = din / 5.75

print('com R${:.2f} você pode comprar US${:.2f}'.format(din, dolar))