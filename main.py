import itertools


def main():
    wordlist = gen_words(*ask_user())
    print(len(wordlist))


def gen_words(words, leets, cases, symbl, max):
    print([words, leets, cases, symbl])

    array_of_leet_combination_arrays = []
    for word in words:
        array_of_leet_combination_arrays.append(generate_leet_combinations(word))

    return combine_words(array_of_leet_combination_arrays, max)


def generate_leet_combinations(word):
    leet_mapping = {
        'a': ['a', 'A', '@', '4'],
        'b': ['b', 'B', '8'],
        'c': ['c', 'C', '('],
        'd': ['d', 'D'],
        'e': ['e', 'E', '3'],
        'f': ['f', 'F'],
        'g': ['g', 'G', '9', '6'],
        'h': ['h', 'H'],
        'i': ['i', 'I', '1', '!'],
        'j': ['j', 'J'],
        'k': ['k', 'K'],
        'l': ['l', 'L', '1', '|'],
        'm': ['m', 'M'],
        'n': ['n', 'N'],
        'o': ['o', 'O', '0'],
        'p': ['p', 'P'],
        'q': ['q', 'Q'],
        'r': ['r', 'R'],
        's': ['s', 'S', '$', '5'],
        't': ['t', 'T', '7', '+'],
        'u': ['u', 'U', 'v'],
        'v': ['v', 'V', 'u'],
        'w': ['w', 'W', 'vv'],
        'x': ['x', 'X'],
        'y': ['y', 'Y'],
        'z': ['z', 'Z', '2'],
    }

    word = word.lower()
    char_options = []

    for c in word:
        options = set()
        options.add(c)

        if c.isalpha():
            options.add(c.upper())

        if c in leet_mapping:
            options.update(leet_mapping[c])

        char_options.append(list(options))

    combinations = [''.join(chars) for chars in itertools.product(*char_options)]
    return combinations



def combine_words(word_lists, max_combination_length):
    """
    Combine words from subarrays up to the specified maximum combination length.

    :param word_lists: List of subarrays, each containing words or their leet combinations.
    :param max_combination_length: Maximum number of words to combine.
    :return: List of all possible combined words.
    """
    result = []
    num_subarrays = len(word_lists)
    
    # Ensure the max_combination_length doesn't exceed the number of subarrays
    max_length = min(max_combination_length, num_subarrays)
    
    for combination_length in range(1, max_length + 1):
        # Generate all combinations of subarray indices of the current length
        subarrays_combinations = itertools.combinations(range(num_subarrays), combination_length)
        
        for subarrays_indices in subarrays_combinations:
            # Extract the subarrays corresponding to the current combination
            selected_subarrays = [word_lists[i] for i in subarrays_indices]
            # Generate all possible selections of words (Cartesian product)
            words_combinations = itertools.product(*selected_subarrays)
            
            for words_tuple in words_combinations:
                # Generate all permutations of the selected words
                for permuted_words in itertools.permutations(words_tuple):
                    # Concatenate the words and add to the result list
                    combined_word = ''.join(permuted_words)
                    result.append(combined_word)
    
    return result


def ask_user():
    # asking user for certain parameters | default is yes if it is a yes or no question.
    words = input("list words separated by spaces. (ex: benjamin 537 homebase)").split(" ")
    leets = input("Do you want to add leets? (y/n): ").strip().lower() in ["y", ""]
    cases = input("Do you want to add cases? (y/n): ").strip().lower() in ["y", ""]
    symbl = input("Do you want to add common numbers and symbols? (y/n): ").strip().lower() in ["y", ""]
    max   = input("Max loop level of word combinations: ")

    # Print out user options
    print("--------- OPTIONS ---------")
    print("Word List:    " + str(words))
    print("Leets:        " + str(leets))
    print("Cases:        " + str(cases))
    print("# + $:        " + str(symbl))
    print("Max:          " + str(2 if max == "" else max))
    print("---------------------------")

    return (words, leets, cases, symbl, 2 if max == "" else int(max))


if __name__ == "__main__":
    main()


# ask user for list of common words: name, birthday, etc
# ask user if they want leets
# ask user if they want cases
# ask user if they want to add common numbers and symbols
# ask user for small, medium, or large