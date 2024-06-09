from os import get_terminal_size
from json import loads
from sys import argv
from time import time_ns
from automata import Automata

def get_input_list(input_list : list[str], separator : str = ";"):
    input_list = input_list.strip().replace(separator, " ").split("\n")
    input_lists = []
    for value in input_list:
        input_lists.append(value.split(" "))
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
        print(f"{transition}".center(terminal_width-1))
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