from json import loads
from sys import argv

def get_input_list(input_list : list[str], separator : str = " "):
    input_lists = []
    for value in input_list:
        input_lists.append(value.split(separator))
    return input_lists

def compute_automata(input_str : str, automata : list[dict]):
    accumulator = False
    for letter in input_str:
        accumulator = accumulator or isPathFinal(automata)
    return accumulator

def isPathFinal(currentNode):
    pass

if(len(argv) < 4):
    raise Exception("Menos de três argumentos")

try:
    automata_file = open(argv[1]).read()
    input_file = open(argv[2]).read()
    output_file = open(argv[3]).read()
except:
    raise FileNotFoundError()

automata_data = loads(automata_file)
automata_transition = automata_data["transitions"]
input_list = get_input_list(input_file.strip().replace(";", " ").split("\n"))

for input in input_list:
    real_value = compute_automata(input[0], automata_transition)