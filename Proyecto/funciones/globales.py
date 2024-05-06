from os import system
import sys 
from enum import Enum

def borrar_pantalla():
    if sys.platform =='linus' or sys.platform =='darwin':
        system('clear')
    else:
        system('cls')

def pausar_pantalla():
    if sys.platform == 'linux' or sys.platform == 'darwin':
        x=input('presione un tecla para continuar')
    else:
        system('pase')
mi_clinica_medica={
    "data" :{}
}