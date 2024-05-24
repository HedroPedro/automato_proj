from json import loads
from sys import argv
from time import time, sleep

class Transition:
    de : int
    ler : str | None
    to : int

    def __init__(self, transition_dict : dict) -> None:
        self.de = int(transition_dict["from"])
        self.ler = transition_dict["read"]
        self.to = int(transition_dict["to"])
    
    def __str__(self) -> str:
        return f"from: {self.de}, read: '{self.ler}', to: {self.to}"

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
        return f"{{{self.initial}}}, {{{self.final}}}, {{{transitions}}}"

    def compute(self, input : str) -> bool:
        nodes_list = []

        sliced_input = input[1:]
        for transition in self.transitions:
            if self.initial == transition.de and (input[0] == transition.ler or transition.ler == "None"):
                nodes_list.append(transition.to)

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
                nodes_list.append(int(transition.to))

        if len(nodes_list) == 0:
            return False

        if len(nodes_list) == 1:
            return self.compute_determ(sliced_input, int(nodes_list[0]))
        

        return self.compute_underm(sliced_input, nodes_list)

    def compute_underm(self, input : str, current_nodes : list[int]) -> bool:
        sliced_input = input[1:]
        nodes_list = []
        bool_accumulator = 0 == 1
        for node in current_nodes:
            bool_accumulator = bool_accumulator or self.compute_determ(sliced_input, node)
        return bool_accumulator
     
def get_input_list(input_list : list[str], separator : str = " "):
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
input_list = get_input_list(input_file.read().strip().replace(";", " ").split("\n"))

for input in input_list:
    start_time = time()
    isValid = automata.compute(input[0])
    final_time = time() - start_time
    output_file.write(f"{input[0]};{input[1]};{1 if isValid else 0};{final_time}\n")

automata_file.close()
input_file.close()
output_file.close()