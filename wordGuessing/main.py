import random
import time
import os

easy_names = ["Ali", "Omid", "Sara", "Lina", "Nima", "Mina",
              "Amir", "Sina", "Yara", "Reza", "Zara", "Tara",
              "Hani", "Sami", "Roya", "Nazi"]

medium_names = ["Rahimi", "Akbari", "Hassani", "Rasouli", "Nazari", "Hashimi",
                "Karimi", "Qasimi", "Alizada", "Mohseni", "Ahmadi", "Jafari",
                "Mandegar", "Amiri", "Hussaini", "Rezaian"]

hard_names = ["Mohammadi", "Abdolrahim", "Ghaznavian", "Mostafavi",
              "Sadatkhani", "Abdulkarim", "Charkhgard", "Etemadian",
              "Darvishian", "Soleymani", "Farrokhzad", "Tavakkolian"]

HIGHSCORE_FILE = "highscore.txt"
HISTORY_FILE = "history.txt"

def load_high_score():
    if os.path.exists(HIGHSCORE_FILE):
        with open(HIGHSCORE_FILE, "r") as file:
            return int(file.read())
    return 0

def save_high_score(score):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))

def save_game_history(player, level, name, result, score, correct, wrong, duration):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"Player: {player}, Level: {level}, Name: {name}, Result: {result}, Score: {score}, Time: {round(duration,2)}s, Correct: {correct}, Wrong: {wrong}\n")

def show_game_history():
    if not os.path.exists(HISTORY_FILE):
        print(" No history found.")
        return
    print("\n Game History:")
    with open(HISTORY_FILE, "r") as file:
        print(file.read())

def draw_board(select_name, player_name, level_name):
    select_name = select_name.lower()
    guess_list = ['-' for _ in select_name]
    guess_count = len(select_name)
    guessed_chars = set()
    correct_char_list = []
    wrong_char_list = []
    score = 0
    start_time = time.time()

    print(f"\n {player_name}, let's start! Guess the name.")
    while guess_count > 0:
        print("Current word:", " ".join(guess_list))
        guess_char = input("Enter a character: ").lower()

        if not guess_char.isalpha() or len(guess_char) != 1:
            print(" Invalid input. Enter one alphabet letter.")
            continue

        if guess_char in guessed_chars:
            print(" You already guessed that character.")
            continue
        guessed_chars.add(guess_char)

        if guess_char in select_name:
            correct_char_list.append(guess_char)
            for i, char in enumerate(select_name):
                if char == guess_char:
                    guess_list[i] = guess_char
            score += 10
            print(" Correct guess!")

            if '-' not in guess_list:
                duration = time.time() - start_time
                print(f"\n You win, {player_name}! The name was: {select_name.capitalize()}")
                print(f" Your score: {score}")

                high_score = load_high_score()
                if score > high_score:
                    print(" New high score!")
                    save_high_score(score)
                else:
                    print(f" Current high score: {high_score}")

                save_game_history(player_name, level_name, select_name.capitalize(), "Win", score, correct_char_list, wrong_char_list, duration)
                break
        else:
            wrong_char_list.append(guess_char)
            guess_count -= 1
            print(f" Wrong! Remaining guesses: {guess_count}")

    else:
        duration = time.time() - start_time
        print(f"\n You lost, {player_name}. The correct name was: {select_name.capitalize()}")
        print(f" Your score: {score}")
        save_game_history(player_name, level_name, select_name.capitalize(), "Lose", score, correct_char_list, wrong_char_list, duration)

    print("\n Correct letters:", ", ".join(correct_char_list))
    print(" Incorrect letters:", ", ".join(wrong_char_list))

def easy(player):
    name = random.choice(easy_names)
    draw_board(name, player, "Easy")

def medium(player):
    name = random.choice(medium_names)
    draw_board(name, player, "Medium")

def hard(player):
    name = random.choice(hard_names)
    draw_board(name, player, "Hard")

def menu():
    player_name = input("Enter your name: ")
    while True:
        print("\n Choose a difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. View History")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            easy(player_name)
        elif choice == "2":
            medium(player_name)
        elif choice == "3":
            hard(player_name)
        elif choice == "4":
            show_game_history()
        elif choice == "5":
            print(f"Goodbye, {player_name} 👋")
            break
        else:
            print("Invalid choice. Try again.")

menu()