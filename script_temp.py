#!/usr/bin/env python3
import sys

print('Digite as temperaturas em graus Celsius (separadas por espaço):  ')

stringCelsius = input() # Obtém o string do usuário com os valores em celsius
listaCelsius = stringCelsius.split() #  Transformar os valores no string em elementos de uma lista

for valor in listaCelsius:
    try:
        valorEmCelsius = float(valor)
        valorEmFahrenheit = 9/5 * valorEmCelsius + 32
        print(f'\n{valorEmCelsius:.1f}      {valorEmFahrenheit:.1f}')
    except ValueError:
        print(f'\n{valor}      Erro: O input deve ser um valor numérico válido')

sys.exit()

