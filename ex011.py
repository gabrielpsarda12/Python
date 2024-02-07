# Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input("Digite a largura da parede em metros: "))
alt = float(input("Digite a altura da parede em metros: "))

area = larg * alt
qtdTinta = area / 2

print('')

print(f'A área da parede é de {area:.2f} metros quadrados. \nE será ' +
      f'necessário {qtdTinta:.2f} litros de tinta para pintá-la.')
