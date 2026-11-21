#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².

larg = float( input('Largura da parede: '))
alt = float( input('Altura da parede: '))
area = larg * alt
tinta = area / 2

print('A dimensão da parede é de {}x{} e a sua área é de {}m²'.format(larg, alt, area))
print('Para pintar essa parede você precisara de {}l de tinta.'.format(tinta))