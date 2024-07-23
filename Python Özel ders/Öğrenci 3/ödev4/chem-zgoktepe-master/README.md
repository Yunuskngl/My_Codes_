# Instructions  

In this assignment, you'll write a chemical equation balancer.  That is, given the first line below, you'll generate the second line below:

```
Unbalanced Equation: H₂ + O₂ → H₂O
  Balanced Equation: 2H₂ + O₂ → 2H₂O
```

## Chemical Format
The inputs to your program will look like the following:
```
reactants = [[("H", 2)], [("O", 2)]]
products =  [[("H", 2), ("O", 1)]]
```
The reactants above are H₂ and O₂, and the product is H₂O.
You will want to make sure you understand this format before continuing.

## Required Task 
Your job is to implement the following functions:

### Finding all the atoms on one side of the equation
First, you will implement `find_atoms(reactants)`.
This function returns a list of unique atoms in the provided reactants. For example, if the reactants are `[[("C", 3), ("H", 8)], [("O", 2)]]`, you
would return the list: `["C", "H", "O"]`.
That is, a list of all the atoms that appear in any
reactant.  Don't include duplicates though!

### Finding the number of each atom in each compound
Returns a list...of lists...of coefficients.
There should be one term for each atom in the
outer list.  And one term for each chemical
on the provided side of the equation in each
inner list.

Using the same input as above:
``` 
[[("C", 3), ("H", 8)], [("O", 2)]]
```

The output would be below:
```
C's      H's     O's
[[3, 0], [8, 0], [0, 2]]
  ^                  ^
  |                  |
  |                  There are 2 O's in O₂.
  There are 3 C's in C₃H₈.
```
That is, each outer list represents a particular atom.  Each inner list represents numbers for each compound.
So, `[3, 0]` is the carbons and indicates C₃H₈ has 3 carbons and O₂ has none.

This part is difficult; so, we've split it up into
three functions for you:
1. `get_num_atoms_in_compound(atom, compound)` -- Given a particular compound, determines the number of atoms of a particular type in that compound.  Conceptually, this function returns one of the single numbers in the output.
2. `get_atom_in_side(atom, side)` -- Given a side of the equation and a particular atom, returns a list of the number of that atom in each individual compound.
3. `get_coeffs(atoms, side)` -- Given a list of atoms and a side of the equation, returns a list of lists of numbers of atoms on that entire side of the equation, for each atom.

### Constructing a matrix of equations
1. `negate_all_coefficients(coeffs)` -- This function takes in the output from `get_coeffs` and negates every number in the list of lists.  It is useful to construct the final matrix because all the product coefficients need to be negated (since they're on the opposite side of the equation).

### Victory!
Once you've implemented these equations, your balancer should work!