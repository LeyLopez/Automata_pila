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
    alfabeto_entrada = {'a', 'b'}
    alfabeto_pila = {'a', 'b', '#'}
    
    transiciones = {
        ('p', 'a', ''): ('p', 'a#'),
        ('p', 'b', ''): ('p', 'b#'),
        ('p', '', '#'): ('q', ''),
        ('q', 'b', 'a'): ('q', ''),
        ('q', 'a', 'b'): ('q', ''),
        ('q', 'b', 'a'): ('q', ''),
        ('q', 'a', 'b'): ('q', ''),
        ('q', '', '#'): ('r', '#'),
        ('q', 'b', '#'): ('q', ''),
        ('q', 'a', '#'): ('q', ''),
        ('q', 'a', 'a'): ('q', ''),
        ('q', 'b', 'b'): ('q', ''),
        ('q', 'a', 'a'): ('q', ''),
        ('q', 'b', 'b'): ('q', ''),
    }
    
    estado_inicial = {'p'}
    estado_aceptacion = {'r'}
    
    posicion = {
    "p": (1, 0),
    "q": (1, 1),
    "r": (2, 2)
}

    
    
    automata = AutomataDePila(estados, alfabeto_entrada, alfabeto_pila, transiciones, estado_inicial, estado_aceptacion, posicion)
    return automata


iniciar()
