# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

real = float(input('Quantos reais voce tem? \nR$'))

dolar = 4.96

carteira = real / dolar

print('Com esse valor R${:.2f} voce pode comprar em dolar: US${:.2f}'.format(real, carteira))