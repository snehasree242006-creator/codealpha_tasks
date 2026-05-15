import random

# Words with medium clues
word_data = {
    "python": "Used for coding and automation",
    "apple": "A fruit that is also a famous brand",
    "planet": "Earth is one of these",
    "school": "Students go here to study",
    "gaming": "Playing console or PC games"
}

# Randomly select word
word = random.choice(list(word_data.keys()))
clue = word_data[word]

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Hidden word
display = ["_"] * len(word)

print("🎮 Welcome to Hangman Game!")
print("Enter ONLY ONE LETTER at a time.")
print("You have 6 incorrect guesses.\n")

# Show clue
print("🔍 Clue:", clue, "\n")

# Game loop
while wrong_guesses < max_wrong and "_" in display:

    print("Word:", " ".join(display))
    print("Guessed Letters:", guessed_letters)
    print("Wrong Guesses Left:", max_wrong - wrong_guesses)

    # User input
    guess = input("Enter one letter: ").lower().strip()

    # Validate input
    if len(guess) != 1:
        print("❌ Enter ONLY ONE letter.\n")
        continue

    if not guess.isalpha():
        print("❌ Use alphabet letters only.\n")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("⚠️ Letter already guessed.\n")
        continue

    guessed_letters.append(guess)

    # Correct guess
    if guess in word:
        print("✅ Correct letter!\n")

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

    # Wrong guess
    else:
        wrong_guesses += 1
        print("❌ Wrong letter!\n")

# Game result
if "_" not in display:
    print("🏆 Congratulations! The word was:", word)
else:
    print("💀 Game Over! The word was:", word)g