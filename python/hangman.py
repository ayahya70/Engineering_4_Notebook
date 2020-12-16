def clear_screen():
    print(chr(27) + "[2J")  # supposedly clears the screen


def print_hangman(errors=0):
    print("---┐")  # print the top

    hangman = ["   O", "   |", "  /|\\", "   |", "  / \\"]  # the different levels

    print("\n".join(hangman[:errors]))  # print up to the number of errors


MAX_MISTAKES = 5  # five lines, five mistakes

word = input("Type a word: ")  # get the word to guess
word_len = len(word)  # the length of the word
word_split = [char for char in word]  # split the word into individual charachters
guesses = ["_"] * word_len  # empty guess array with just underscores
mistakes = 0  # number of mistakes, start with zero

while guesses != word_split:  # loop until the guess matches the word
    clear_screen()  # clear the screen

    print("".join(guesses))  # turn the guesses array into a string to print
    print_hangman(mistakes)  # print the hangman for the number of mistakes

    guess = input("Guess: ")  # get the guess
    guess_split = [char for char in guess]  # split the guess into individual characters

    length = len(guess_split) if len(guess_split) < word_len else word_len  # get the shortest length to prevent errors

    is_mistake = True

    for i in range(length):  # loop over guess
        if word[i] == guess_split[i]:  # if a character matches, chage the underscore to the correct letter
            guesses[i] = word[i]
            is_mistake = False  # the user got a letter right


    if is_mistake:  # if there is a mistake, add a mistake to the mistakes variable
        mistakes += 1

    if mistakes >= MAX_MISTAKES:  # Too many mistakes!
        print(f"You lose idiot!! The word was {word}")
        quit()  # exit the program


print(f"You guessed the word: {word}")  # sucess is down here
