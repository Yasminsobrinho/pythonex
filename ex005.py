nome = input('Qual o seu nome? ') 
# {:=^20} = o sinal de = vai preencher com  em volta =, o sinal de ^ vai centralizar e o 20 é a quantidade de caracteres que vai ter no total.
# {:20} = o sinal de ^ vai centralizar e o 20 é a quantidade de caracteres que vai ter no total.
# {:<20} = o sinal de < vai alinhar a esquerda e o 20 é a quantidade de caracteres que vai ter no total.
# {:>20} = o sinal de > vai alinhar a direita e o 20 é a quantidade de caracteres que vai ter no total.
print('Prazer em te conhecer {:=^20}!'.format(nome))
