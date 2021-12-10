from json import load

with open("br_states.json", "r") as file:
    brazilian_states = load(file)
    
    for state in brazilian_states:
        print(state["nome"])