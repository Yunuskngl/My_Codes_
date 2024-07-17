def get_runs(s):
    """
    A "run" in a sequence of digits is a substring of as many of the same digit in a row as possible.
    For example, "11141234" has three runs: "1", "22", and "333".

    This function should return a list of all the runs in the string `s` by using a similar algorithm
    to yesterday's class, where it keeps going until it finds a new number and processes the previous
    number at that point.

    Each run should be represented by a string xy where `x` is the length of the run and `y` is the
    number the run is made of.
    """
    runs = []
    prev = None
    if not s:
        return runs
    
    prev = s[0]
    count = 1
    
    for i in range(1,len(s)):
        if s[i] == prev:
            count +=1,
        else:
            bos = str(count) + prev
            runs.append(bos)
            prev = s[i]
            count = 1
        
    bos = str(count) + prev
    runs.append(bos)
    return runs

    
def look_and_say(n):
    """
    The look and say sequence is a sequence of strings with the first element "1".  To generate another 
    element of the sequence, the previous element is "read out loud" by counting the number of the
    same digit in a row.

    For example, if "121133111" were an element in the sequence, we would read off: "11 12 21 23 31" 
    resulting in the next element "1112212331".

    This function should return a list of the first `n` elements of the look and say sequence.
    """
    seq = ["1"]
    if n == 1:
        return seq

    for i in range(n-1):
        b = seq[-1]
    return seq


##### IGNORE EVERYTHING BELOW HERE #####

from checker import *
check(look_and_say)
