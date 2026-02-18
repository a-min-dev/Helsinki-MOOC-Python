"""
The following program creates a new class, Pet.  The class includes
a constructor, which takes the initial values of the attributes
name, species, and year_of_birth as its arguments.

A function, outside the class definition, is written to create and
return a new object of type Pet.
"""

# Define the class Pet
class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

# Function, new_pet, that creates and returns a new object of type Pet
def new_pet(name: str, species: str, year_of_birth: int):
    return Pet(name, species, year_of_birth)


if __name__ == "__main__":
    fluffy = new_pet("Fluffy", "dog", 2017)
    print(fluffy.name)
    print(fluffy.species)
    print(fluffy.year_of_birth) 