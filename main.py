from os import get_terminal_size
from json import loads
from sys import argv
from time import time_ns

class Transition:
    de : int
    ler : str
    para : int
    def __init__(self, transition_dict : dict) -> None:
        self.de = int(transition_dict["from"])
        if transition_dict["read"] == None or transition_dict["read"] == "None" or transition_dict["read"] == "null":
            self.ler = "None"
        else:
            self.ler = transition_dict["read"].lower()
        self.para = int(transition_dict["to"])

    def __str__(self) -> str:
        return f"de: {self.de}; ler: {self.ler}; para: {self.para}"

class Automata:
    initial: int
    final: list[int]
    transitions: list[Transition]
    transitions_dict : dict

    def __init__(self, automata_dict : dict) -> None:
        self.initial = automata_dict["initial"]
        self.final = automata_dict["final"]
        self.transitions = []
        for transition in automata_dict["transitions"]:
            self.transitions.append(Transition(transition))

    def __str__(self) -> str:
        transitions = ""
        for transition in self.transitions:
            transitions += transition.__str__() + "\n"
        return f"Inicial:{{{self.initial}}}, Finais: {{{self.final}}}, [\n{{{transitions}}}\n]"

    def compute_list(self, input : str) -> bool:
        current_nodes = [self.initial]
        for char in input:
            for node in current_nodes:
                tmp_list = []
                for transition in self.transitions:
                    if transition.de == node and (transition.ler == char or transition.ler == "None"):
                        tmp_list.append(transition.para)
            current_nodes = tmp_list.copy()
            if current_nodes == []:
                return False
            
        for final_node in current_nodes:
            if final_node in self.final:
                return True
        return False
    
    def convert_transitions_to_dict(self) -> None:
        transition_dict = {}
        for transition in self.transitions:
            key = f"{transition.de}{transition.ler}"
            if not key in transition_dict.keys():
                transition_dict[key] = [transition.para]
            else:
                para_list : list[int] =  transition_dict[key]
                para_list.append(transition.para)
                transition_dict[key] = para_list
        self.transitions_dict = transition_dict
    
    def compute_transitions_dict(self, input : str) -> bool:
        current_nodes = [self.initial]
        for char in input:
            tmp_list = []
            for node in current_nodes:
                try:
                    tmp_list.extend(self.transitions_dict[f"{node}{char}"])
                except:
                    pass
                try:
                    tmp_list.extend(self.transitions_dict[f"{node}None"])
                except:
                    pass
            current_nodes = tmp_list.copy()
            if current_nodes == []:
                return False
        
        for final_node in current_nodes:
            if final_node in self.final:
                return True

        return False
   
def get_input_list(input_list : list[str], separator : str = " "):
    input_list = input_list.strip().replace(";", " ").split("\n")
    input_lists = []
    for value in input_list:
        input_lists.append(value.split(separator))
    return input_lists

def main():
    if(len(argv) < 4):
        raise Exception("Menos de três argumentos")
    try:
        automata_file = open(argv[1])
        input_file = open(argv[2])
        output_file = open(argv[3], "w")
    except:
        raise FileNotFoundError()

    automata = Automata(loads(automata_file.read()))
    automata.convert_transitions_to_dict()
    input_list = get_input_list(input_file.read())
    terminal_width = get_terminal_size().columns
    print(("="*terminal_width))
    print("AUTOMATO".center(terminal_width))
    print(("="*terminal_width), end="\n\n")
    print(f"Inicial: {automata.initial}, Finais: {automata.final}, [".center(terminal_width))
    for transition in automata.transitions:
        print(f"{transition}".center(terminal_width))
    print("]".center(terminal_width-(len(transition.__str__())+1)), end="\n\n")
    print(("="*terminal_width), end="\n\n")
    print(("="*terminal_width))

    for input in input_list:
        start_time = time_ns()
        is_valid = automata.compute_transitions_dict(input[0])
        final_time = time_ns() - start_time
        output_file.write(f"{input[0]};{input[1]};{1 if is_valid else 0};{final_time}\n")
    print(f"Resultados salvos em: {argv[3]}")
    automata_file.close()
    input_file.close()
    output_file.close()

if __name__ == "__main__":
    main()