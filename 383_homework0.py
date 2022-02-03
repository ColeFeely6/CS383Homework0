# Cole Feely
# Starting 2/1/22
# Due 2/4/22

# COMPSCI 383 Homework 0
#
# Fill in the missing bodies of the functions as specified by the comments and docstrings.
#
# If you execute this file, the main() function below will test your implementations.  You can 
# compare your results to the answers in the comments.
#

## TODO Make a readme 
# Exercise 1 (6 points)
def max_unique(lst):
    """Returns the largest element of a list that appears only once"""
    # print("1.", max_unique([9, 0, 1, 2, 5, 8, 6, 7, 5, 3, 0, 9])) and returns 1. 8
    #
    # This returns the largest number that does not repeat
    #
    # so in order to do this, I need to iterate through the list and somehow store each one we have seen. Possibly two loops then. Look at i in lst,
    # see if it is in the frontier list. If it is not, check if that is greater than the max_return. If it is, set that as the new one. 
    # Then add it to the frontier list, no matter if it passed that test or not. 


    # if counter is x length
            #   if return_max is less than this
            #       set our new return max
            #   reset counter
            #add i to frontier

    unique_list = []
    is_unique = True

    for i in range(len(lst)):
        # corner case: if the start of the loop
        if len(unique_list) == 0:
            unique_list.append(lst[i])
        else:
            for j in range(len(unique_list)): # search through the frontier list
                if lst[i] == unique_list[j]: # Find a match: if this number in lst is seen in frontier list
                    is_unique = False # That number is not unique
            # My issue is that I need to remove the previous big one if it is found
            if not is_unique:
                unique_list.remove(int(lst[i]))
            else:
                unique_list.append(lst[i])
            is_unique = True

    return max(unique_list)



# Exercise 2 (6 points)
def splice_em(list_one, list_two):
    """Splice two equal-length lists together.
    
    Returns a list with alternating elements from the two lists given as arguments.  For example:
    splice_em(['a', 'b', 'c'], [1, 2, 3]) should return the list ['a', 1, 'b', 2, 'c', 3]
    
    Hint: you'll probably want to use a for or while loop to iterate.  The enumerate() and/or zip() 
    built-in functions might be helpful here: https://docs.python.org/3/library/functions.html    
    """

    # Here I did not go with the given hints because I thought the tuples from the zip() were a bit too complicated
    # I thought I could easily combine the two if they are the same length with one for loop
    return_list = [] # the list that we are returning

    # Check to see if they are the same length
    if len(list_one) != len(list_two):
        ValueError("Arrays must have the same size")
    else:
        for i in range(len(list_one)):
            return_list.append(list_one[i])
            return_list.append(list_two[i])

    return return_list  # fix this line!


# Exercise 3 (8 points)
def reverse_dict_list(d):
    """Reverse a dictionary that maps keys to lists of values.
    
    Given a dictionary that maps each key k1, k2, etc. to a list of values v1, v2, ..., create a 
    new dictionary keys by v1, v2, mapping them to lists k1, k2, etc.

    For example, reverse_dict_list({'a':[1, 2, 3], 'b':[1, 3, 5, 7], 'c':[4, 5, 6]}) should return 
    the dictionary {1:['a', 'b'], 2:['a'], 3:['a', 'b'], 5:['b', 'c'], 7:['b'], 4:['c'], 6:['c']}

    # There are ways in python to get the key and values of a dictionary
    # So I should look these up, it may need some for loops
    """
    #print("3.", reverse_dict_list({1: ['h', 'e', 'y'], 2: ['h', 'o']}))  # {'h': [1, 2], 'e': [1], 'y': [1], 'o': [2]}
    new_dict = {}
    old_keys = []
    old_vals = []

    '''print("Dict key-value are : ")
    for key, value in d.items():
        old_keys.append(key)
        old_vals.append(value)
    for i in old_keys:
        #this doesn't work because they are of different lengths
        new_dict.update({old_keys[i]:old_vals[i]})'''


    #
    # fill in function body here
    #
    return new_dict  # fix this line!


# Exercise 4 (8 points)
def char_counts(some_text):
    """Return a dictionary containing each character in the text as keys, and the number of times
    they occur as values.

    Hint: recall that since a string is a sequence, you can loop through it as you would a list.
    For help with dictionaries, see the Python docs: 
    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

    """
    #TODO my unique list function is messed up, I need to fix it. Look at problem 1 maybe

    # 1. Get unique list
    # 2. Create a counting list
    # 3. Sift through the given string and count the number of times that letter is seen
    # 4. Init a dict
    # 5. Loop through unique list and counting list to build the new dictionanry

    unique_list1 = []
    is_unique1 = True

    for i in some_text:
        # corner case: if the start of the loop
        if len(unique_list1) == 0:
            unique_list1.append(i)
        else:
            for j in range(len(unique_list1)): # search through the frontier list
                if i == unique_list1[j]: # Find a match: if this number in lst is seen in frontier list
                    is_unique1 = False # That number is not unique
            # My issue is that I need to remove the previous big one if it is found
            if  is_unique1:
                unique_list1.append(i)
            is_unique1 = True


    count_list1 = [0] * len(unique_list1)


    for i in some_text:
        for j in range(len(unique_list1)):
            if i == unique_list1[j]:
                count_list1[j] += 1
    print('unique_list: ',unique_list1)
    print('count_list: ', count_list1)

    dict = {}
    for i in range(len(unique_list1)):
        dict.update({unique_list1[i]:count_list1[i]})
    return dict  # fix this line!


# Exercise 5 (10 points)
def rewrap(txt, c):
    """Wrap a string to a specified number of characters per line.

    Given a text string, eliminate any newline characters an insert new ones such that no word is 
    broken up and no line is longer than c characters (unless it consists of word whose length is
    greater than c).  Any number of whitespace characters in the input should be condensed into a
    single space.  Punctuation should be treated as a normal character, and not separated from
    words.

    For example, if s="Experience is simply the name we give our mistakes.", rewrap(s, 30) yields:
        Experience is simply the name
        we give our mistakes.

    While rewrap(s, 10) gives: 
        Experience
        is simply
        the name
        we give
        our
        mistakes.
    """
    #
    # fill in function body here
    #
    return ""  # fix this line!


# Exercise 6 (10 points)
def is_monotonicish(lst):
    """Return True if list of numbers is "mostly monotonic", False otherwise.

    In "mostly increasing" lists of numbers, the difference between each entry and the one before
    it is no less than -1.  That is, [1, 3, 5, 7] and [1, 3, 2, 3] are "mostly increasing", while
    [1, 3, 1, 5] is not.  A "mostly decreasing" list is defined simlarly, with each successive 
    being no more than one greater than the preceeding.  A "mostly monotonic" sequence of numbers
    is either mostly increasing or mostly decreasing. 
    """
    #
    # fill in function body here
    #
    return True  # fix this line!


# Exercise 7 (2 points +10 extra credit)
def moxie_combos(n):
    """Return a list of tuples describing all possible ways to deliver the world's best soda.

    Moxie can be packaged in single cans, six-packs of cans, or cases of 24 cans.  For example, 
    42 Moxies could be delivered in 1 case, 1 six-pack, and twelve singles, or 1 case, 3 six-packs,
    and 0 singles, or 0 cases, 2 six-packs, and 30 singles, etc.  

    For a given n, moxie_combos(n) returns a list of tuples that describe all possible ways to 
    group n cans into cases, six-packs, and singles.  It returns a list of unique three-element 
    tuples, each describing the number of cases, six-packs, and singles in that particular 
    combination.  For example, moxie_combos(19) should return the list:
    [ (0, 0, 19), (0, 3, 1), (0, 2, 7), (0, 1, 13) ]

    (Note that the order of the list does not matter.)

    Hint: you may want to consider a recursive solution --- given a valid solution for n-1, how
    can you create the solution for n?  
    """
    #
    # fill in function body here
    #
    return [(0, 0, 0)]  # fix this line!


# The main() function below will be executed when your program is run.  Note that Python does not 
# require a main() function, but it is considered good style.  The comments on each line show
# what should be printed if your code is running correctly.
def main():
    print("1.", max_unique([9, 0, 1, 2, 5, 8, 6, 7, 5, 3, 0, 9]))      # 8
    print("2.", splice_em(['r', 'd', 'c', 'p'], [2, 2, 3, 0]))         # ['r', 2, 'd', 2, 'c', 3, 'p', 0]
    print("3.", reverse_dict_list({1:['h', 'e', 'y'], 2:['h', 'o']}))  # {'h': [1, 2], 'e': [1], 'y': [1], 'o': [2]}
    print("4.", char_counts("wowie zowie"))                            # {'w': 3, 'o': 2, 'i': 2, 'e': 2, ' ': 1, 'z': 1}
    print("5.", rewrap("I love writing Python code.", 6))              # "I love\nwriting\nPython\ncode." 
    print("6.", is_monotonicish([3, 5, 10, 9, 13]))                    # True
    print("7.", moxie_combos(13))                                      # [(0, 0, 13), (0, 1, 7), (0, 2, 1)]


###################################

# The lines below are a common Python idiom for creating Python programs that can be exectuted
# directly or used as a module.  For more info, see: 
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == '__main__':
    main()
