import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
code_on = True
while code_on:
    word = input("Enter a word: ").upper()
    try:    # try the code out
        output_list = [phonetic_dict[letter] for letter in word]    # for each letter in word, gives value for key
    except KeyError:    # then try the exception to the correct error (KeyError)
        print("Sorry, only letters in the alphabet please. ")
    else:
        print(output_list)
