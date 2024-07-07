import random
from prettytable import PrettyTable

def write_names(filename):
    # Open the file and read all lines, stripping any extra whitespace
    with open(filename, "r") as file:
        names = [line.strip() for line in file]

    # Shuffle the list of names to ensure random pairing
    random.shuffle(names)
    
    # Create a PrettyTable object with the specified column names
    table = PrettyTable(["Number", "Name 1", "Name 2"])

    # Iterate over the list of names in steps of 2 to create pairs
    for i in range(0, len(names), 2):
        number = i // 2 + 1  # Calculate the pair number
        name1 = names[i]  # First name in the pair
        name2 = names[i + 1] if i + 1 < len(names) else ""  # Second name or empty if it doesn't exist
        
        # Add the pair to the table
        table.add_row([number, name1, name2])
        
        # Add a separator row for visual clarity
        table.add_row(["-", "-", "-"])

    # Print the table to the console
    print(table)

# Call the function with the filename
write_names("people.txt")
