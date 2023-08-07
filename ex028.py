from random import randint
from time import sleep
sorteado = randint(0, 5)
escolha = int(input('Escolha um numero de 0 a 5: '))
print('\033[4;33mPROCESSANDO...')
sleep(2)
if escolha != sorteado:
    print('\033[0;31mInfelizmente você errou, o numero sorteado foi {}'.format(sorteado))
else:
    print('\033[0;32mPARABENS!!!, Você acertou o numero!')
