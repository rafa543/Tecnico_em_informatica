from ast import If
from functools import update_wrapper
from re import M


nome = input('Digite Seu Nome: ')
tamanho = len(nome)
if tamanho >= 6:
    print('Nome muito Grande')
elif tamanho <= 4:
    print('Nome muito curto')
elif tamanho >= 5 :
    print('Nome Normal')
nmr = 11.1111
print(f'{nmr:.2f}')
