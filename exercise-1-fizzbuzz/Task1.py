import sys

# Base task

for i in range(1, 101):
    line = ""
    if  i % 3 == 0:
        line += "Fizz"
    if i % 5 == 0:
        line += "Buzz"
    if line:
        print(line)
    else:
        print(i)



# Extension 1: add Fang and Bang

for i in range(1, 101):
    line = ""
    if  i % 3 == 0:
        line += "Fizz"
    if i % 5 == 0:
        line += "Buzz"
    if i % 7 == 0:
        line += "Fang"
    if i % 11 == 0:
        line += "Bang"
    if line:
        print(line)
    else:
        print(i)



# Extension 2: allow the user to define the factor and word,
# at the moment only 1 word

# %%writefile fizz_mod.py This line is to add if running 
# on Jupyter Notebooks


def fizz_buzz(dict, max):
    for i in range(1,max+1):
        line=""
        for key, value in dict.items():
            if i % key == 0:
                line += value
        if line:
            print(line)
        else:
            print(i)


def main(num, word, max):
    num = int(num)
    max = int(max)
    # Base game rules
    dictionary = {3: "Fizz", 5: "Buzz", 7: "Fang", 11: "Bang"}
    # Build dictionary item with the user input
    user_rule = {num: word}
    # Update the dictionary
    dictionary.update(user_rule)
    fizz_buzz(dictionary, max)

if __name__ == '__main__':
    """
    The user input are, in order
    num: the value for the new rule
    word: the corresponding new word for the value
    max  the maximum number for the itaration of the loop
    """
    num = sys.argv[1]
    word = sys.argv[2]
    max = sys.argv[3]
    main(num, word, max)


# Example of command line for input
# %run fizz_mod.py 13 casa 77
