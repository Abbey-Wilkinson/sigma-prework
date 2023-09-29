import random

with open('secret_word_list.txt', 'r') as secret_word_list:
    secret_words = secret_word_list.readlines()[:-1]


def generate_secret_word(secret_words):
    return random.choice(secret_words)


guesses_taken = 0
guesses_allowed = len(generate_secret_word(secret_words)) + 5
guesses = []
done = False

while not done:
    for letter in generate_secret_word(secret_words):
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    print(
        "You have made {guesses_taken} guesses. You have {guesses_allowed} guesses left.")
    guess = input('What is your next guess? Input letter here: ')

    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        guesses_taken += 1
        guesses_allowed -= 1
        if guesses_allowed == 0:
            print(
                f"You ran out of guesses! The secret word was {generate_secret_word(secret_words)}")
            break

done = True
for letter in generate_secret_word(secret_words):
    if letter.lower() not in guesses:
        done = False
