"""
The program utilizes a previously created function, line,
to output a spruce tree drawing by calling the spruce
function.

The spruce function handles centering each layer of the 
spruce tree.  The spruce function calls the line function
to handle printing each row of the spruce tree.
"""

def line(num, text):
    if text == "":
        text = "*"
    
    print(text[0]*num)

def spruce(size):
    width = size*2 - 1
    row_size = 1
    
    print("a spruce!")
    while row_size <= width:
        spaces = (width - row_size)//2
        print(" "*spaces, end = "")
        line(row_size, "*")
        row_size +=2

    trunk_spaces = (width - 1)//2
    print(" " * trunk_spaces + "*")

def main():
    spruce(7)

if __name__ == "__main__":
    main()