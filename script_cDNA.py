#!/usr/bin/env python3
import sys

sequênciaDeDNA = sys.argv[1] # obtém a sequência de DNA
n1 = sys.argv[2] # obtém o parâmetro da pos 1 (n1)
n2 = sys.argv[3] # obtém o parâmetro da pos 2 (n2)
n3 = sys.argv[4] # obtém o parâmetro da pos 3 (n3)
n4 = sys.argv[5] # obtém o parâmetro da pos 4 (n4)
n5 = sys.argv[6] # obtém o parâmetro da pos 5 (n5)
n6 = sys.argv[7] # obtém o parâmetro da pos 6 (n6)

parametros = [n1, n2, n3, n4, n5, n6] # Jutando posições numa lista para facilitar depois

for parametro in parametros:
    try:
        parametroInt =int(parametro)  # Verifica se nx é integer, caso não - imprime mensagem de erro e sair da programa

        # Verifica se o valor nx é contido na sequencia, caso não - imprime mensagem de erro e sair da programa
        if parametroInt < 1 or parametroInt > len(sequênciaDeDNA):
            print(f'\nErro: o valor {parametro} precisa ser menor que o comprimento da sequência e não pode ser inferior ao 1')
            sys.exit()

    except ValueError:
        print(f'\nErro: o valor {parametro} deve ser um integer')
        sys.exit()

for i in range(0, 6):
    # Substituir os valores string com int para que possam ser usadas como posições
    parametros[i] = int(parametros[i])

    # Checar coerência da ordem dos parametros
    if i>0:
        if parametros[i]<parametros[i-1]:
            print('\nErro: As posicoes na sequencia devem seguir um ordem cresente')
            sys.exit()    

# Padroniza a capitalização da sequência de DNA
sequênciaDeDNA = sequênciaDeDNA.upper()

# Verifica se as bases são validas
for base in sequênciaDeDNA:
    if base in ('A','T','G','C') == False:
        print(f'\n{base} deveria ser uma base valida, ex; A,T,G,C')

print('\nOs inputs são validos\n')

# Extrair a sequência que está entre a CDS 1 e a CDS 2
seqEntreCDS1eCDS2 = sequênciaDeDNA[parametros[1]:parametros[2]-1]
print('\nSequência que está entre a CDS 1 e a CDS 2:',seqEntreCDS1eCDS2)

# Extrair a sequência que está entre a CDS 2 e a CDS 3
seqEntreCDS3eCDS4 = sequênciaDeDNA[parametros[3]:parametros[4]-1]
print('\nSequência que está entre a CDS 2 e a CDS 3:',seqEntreCDS3eCDS4)

# Verificar se as sequências iniciam com os nucleotídeos GT e terminam com os nucleotídeos AG
if (seqEntreCDS1eCDS2[0:2] == 'GT' and seqEntreCDS1eCDS2[-2:] == 'AG') and (seqEntreCDS3eCDS4[0:2] == 'GT' and seqEntreCDS3eCDS4[-2:] == 'AG'):

    print('\nAs sequências entre CDS 1 e CDS 2, e CDS 3 e CDS 4 iniciam com os nucleotídeos GT e terminam com os nucleotídeos AG')

    # Imprimir na tela a sequência resultante da junção (concatenação) das CDS 1, CDS 2 e CDS 3
    seqConcatenadoCDS1CDS2CDS3 = sequênciaDeDNA[(parametros[0])-1:(parametros[1])] + sequênciaDeDNA[(parametros[2])-1:(parametros[3])] + sequênciaDeDNA[(parametros[4])-1:(parametros[5])]
    print(f'\nA sequência resultante da junção de CDS 1, CDS 2, CDS 3 é {seqConcatenadoCDS1CDS2CDS3}')


print('\nFIM\n')

sys.exit()



