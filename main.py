import tkinter as tk
from Pila import Stack

class Automaton:
    def __init__(self):
        self.stack = Stack()
        self.states = {
            'q0': {'a': ('q1', 'pop_push'), 'b': ('q3', 'push')},
            'q1': {'a': ('q1', 'pop_push'), 'b': ('q2', 'pop')},
            'q2': {'a': ('q2', 'pop'), 'b': ('q2', 'pop')},
            'q3': {'a': ('q3', 'push'), 'b': ('q4', 'push')},
            'q4': {'a': ('q4', 'push'), 'b': ('q2', 'pop')}
        }
        self.current_state = 'q0'

    def reset(self):
        self.stack = Stack()
        self.current_state = 'q0'

    def process_input(self, input_str):
        self.reset()
        for symbol in input_str:
            if symbol in self.states[self.current_state]:
                next_state, action = self.states[self.current_state][symbol]
                if action == 'pop_push':
                    self.stack.pop()
                elif action == 'pop':
                    self.stack.pop()
                elif action == 'push':
                    self.stack.push(symbol)
                self.current_state = next_state
                yield (self.current_state, symbol)

    def is_valid(self):
        return self.current_state == 'q2' and self.stack.is_empty()

class PalindromeRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Palindrome Recognizer')
        self.root.geometry("600x400")
        
        self.label = tk.Label(root, text='Enter a string (abbbba format):')
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.check_button = tk.Button(root, text='Check', command=self.check_palindrome)
        self.check_button.pack()

        self.result_label = tk.Label(root, text='Result: ')
        self.result_label.pack()

        self.state_label = tk.Label(root, text='Current State: q0')
        self.state_label.pack()

        label_style = ("Helvetica", 14, "bold")  # Cambiar la fuente, el tamaño y la negrita

        self.label.config(fg="Purple", font=label_style)  # Cambiar el color y el estilo
        self.result_label.config(fg="Purple", font=label_style)  # Cambiar el color y el estilo
        self.state_label.config(fg="Purple", font=label_style)  # Cambiar el color y el estilo

    def check_palindrome(self):
        input_str = self.entry.get()
        automaton = Automaton()
        for state, symbol in automaton.process_input(input_str):
            self.state_label.config(text=f'Current State: {state} -> Next Symbol: {symbol}')
            self.root.update()
        
        if automaton.is_valid():
            self.result_label.config(text='Result: Valid Palindrome')
        else:
            self.result_label.config(text='Result: Not a valid palindrome')

if __name__ == '__main__':
    root = tk.Tk()
    app = PalindromeRecognizerApp(root)
    root.mainloop()
