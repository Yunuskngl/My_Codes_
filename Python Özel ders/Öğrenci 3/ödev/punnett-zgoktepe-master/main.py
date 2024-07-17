import random
import matplotlib.pyplot as plt
from collections import namedtuple

Creature = namedtuple("Creature", ["shape", "color"])

def choose_feature(pheno1, pheno2):
    """
    Given two phenotypes (strings of two letters),
    returns a new phenotype (a string of two letters
    where one comes from each of the original two, each
    with probability 1/2).
    """
    return ''.join(random.choice(letters) for letters in zip(pheno1, pheno2))

def cross(c1, c2):
    """
    Returns a new Creature that is a child of c1 and c2.
    """
    return Creature(
        shape = choose_feature(c1.shape, c2.shape),
        color = choose_feature(c1.color, c2.color)
    )

def is_green(creature):
    """
    Returns True if the creature's color phenotype is
    recessive (both genes are "a") and False otherwise.
    """
    return creature.color == "aa"

def is_wrinkled(creature):
    """
    Returns True if the creature's shape phenotype is
    recessive (both genes are "r") and False otherwise.
    """
    return creature.shape == "rr"

def percentage_green(population):
    """
    Returns the percentage of the population
    (which is a list of creatures) that are green.
    """
    green_count = sum(1 for creature in population if is_green(creature))
    return green_count / len(population) * 100

def percentage_wrinkled(population):
    """
    Returns the percentage of the population
    (which is a list of creatures) that are wrinkled.
    """
    wrinkled_count = sum(1 for creature in population if is_wrinkled(creature))
    return wrinkled_count / len(population) * 100

def percentage_green_and_wrinkled(population):
    """
    Returns the percentage of the population
    (which is a list of creatures) that are *both* green and wrinkled.
    """
    both_count = sum(1 for creature in population if is_green(creature) and is_wrinkled(creature))
    return both_count / len(population) * 100

def generation(population):
    """
    Returns a new generation (list) of Creatures by randomly
    choosing 50,000 pairs of parents from the population
    and crossing them into a child.
    """
    new_generation = []
    for _ in range(50000):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        child = cross(parent1, parent2)
        new_generation.append(child)
    return new_generation

# Initialize a population of creatures where nobody has
# *any* recessive genes.
population = []
for shape in ["Rr", "RR", "rR"]:
  for color in ["Aa", "AA", "aA"]:
    population.append(Creature(shape=shape, color=color))

# Do simulation
xs = []
green = []
wrinkled = []
both = []
for i in range(10):
  xs.append(i)
  green.append(percentage_green(population))
  wrinkled.append(percentage_wrinkled(population))
  both.append(percentage_green_and_wrinkled(population))
  population = generation(population)

# Plot the trends of green, wrinkled and both.
plt.plot(xs, green, 'g-')
plt.plot(xs, wrinkled, 'b--')
plt.plot(xs, both, "r--")
plt.savefig('out.png')
plt.show()
