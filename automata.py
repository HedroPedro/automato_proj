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