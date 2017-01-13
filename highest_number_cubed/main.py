"""This is the entry point of the program."""


def highest_number_cubed(limit):
    for i in range(limit):
        if i**3 > limit:
            return (i-1)
            
print(highest_number_cubed(30))