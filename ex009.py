#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.

n1 = float( input('Digite a sua primeira nota: '))
n2 = float( input('Digite a sua segunda nota:'))
m = (n1 + n2)/ 2

print('A media entre {} e {} é {}'. format(n1, n2, m))