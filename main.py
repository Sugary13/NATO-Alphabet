import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ")

word_in_nato = [data_dict[letter.upper()] for letter in word]
print(word_in_nato)


