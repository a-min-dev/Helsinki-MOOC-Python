"""
The following program is an implementation of a programming language executor.  The program
consists of rows, and each row is in the format as follows:
    PRINT [value]: store value in a list to be printed
    MOV [variable] [value] : assign a value to a variable
    ADD [variable] [value] : add value to the value assigned to the variable
    SUB [variable] [value] : subtract value from value assigned to the variable
    MUL [variable] [value] : multiple value by value assigned to the variable
    [location]: : names a line of code, where it can be jumped to from elsewhere in program
    JUMP [location] : jumps to specified location
    IF [condition] JUMP [location] : if condition is True, jump to specified location
    END: finish execution of the program

    [value] can be a value stored in a variable or an integer number typed in directly
"""

import string

def run(program):

    #Initialize a dictionary with 26 variables, A-Z as keys, with initial values of 0
    variable_dict = {letter: 0 for letter in string.ascii_uppercase}

    #Initialize a labels dictionary, for locations, or a name for a line of code
    labels = {}
    #List to return printed values
    output = []

    #First pass through program: find all labels/location; a line with a colon, :, is a definition of a location
    for i in range(len(program)):
        line = program[i].strip()
        #Strip the line to get the name of the label/location only
        if line.endswith(":"):
            label_name = line[:-1]
            #The cleaned-up label/location name is the Key in the labels dictionary, and line number is Value
            labels[label_name] = i


    #A helper function to determine if [value] is a value stored in a variable or integer typed directly
    def get_val(token):
        if token in variable_dict:
            return variable_dict[token]
        return int(token)

    #Second pass through program:  execution loop
    pointer = 0

    while pointer < len(program):
        line = program[pointer].strip()

        #Skip the label/locations definitions during this pass through program
        if line.endswith(":") or not line:
            pointer += 1
            continue

        parts = line.split()
        cmd = parts[0]

        #Handle the logic for each command
        if cmd == "PRINT":
            output.append(get_val(parts[1]))

        elif cmd == "MOV":
            variable_dict[parts[1]] = get_val(parts[2])

        elif cmd == "ADD":
            variable_dict[parts[1]] += get_val(parts[2])

        elif cmd == "SUB":
            variable_dict[parts[1]] -= get_val(parts[2])

        elif cmd == "MUL":
            variable_dict[parts[1]] *= get_val(parts[2])

        elif cmd == "JUMP":
            #Jump directly to line
            pointer = labels[parts[1]]
            continue

        #IF:  if a condition is True, jump to the specified location
        elif cmd == "IF":
            v1 = get_val(parts[1])
            op = parts[2]
            v2 = get_val(parts[3])
            target_location = parts[5]

            #Comparison logic
            condition = False
            if op == "==": condition = (v1 == v2)
            elif op == "!=": condition = (v1 != v2)
            elif op == "<": condition = (v1 < v2)
            elif op == ">": condition = (v1 > v2)
            elif op == "<=": condition = (v1 <= v2)
            elif op == ">=": condition = (v1 >= v2)

            if condition:
                pointer = labels[target_location]
                continue
        
        elif cmd == "END":
            break

        pointer += 1

    return output


#Example:  find the first 10 factorials
program = []
program.append("MOV A 1")
program.append("MOV B 1")
program.append("begin:")
program.append("PRINT A")
program.append("ADD B 1")
program.append("MUL A B")
program.append("IF B <= 10 JUMP begin")
program.append("END")
result = run(program)
print(result)