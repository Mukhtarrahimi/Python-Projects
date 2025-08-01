import random

easy_names = [
    "Ali", "Omid", "Sara", "Lina", "Nima", "Mina",
    "Amir", "Sina", "Yara", "Reza", "Zara", "Tara",
    "Hani", "Sami", "Roya", "Nazi"
]

medium_names = [
    "Rahimi", "Akbari", "Hassani", "Rasouli", "Nazari", "Hashimi",
    "Karimi", "Qasimi", "Alizada", "Mohseni", "Ahmadi", "Jafari",
    "Mandegar", "Amiri", "Hussaini", "Rezaian"
]

hard_names = [
    "Mohammadi", "Abdolrahim", "Ghaznavian", "Mostafavi", 
    "Sadatkhani", "Abdulkarim", "Charkhgard", "Etemadian", 
    "Darvishian", "Soleymani", "Farrokhzad", "Tavakkolian"
]


def draw_board(select_name):
    select_name = select_name.lower()
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
            print("Invalid input. Enter one alphabet letter.")
            continue

        if guess_char in guessed_chars:
            print("You already guessed that character.")
            continue
        guessed_chars.add(guess_char)

        if guess_char in select_name:
            correct_char_list.append(guess_char)
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

    print("\nCorrect guesses:", ", ".join(correct_char_list))
    print("Incorrect guesses:", ", ".join(discorrect_char_list))


def easy():
    name = random.choice(easy_names)
    draw_board(name)


def medium():
    name = random.choice(medium_names)
    draw_board(name)


def hard():
    name = random.choice(hard_names)
    draw_board(name)


def menu():
    while True:
        print("\n🎯 Choose a difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            easy()
        elif choice == "2":
            medium()
        elif choice == "3":
            hard()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

# Start the game
menu()
