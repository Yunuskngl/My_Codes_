
def find_atoms(reactants):
    atoms = set()
    for a in reactants:
      for atom, _ in a :
        atoms.add(atom)
      
    return list(atoms)

def get_coeffs(atoms, side):
  return [get_atom_in_side(atom,side) for atom in atoms]
  
def get_atom_in_side(atom, side):
  return [get_num_atoms_in_compound(atom,compound) for compound in side] #liste yapııs oluşturur.

def get_num_atoms_in_compound(atom, compound):
  for a,count in compound:
    if a == atom:
      return count
  return 0

def negate_all_coefficients(coeffs):
  return [[-num for num in lst] for lst in coeffs]

import numpy as np

# Combine the reactant and product coefficients into
# a single list for each atom.
def construct_matrix(atoms, reactants, products):
  reactant_coeffs = get_coeffs(atoms, reactants)
  product_coeffs = negate_all_coefficients(get_coeffs(atoms, products))

  coeffs = []
  for x in range(len(atoms)):
    coeffs.append(reactant_coeffs[x] + product_coeffs[x])
  
  # Add a dummy equation to complete the system of equations.
  coeffs.append([1] + [0]*(len(coeffs[0])-1))
  return coeffs
  
from fractions import Fraction
# Solve the system of equations
def solve(coeffs):
  A = np.array(coeffs)
  b = np.array([0]*(len(coeffs)-1) + [1])
  solution = np.linalg.solve(A, b)
  solution= [Fraction(x).limit_denominator() for x in solution]

  # Scale the solutions so the coefficients are all integers
  x = max([x.denominator for x in solution])
  solution = [s * x for s in solution]
  return solution

SUBSCRIPTS = "₀₁₂₃₄₅₆₇₈₉"

def chemical(chem):
  z = ""
  for x in chem:
    y = x[0]
    if x[1] != 1:
      j = ""
      for c in str(x[1]):
        j += SUBSCRIPTS[int(c)]
      y += j
    z += y
  return z

def equation(reactants, products, sol=None):
  def strside(side, N=0):
    output = []
    for i, x in enumerate(side):
      term = chemical(x)
      if sol and int(sol[i + N]) > 1:
        term = str(int(sol[i + N])) + term
      output.append(term)
    return " + ".join(output)
  return strside(reactants) + " → " + strside(products, N=len(reactants))


def balance(reactants, products):
  solution = solve(construct_matrix(find_atoms(reactants), reactants, products))
  print("Unbalanced Equation:", equation(reactants, products))
  print("  Balanced Equation:", equation(reactants, products, solution))


# H₂ + O₂ → H₂O
reactants = [[("H", 2)], [("O", 2)]]
products =  [[("H", 2), ("O", 1)]]
balance(reactants, products)
print()

# C₃H₈ + O₂ → CO₂ + H₂O
reactants = [[("C", 3), ("H", 8)], [("O", 2)]]
products =  [[("C", 1), ("O", 2)], [("H", 2), ("O", 1)]]
balance(reactants, products)
