"""
This program focus on handling errors where a user
is asked to type in an integer between a lower bound
and an upper bound.
"""

def read_input(prompt: str, lower_limit: int, upper_limit: int)->int:
    while True:
        try:
            number = int(input(prompt))
            if lower_limit <= number <= upper_limit:
                print(f"You typed in: {number}")
                return number
        except ValueError:
            pass

        print(f"You must type in an integer between {lower_limit} and {upper_limit}")

        
def main():
    num = read_input("Please type in an integer: ", 0, 10)
    print(f"You typed in: {num}")

main()
