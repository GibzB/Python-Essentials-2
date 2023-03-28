# Seed function
# The seed() function is used to initialize the random number generator.
# The seed() function is able to directly set the generator's seed.
from random import random, seed

seed(0)

for i in range(5):
    print(random())