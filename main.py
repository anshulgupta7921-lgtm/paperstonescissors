import random
from utils import *
from gamefxn import *
while True:
    print("\n===== STONE PAPER SCISSORS =====")
    print("1. Play Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        game()
    elif choice == "2":
        print("Final Score -> You:", your_score, "| My:", my_score)
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")