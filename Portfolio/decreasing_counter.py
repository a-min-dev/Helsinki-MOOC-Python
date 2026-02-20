"""
The program includes a class, DecreasingCounter, with
several methods.

The print_value method prints the value of the counter
in its current state.  The decrease method decreases
the value of the counter by 1, but the method also
ensures the counter will not go below 0.

The set_to_zero method sets the value of the counter to 0.
The reset_original_value method resets the value of 
the counter to its original value.
"""

class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.start_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.start_value

if __name__ == "__main__":
    # The initial value is 100
    counter = DecreasingCounter(100)
    # Decrease the value by 1 each time the decrease() method is called
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    # Reset the counter value to the original value, 100
    counter.reset_original_value()
    counter.print_value()