#!/usr/bin/env python3
import sys

a = sys.argv[1] # obtém o parâmetro do primeiro cateto
b = sys.argv[2] # obtém o parâmetro do segundo cateto

#  Verifica se os inputs do usuário são digitos, caso não imprima erro e sai da programa
if a.isdigit() == False or b.isdigit() == False:
    print('Erro: Os valores dos catetos devem ser fornecidos em digitos numericos')
    sys.exit()

#   Converta possiveis valores float em int (resulta na perda da precisao decimal)
a=int(a)
b=int(b)

#   Verifica se os valores dos catetos são positivos e menores que 500
if a<500 and b<500 and a>=0 and b>=0:
    #   Calculo da área
    A = (a*b)/2
    #   Imprima string 
    print('A área do triangulo retângulo com lados a=', a ,'e b=', b,' é ',A)
    
#   Mensagem de erro
else: print('Erro: Os valores dos catetos a e b devem ser numeros positivos inferiores ao 500')

sys.exit()
