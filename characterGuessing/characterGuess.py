import random

names = ['Rahimi', 'Akbari', 'Amiri', 'Hussaini', 'Mohammadi', 'Ahmadi', 'Sultani']
select_name = random.choice(names).lower()
guess_list = ['-'] * len(select_name)
current_guess = " ".join(guess_list)
guess_count = len(select_name) + 3 
used_chars = []

print(" Welcome to the Guessing Game!")

while guess_count > 0:
    print("\n" + "-" * 30)
    print(f"Word: {current_guess}")
    print(f"Used letters: {' '.join(used_chars)}")
    print(f"Remaining guesses: {guess_count}")
    print("-" * 30)

    guess_char = input('Enter a character: ').lower()
    
    if not guess_char.isalpha() or len(guess_char) != 1:
        print("Please enter only a single alphabetic character.")
        continue

    if guess_char in used_chars:
        print(f"You already tried '{guess_char}'. Try a new one.")
        continue

    used_chars.append(guess_char)

    if guess_char in select_name:
        for i, char in enumerate(select_name):
            if char == guess_char:
                guess_list[i] = guess_char
        current_guess = " ".join(guess_list)
        print(f" Good job! -> {current_guess}")
        if '-' not in guess_list:
            print(" You win!")
            break
    else:
        guess_count -= 1
        print(f" Wrong! -> Remaining guesses: {guess_count}")

if '-' in guess_list:
    print(f"\n Game over! The word was: {select_name}")
