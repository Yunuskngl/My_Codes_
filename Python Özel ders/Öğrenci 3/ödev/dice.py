from collections import namedtuple, Counter
import random

from util import *

Side = namedtuple('Side', ['value', 'probability'])

# Checking Unfair or Invalid Dice

check_die([], False)
check_die([Side(value=1, probability=1/3)], False)
check_die([Side(value=1, probability=1.5)], False)
check_die([Side(value=1, probability=0.25), Side(value=2, probability=0.65)], False)
check_die([Side(value=1, probability=0.25), Side(value=1, probability=0.75)], False)
check_die([Side(value=1, probability=0.25), Side(value=2, probability=0.25), Side(value=1, probability=0.50)], False)
check_die([Side(value=1, probability=0.25), Side(value=2, probability=0.25), Side(value=3, probability=0.60)], False)
print("PASSED ALL INVALID DICE TESTS!")

# Making Fair Dice

def make_fair_die(n):
    """
    Returns a list of Sides which represents a die with *n* sides (1, 2, ..., n),
    each of which has probability 1/n of being rolled
    """
    sides = [Side(value=i+1, probability=1/n) for i in range(n)]
    return sides

for x in range(1, 21):
    check_die(make_fair_die(x), True)
print("PASSED ALL VALID DICE TESTS!")

# Rolling Dice

def roll_die(die):
    r = random.uniform(0, 1)
    total = 0
    # Missing code here!

def simulate_rolls(die, n):
    tally = Counter()
    for i in range(n):
        tally[roll_die(die)] += 1
    return tally

print(simulate_rolls(make_fair_die(2), 1000000))
