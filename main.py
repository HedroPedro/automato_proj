from os import get_terminal_size
from json import loads
from sys import argv
from time import time

class Transition:
    de : int
    ler : str
    para : int
    def __init__(self, transition_dict : dict) -> None:
        self.de = int(transition_dict["from"])
        if transition_dict["read"] == None:
            self.ler = "None"
        else:
            self.ler = transition_dict["read"].lower()
        self.para = int(transition_dict["to"])
    def __str__(self) -> str:
        return f"from: {self.de}, read: '{self.ler}', to: {self.para}"

class Automata:
    initial: int
    final: list[int]
    transitions: list[Transition]

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
        return f"Inicial:{{{self.initial}}}, Finals: {{{self.final}}}, [\n{{{transitions}}}\n]"

    def compute(self, input : str) -> bool:
        nodes_list = []

        sliced_input = input[1:]
        for transition in self.transitions:
            if self.initial == transition.de and (input[0] == transition.ler or transition.ler == "None"):
                nodes_list.append(transition.para)

        if len(nodes_list) == 0:
            return False

        if len(nodes_list) == 1:
            return self.compute_determ(sliced_input, int(nodes_list[0]))
        return

    def compute_determ(self, input : str, current_node : int) -> bool:
        sliced_input = input[1:]
        nodes_list = []
        if input == "":
            return current_node in self.final
        
        for transition in self.transitions:
            if current_node == transition.de and (input[0] == transition.ler or transition.ler == "None"):
                nodes_list.append(int(transition.para))

        if len(nodes_list) == 0:
            return False

        if len(nodes_list) == 1:
            return self.compute_determ(sliced_input, int(nodes_list[0]))
        

        return self.compute_underm(sliced_input, nodes_list)

    def compute_underm(self, input : str, current_nodes : list[int]) -> bool:
        sliced_input = input[1:]
        bool_accumulator = 0 == 1
        for node in current_nodes:
            bool_accumulator = bool_accumulator or self.compute_determ(sliced_input, node)
        return bool_accumulator
    
    def convert_transitions_to_dict(self) -> dict:
        transition_dict = {}
        for transition in self.transitions:
            key = f"{transition.de}{transition.ler}"
            if not key in transition_dict.keys():
                transition_dict[key] = [transition.para]
            else:
                para_list : list[int] =  transition_dict[key]
                para_list.append(transition.para)
                transition_dict[key] = para_list
        return transition_dict
    

     
def get_input_list(input_list : list[str], separator : str = " "):
    input_list = input_list.strip().replace(";", " ").split("\n")
    input_lists = []
    for value in input_list:
        input_lists.append(value.split(separator))
    return input_lists

if(len(argv) < 4):
    raise Exception("Menos de três argumentos")

try:
    automata_file = open(argv[1])
    input_file = open(argv[2])
    output_file = open(argv[3], "w")
except:
    raise FileNotFoundError()

automata = Automata(loads(automata_file.read()))
input_list = get_input_list(input_file.read())
transitions_dict = automata.convert_transitions_to_dict()
print(transitions_dict)
terminal_width = get_terminal_size().columns
print(("="*terminal_width))
print("AUTOMATO".center(terminal_width))
print(("="*terminal_width), end="\n\n")
print(f"Initial: {automata.initial}, Final: {automata.final}, [".center(terminal_width))
for transition in automata.transitions:
    print(f"{transition}".center(terminal_width))
print("]".center(terminal_width-len(transition.__str__())), end="\n\n")
print(("="*terminal_width), end="\n\n")
print(("="*terminal_width))

for input in input_list:
    start_time = time()
    is_valid = automata.compute(input[0])
    final_time = time() - start_time
    output_file.write(f"{input[0]};{input[1]};{1 if is_valid else 0};{final_time}\n")

automata_file.close()
input_file.close()
output_file.close()