import math

print(f"It's math! It has type {type(math)}")

print(dir(math))

print(f"pi to 4 significant digits = {math.pi:.6}")

print(math.log(32, 2))

# help(math)

import math as mt
print(mt.pi)

from math import log, pi
from numpy import asarray
print(pi, log(32, 2))

import numpy
print("numpy.random is a", type(numpy.random))
print("it contains names such as...",
      dir(numpy.random)[-15:]
     )

# Roll 10 dice
rolls = numpy.random.randint(low=1, high=6, size=10)
print(rolls)