sentence = input("Type a simple sentence: ")
split_sentence = sentence.split(" ")

for word in split_sentence:

    for character in word:
        print(character)
    print("-")

