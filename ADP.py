from Pila import Stack 

class AutomataDePila:
    def __init__(self, status, input_alphabet, stack_alphabet, transitions, initial_status, acceptance_status, position):
        self.status = status
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.initial_status = initial_status
        self.acceptance_status = acceptance_status
        self.position = position
        
    
    def get_status(self):
        return self.status
    
    def get_input_alphabet(self):
        return self.input_alphabet
    
    def get_stack_alphabet(self):
        return self.stack_alphabet
    
    def get_transitions(self):
        return self.transitions
    
    def get_initial_status(self):
        return self.initial_status
    
    def get_acceptance_status(self):
        return self.acceptance_status
    
    
    def get_position(self):
        return self.position