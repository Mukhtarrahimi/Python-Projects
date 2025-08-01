import random

names = ["Rahimi", "Akbari", "Hussaini", "Mohammadi", "Ahmadi",
         "Mandegar", "Hassani", "Jafari", "Qasimi", "Alizada",
         "Amiri", "Nazari", "Rezaie", "Hashimi", "Rasuli", "Rahmani"]

select_name = random.choice(names).lower()
guess_list = ['-' for _ in select_name]
guess_count = len(select_name)
guessed_chars = set()
correct_char_list = []
discorrect_char_list = []

print("Guess the name!")

while guess_count > 0:
    print("Current word:", " ".join(guess_list))
    guess_char = input("Enter a character: ").lower()

    if not guess_char.isalpha() or len(guess_char) != 1:
        correct_char_list.append(guess_char)
        print("Invalid input. Enter one alphabet letter.")
        continue

    if guess_char in guessed_chars:
        print("You already guessed that character.")
        continue
    guessed_chars.add(guess_char)

    if guess_char in select_name:
        for i, char in enumerate(select_name):
            if char == guess_char:
                guess_list[i] = guess_char
        print("Correct guess!")

        if '-' not in guess_list:
            print("You win! The name was:", select_name.capitalize())
            break
    else:
        discorrect_char_list.append(guess_char)
        guess_count -= 1
        print(f"Wrong! Remaining guesses: {guess_count}")

else:
    print("You lost! The correct name was:", select_name.capitalize())

print(f'correct list of character you enter: {correct_char_list}')
print(f'discorrect list of character you enter: {discorrect_char_list}')

def menu():
    print("Choose an degree option:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Quit")
    chose = input("Enter your choice: ")
    if chose == "1":
        easy()
    elif chose == "2":
        medium()
    elif chose == "3":
        hard()
    else:
        print("Goodbye!")
