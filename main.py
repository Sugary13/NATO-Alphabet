import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

while True:
    try:
        word = input("Enter a word: ")
        word_in_nato = [data_dict[letter.upper()] for letter in word]
        print(word_in_nato)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break
