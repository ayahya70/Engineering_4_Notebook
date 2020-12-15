sentence = input("Type a simple sentence: ")  # this is where you insret your senetence
split_sentence = sentence.split(" ")  # split sentences

for word in split_sentence:   # loops over words

    for character in word:  # loops over character
        print(character)
    print("-")

