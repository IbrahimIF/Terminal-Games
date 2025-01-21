import curses
import locale
import subprocess
import os
import sys
import random

# Setup Unicode support for emojis
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")


# Define the main game function
def main(win):
    # Setup curses
    curses.curs_set(0)  # Hide cursor
    win.keypad(1)  # Enable special keys
    curses.noecho()  # Don't display user input
    win.nodelay(0)  # Wait for user input
    win.clear()

    # Define constants and variables
    arrow = "→"
    options = ["Rock 🧱", "Paper 📃", "Scissors ✂️"]
    ESC = 27
    ENTER = 10
    score = 0
    key = None
    current_option = 0  # Index for current option

    while True:
        # Clear the screen and display the main menu
        win.clear()
        win.border(0)
        win.addstr(0, 2, f"Rock Paper Scissors Terminal Game!")
        win.addstr(2, 2, f"Score: {score}")
        win.addstr(3, 2, "Use UP/DOWN arrows to choose, ENTER to play, ESC to quit.")

        # Display the options with the arrow
        for idx, option in enumerate(options):
            if idx == current_option:
                win.addstr(5 + idx, 4, f"{arrow} {option}")
            else:
                win.addstr(5 + idx, 6, option)

        # Refresh the screen
        win.refresh()

        # Get user input
        key = win.getch()

        # Navigate through options
        if key == ord('w') and current_option > 0:
            current_option -= 1
        elif key == ord('s') and current_option < len(options) - 1:
            current_option += 1
        elif key == ENTER:
            # Play the game
            win.clear()
            win.border(0)
            user_choice = options[current_option].lower()  # Get user choice
            computer_choice = random.choice(["rock 🧱", "paper 📃", "scissors ✂️"])  # Random computer choice
            win.addstr(2, 2, f"You chose: {user_choice.capitalize()}")
            win.addstr(3, 2, f"Computer chose: {computer_choice.capitalize()}")

            # Determine the result
            if user_choice == computer_choice:
                result = "It's a tie!"
            elif (user_choice == "rock 🧱" and computer_choice == "scissors ✂️") or \
                 (user_choice == "paper 📃" and computer_choice == "rock 🧱") or \
                 (user_choice == "scissors ✂️" and computer_choice == "paper 📃"):
                result = "You win!"
                score += 1
            else:
                result = "You lose."

            win.addstr(5, 2, result)
            win.addstr(7, 2, "Press any key to return to the menu.")
            win.refresh()
            win.getch()  # Wait for the user to acknowledge
        elif key == ESC:
            break  # Exit the game

    curses.endwin()  # End curses mode

# Run the game
curses.wrapper(main)