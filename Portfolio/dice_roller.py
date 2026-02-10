"""
The program is intended for use in games that may 
involve non-standard 6-sided dice.

The first function, roll, will roll the die
specified by the argument passed to the function.

The second function, play, will throw two dice
as many times as specified by the argument passed
to the funciton.  The function returns a tuple with
the number of times die 1 wins, the number of times
die 2 wins, and the number of ties.

"""

from random import choice

def roll(die: str):
    dice = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
    
    return choice(dice[die])

def play(die1: str, die2: str, times:int):
    die_1_wins = 0
    die_2_wins = 0
    tie_cases = 0

    for _ in range(times):
        result_1 = roll(die1)
        result_2 = roll(die2)
        
        if result_1 > result_2:
            die_1_wins += 1
        elif result_2 > result_1:
            die_2_wins += 1
        else:
            tie_cases += 1

    return (die_1_wins, die_2_wins, tie_cases)


# Test case with die A, die C, and 1000 rolls
if __name__ == "__main__":
    result = play("A", "C", 1000)
    print(result)
