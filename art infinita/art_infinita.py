import random
import time
from art import *
from colorama import just_fix_windows_console
just_fix_windows_console()

vermelho = '\033[31m' 
verde = '\033[32m'
azul = '\033[34m'
ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'
branco = '\033[37m'
negrito = '\033[1m'
reverso = '\033[2m'

arr = [vermelho, verde, azul, ciano, magenta, amarelo, branco]

danielold = 0

tprint(negrito+"Start!!")

for x in range(int(1e18)):
    daniel = random.randint(0,6)
    if danielold != daniel:
        danielold = daniel
        print(arr[daniel]+randart()+"\n")
        time.sleep(1)   
        
    