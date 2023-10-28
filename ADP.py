from Pila import Stack 

class AutomataDePila:
    def __init__(self, status, input_alphabet, stack_alphabet, transitions, initial_status, acceptance_status):
        self.status = status
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.initial_status = initial_status
        self.acceptance_status = acceptance_status
        
    
    def process_chain(self, chain):
        stack = Stack()
        current_status = self.initial_status
        
        for simbol in chain:
            if(current_status, simbol, stack.top()) in self.transitions:
                new_status, simbols_to_stack = self.transitions[(current_status, simbol, stack.top())]
                current_status = new_status
                
                if simbols_to_stack != '':
                    for simbol_to_stack in simbols_to_stack[::-1]:
                        if simbol_to_stack != '':
                            stack.push(simbol_to_stack)
                        else:
                            stack.pop()
                        
            else:
                return False
        
        return current_status == self.acceptance_status
    
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