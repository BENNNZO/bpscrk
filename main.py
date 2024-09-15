import itertools

def main():
    words, leets, cases, max_combination_length, output_filename = ask_user()
    wordlist = gen_words(words, leets, cases, max_combination_length)
    print("Wordlist Count:", len(wordlist))
    output_file(output_filename, wordlist)

def output_file(filename, wordlist):
    with open(filename, "w") as f:
        f.write('\n'.join(wordlist))

def gen_words(words, leets, cases, max_combination_length):
    """
    Generate a wordlist based on the provided words and options.
    """
    print("Generating words with options:", {"leets": leets, "cases": cases})
    array_of_leet_combination_arrays = []
    for word in words:
        leet_combinations = generate_leet_combinations(word, leets=leets, cases=cases)
        array_of_leet_combination_arrays.append(leet_combinations)
    return combine_words(array_of_leet_combination_arrays, max_combination_length)

def generate_leet_combinations(word, leets=True, cases=True):
    """
    Generate all possible leet combinations of a word based on the provided options.
    """
    # Base mapping of characters to themselves
    base_mapping = {c: [c] for c in 'abcdefghijklmnopqrstuvwxyz'}

    # Include uppercase letters if cases is True
    if cases:
        for c in base_mapping.keys():
            base_mapping[c].append(c.upper())

    # Leet replacements (numbers and symbols)
    leet_mapping = {
        'a': ['@'],
        'b': ['8'],
        'e': ['3'],
        'g': ['6'],
        'i': ['1', '!', '|'],
        'l': ['1', '!', '|'],
        'o': ['0'],
        's': ['5', '$'],
        't': ['7'],
        'z': ['2'],
    }

    # Combine mappings based on options
    combined_mapping = base_mapping.copy()
    if leets:
        for c, replacements in leet_mapping.items():
            combined_mapping[c].extend(replacements)

    word = word.lower()
    char_options = []
    for c in word:
        options = set()
        if c in combined_mapping:
            options.update(combined_mapping[c])
        else:
            options.add(c)
            if cases and c.isalpha():
                options.add(c.upper())
        char_options.append(list(options))

    combinations = [''.join(chars) for chars in itertools.product(*char_options)]
    return combinations

def combine_words(word_lists, max_combination_length):
    """
    Combine words from subarrays up to the specified maximum combination length.
    """
    result = []
    num_subarrays = len(word_lists)
    max_length = min(max_combination_length, num_subarrays)
    for combination_length in range(1, max_length + 1):
        subarrays_combinations = itertools.combinations(range(num_subarrays), combination_length)
        for subarrays_indices in subarrays_combinations:
            selected_subarrays = [word_lists[i] for i in subarrays_indices]
            words_combinations = itertools.product(*selected_subarrays)
            for words_tuple in words_combinations:
                for permuted_words in itertools.permutations(words_tuple):
                    combined_word = ''.join(permuted_words)
                    result.append(combined_word)
    return result

def ask_user():
    """
    Prompt the user for input and return the collected parameters.
    """
    words_input = input("List words separated by spaces (e.g., benjamin 537 homebase): ").strip()
    words = words_input.split() if words_input else []
    leets = input("Do you want to add leets? (y/n) [y]: ").strip().lower() in ["y", "yes", ""]
    cases = input("Do you want to add cases? (y/n) [y]: ").strip().lower() in ["y", "yes", ""]
    output_filename = input("Name of output file (no spaces, include extension) [tmp.txt]: ").strip() or "tmp.txt"
    max_input = input("Max loop level of word combinations [2]: ").strip()
    max_combination_length = int(max_input) if max_input else 2

    # Print out user options
    print("--------- OPTIONS ---------")
    print("Word List:    ", words)
    print("Leets:        ", leets)
    print("Cases:        ", cases)
    print("Max:          ", max_combination_length)
    print("File Name:    ", output_filename)
    print("---------------------------")

    return (
        words,
        leets,
        cases,
        max_combination_length,
        output_filename,
    )

if __name__ == "__main__":
    main()