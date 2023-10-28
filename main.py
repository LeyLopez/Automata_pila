from ADP import AutomataDePila

estados = {'p', 'q', 'r'}
alfabeto_entrada = {'a', 'b', ''}
alfabeto_pila = {'#', 'a', 'b'}
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
estado_inicial = 'p'
estado_aceptacion = 'r'

automata = AutomataDePila(estados, alfabeto_entrada, alfabeto_pila, transiciones, estado_inicial, estado_aceptacion)
cadena = 'aab'
resultado = automata.process_chain(cadena)
print("La cadena '{}' es aceptada: {}".format(cadena, resultado))