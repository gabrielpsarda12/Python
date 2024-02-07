# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele

a = input('Digite alguma coisa: \n')

print('Tipo primitivo? {}'.format(type(a)))
print('É numérico? {}'.format(a.isnumeric()))
print('É alfanumérico? {}'.format(a.isalpha()))
print("É um decimal? {}.".format(a.isdecimal()))
print("Está em caixa baixa? {}.".format(a.islower()))
print("É apenas espaço em branco? {}.".format(a.isspace()))
print("Está em caixa alta? {}.".format(a.isupper()))