# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

day = int(input('Digite o dia que nasceu: '))
month = int(input('Digite o mês: '))
year = int(input('Digite o ano: '))

print('Data de nascimento: {}/{}/{}'.format(day, month, year))
print('Nasceu dia {} mês {} de {}'.format(day, month, year))
