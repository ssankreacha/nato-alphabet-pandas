"""
List Comprehension
new_numbers = [new_item for item in list]
"""

import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data.to_dict()

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# Thomas = [Tango, Hotel, Oscar, Mike, Alpha, Sierra]
word = input("Enter a word: ").upper()
# List Comprehension
output_list = [phonetic_dict[letter] for letter in word]    # for each letter in word, gives value for key
print(output_list)

