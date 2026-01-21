"""
This program defines a function, chessboard, which accepts a single
parameter.

The function chessboard prints a chessboard shape of a given length
that is passed as the parameter.  Then, alternating rows of 0s and 1s
are printed up to the given number of rows passed by the call to the 
chessboard function.

For example, a call of chessboard(3) would print:
    101
    010
    101
"""

def chessboard(length):
    index = 0

    while index < length:
        if index % 2 == 0:
            row = "10" * length
        else:
            row = "01" * length

        print(row[0:length])

        index += 1

def main():
    chessboard(5)


# Testing the function
if __name__ == "__main__":
    main()