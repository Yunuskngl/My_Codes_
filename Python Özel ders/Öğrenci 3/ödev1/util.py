def list_has_duplicate(l):
    """Returns True exactly when `l` has at least one duplicate and False otherwise"""
    # Fill this in!!

def sides_are_not_duplicated(die):
    """
    Returns True when the provided `die` does not have any sides with the exact same value
    and False otherwise.

    Hint: You will want to use `list_has_duplicate` as a helper!
    """
    vals = []
    for x in die:
        vals.append(x.value)
    return not list_has_duplicate(vals)

def probabilities_add_to_1(die):
    """
    Returns True exactly when the probabilities of the sides that make up `die` 
    add up to "nearly" 1 and False otherwise.
    """
    total = 0
    # Fill in code here!
    return within(total, 1, 0.00001)

def is_valid_die(die):
    return sides_are_not_duplicated(die) and probabilities_add_to_1(die)

def within(x, y, delta):
    return abs(x - y) < delta


def check_die(die, outcome):
    if is_valid_die(die) != outcome:
        if outcome:
            print("Your code incorrectly claims", die, "is an INVALID die!")
        else:
            print("Your code incorrectly claims", die, "is a VALID die!")
        exit(1)
