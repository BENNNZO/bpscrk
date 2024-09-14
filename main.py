def main():
    options = ask_user()

def ask_user():
    # asking user for certain parameters | default is yes if it is a yes or no question.
    words = input("list words separated by spaces. (ex: benjamin 537 homebase)").split(" ")
    leets = True if input("Do you want to add leets? (y/n): ") in ["y", ""] else False
    cases = True if input("Do you want to add cases? (y/n): ") in ["y", ""] else False
    symbl = True if input("Do you want to add common numbers and symbols? (y/n): ") in ["y", ""] else False

    print(" -------- OPTIONS -------- ")
    print("Word List:    " + str(words))
    print("Leets:        " + str(leets))
    print("Cases:        " + str(cases))
    print("# + $:        " + str(symbl))
    print(" ------------------------- ")

    return { "words": words, "leets": leets, "cases": cases, "commons_digits_and_symbols": symbl }

if __name__ == "__main__":
    main()




# ask user for list of common words: name, birthday, etc
# ask user if they want leets
# ask user if they want cases
# ask user if they want to add common numbers and symbols
# ask user for small, medium, or large