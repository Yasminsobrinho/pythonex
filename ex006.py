n1 = int(input('Um valor:'))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rd = n1 % n2
#print('A soma vale {}'.format(n1+n2)) criar a variavel quando o valor sera usado para mais alguma coisa, caso contrario, pode-se colocar o valor diretamente no print
print('A soma vale {}, o produto vale {} e a divisão vale {}'.format(s, m, d))
print('A divisão inteira vale {} e a potência vale {} e o resto da divisão vale {}'.format(di, e, rd))