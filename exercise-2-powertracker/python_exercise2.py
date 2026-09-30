import numpy as np
from numpy import random

# Base task

import numpy as np
from numpy import random

small = 10000
large = 1
old = 21
i = 0

while True:
    num = random.randint(1,21)
    exp = random.randint(2,4)
    new = num**exp
    i += 1
    if new < small:
        small = new
    if new > large:
        large = new
    if new % old == 0:
        break
    else:
        old = new

print(f"The largest result is {large}")
print(f"The smallest result is {small}")
print(f"{new} is divisible by {old}")
print(f"We completed {i} loops")



# Extention: exclude 1 from the break of the loop

small = 10000
large = 0
old = 21
i = 0

while True:
    num = random.randint(1,21)
    exp = random.randint(2,4)
    new = num**exp
    i += 1
    if new < small:
        small = new
    if new > large:
        large = new
    if new % old == 0:
        break
    if new > 1:
        old = new

print(f"The largest result is {large}")
print(f"The smallest result is {small}")
print(f"{new} is divisible by {old}")
print(f"We completed {i} loops")