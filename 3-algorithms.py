# Justin Caringal
# 
# A script to generate all of the permutations
# of inputted character strings.
#
# Prompt provided by Service Metal Products

import os
import argparse

def swap(array : list, first_index : int, second_index : int) -> None:
    """Given an input array, swap the values at the given indices.

    Affects inputted array. If either inputted index is out of bounds,
    notifies user and does not perform swap.
    
    Args:
        array (list): The inputted array.
        first_index (int): Index of the first value to be swapped.
        second_index (int): Index of the second value to be swapped.
    
    Returns:
        None
    """

    # checks indices to prevent IndexError out of range
    if (first_index >= len(array)) or (second_index >= len(array)):
        print("Given index out of bounds.")
        return

    # performs swap on inputted list
    array[first_index], array[second_index] = \
        array[second_index], array[first_index]
    return


def generate_permutations(char_list : list,
                          left_index : int,
                          right_index : int,
                          permutations : list) -> None:
    """A recursive function which finds all possible permutations
    through a backtracking tree-like algorithm.

    Args:
        char_list (list): The string on which to find all permutations,
            converted into list form for easier processing.
        left_index (int): The left bound of the affected area of the list.
        right_index (int): The right bound of the affected area of the list.
        permutations (list): The output list containing all discovered
            permutations.
        
    Returns:
        None (permutations parameter contains output)
    """


    # base case: new permutation found
    if left_index == right_index:
        permutation = ''.join(char_list) # converts from list to str
        if permutation not in permutations: # ensures only unique added
            permutations.append(permutation)
        return permutations

    for index, _ in enumerate(char_list):
        swap(char_list, left_index, index) # swap current char with next
        generate_permutations(char_list,
                                left_index + 1,
                                right_index,
                                permutations) # adds call to stack
        swap(char_list, left_index, index) # backtracks swap


def permutations_driver(original_string : str) -> list:
    """A driver function to find all permutations of a given string.

    Args:
        original_string (str): The seed string to generate permutations.
    
    Returns:
        list: Returns sorted list of all permutations given an input string.
    """
    char_list = list(original_string)
    starting_left_index = 0
    starting_right_index = len(char_list) - 1
    permutations = []
    generate_permutations(char_list,
                          starting_left_index,
                          starting_right_index,
                          permutations)
    permutations.sort()
    return permutations


def read_file(filename : str) -> list:
    """Reads input file and returns list of lines.
    
    Args:
        filename (str): Path to input file.
    
    Returns:
        list: Returns list of lines to process if valid path,
            returns empty list otherwise.
    """
    if not os.path.exists(filename):
        print(f'\"{filename}\" does not exist.')
        return []

    with open(filename, 'r') as file:
        # list comprehension cleans whitespace
        lines = [line.strip() for line in file.readlines()]
    return lines


def main() -> None:
    """The main program."""

    # prompts user, accesses input file
    input_path = args.filename
    if not input_path: # checks command line input, otherwise prompts user
        welcome_txt = 'No command-line input detected,' \
            ' input a path to the input file: '
        input_path = input(welcome_txt)
    string_seeds = read_file(input_path)
    while not string_seeds: # seeks out valid filepath
        input_path = input('Invalid path, please try again: ')
        string_seeds = read_file(input_path)

    # performs permutation generation on each line
    for seed in string_seeds:
        permutations = permutations_driver(seed)
        permutation_str = ','.join(permutations)
        print(permutation_str)
    

if __name__ == "__main__":
    description = 'A script to generate all permutations of each' \
        'line of an input file.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('filename',
                        type=str,
                        nargs='?',
                        help='Path to input file.')
    args = parser.parse_args()
    main()