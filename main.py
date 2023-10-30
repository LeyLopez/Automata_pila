from ADP import AutomataDePila
from GUI import Interface
from PySide6.QtWidgets import QApplication

import sys

def iniciar():

    automata = create_automata()
    aplicacion = QApplication(sys.argv)
    root = Interface(automata)
    root.show()
    sys.exit(aplicacion.exec())
    
def create_automata():
    
    estados = {'p', 'q', 'r'}
    alfabeto_entrada = {'a', 'b', ''}
    alfabeto_pila = {'a', 'b', '#'}
    
    transiciones = {
        ('p', 'b', 'b'): ('p', 'bb'),
        ('p', 'a', 'b'): ('p', 'ba'),
        ('p', 'b', 'a'): ('p', 'ab'),
        ('p', 'a', 'a'): ('p', 'aa'),
        ('p', 'b', '#'): ('p', '#b'),
        ('p', 'a', '#'): ('p', '#a'),
        ('p', 'b', 'b'): ('q', ''),
        ('p', 'a', 'a'): ('q', ''),
        ('q', 'b', 'b'): ('q', ''),
        ('q', 'a', 'a'): ('q', ''),
        ('q', '', '#'): ('r', '#')
    }
    estado_inicial = {'p'}
    estado_aceptacion ={'r'}
    
    posicion = {
        "p": (1, 0),
        "q": (1, 1),
        "r": (2, 2)
    }
    
    automata = AutomataDePila(estados, alfabeto_entrada, alfabeto_pila, transiciones, estado_inicial, estado_aceptacion, posicion)
    return automata
    
    

    
iniciar()
    
    
    
