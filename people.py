import random
from prettytable import PrettyTable

def write_names(filename):
    with open(filename, "r") as file:
        names = file.readlines()
    names = [name.strip() for name in names]
    random.shuffle(names)
    table = PrettyTable(["Number", "Name 1", "Name 2"])
    for i in range(0, len(names), 2):
        number = i // 2 + 1
        name1 = names[i]
        name2 = names[i + 1] if i + 1 < len(names) else ""
        table.add_row([number, name1, name2])
        table.add_row(["-", "-", "-"])
    print(table)

write_names("people.txt")
