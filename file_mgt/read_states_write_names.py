from json import load

with open("br_states.json", "r") as file, open("state_names.txt", "w") as target:
    brazilian_states = load(file)
    
    for state in brazilian_states:
        target.write(state["nome"] + "\n")