
import sys # used to allow usage of emojis in the terminal by changing the type of terminal
sys.stdout.reconfigure(encoding='utf-8')
import emoji # import emoji module
import random


# testing of rock paper scissors emoji in the terminal
print(emoji.emojize("📃"))
print(emoji.emojize("🧱"))
print(emoji.emojize("✂️"))

top_border = [




]


middle_boarder = [



]


bottom_boarder = [


]

user_choice =  input("Choose either Rock Paper Scissors:") 

print(user_choice)

border = [
    
    ["+","---------------------------------------------------------","+"],
    ["|","------","Welcome to Rock Paper Scissors Terminal Game","-----","|"],
    ["|","You will be versing a randomiser choose the options below","|"],
    ["|","                                                         ","|"],
    ["|",       f"{user_choice:<55}"        ,"|"],
    ["|","None","None","None","None","None","None","|"],
    ["|","None","None","None","None","None","None","|"],
    ["|","None","None","None","None","None","None","|"],
    ["|","None","None","None","None","None","None","|"],
    ["+","---------------------------------------------------------","+"],
    ]

for row in border:
    print(" ".join(row))




# second version 


import curses
from curses import wrapper

def main(stdscr):
    # Initialize the screen
    curses.curs_set(0)
    stdscr.clear()
    
    # Set up options and initial index
    options = ["Rock", "Paper", "Scissors"]
    current_option = 0
    
    # Game title box
    stdscr.addstr(1, 2, "Welcome to Rock Paper Scissors Terminal Game")
    stdscr.addstr(2, 2, "Use arrow keys to choose an option and press Enter")

    while True:
        # Render options
        for idx, option in enumerate(options):
            x = 10
            y = 5 + idx
            if idx == current_option:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, option)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, option)
        
        # Get user input
        key = stdscr.getch()
        
        # Navigate options with arrow keys
        if key == curses.KEY_UP and current_option > 0:
            current_option -= 1
        elif key == curses.KEY_DOWN and current_option < len(options) - 1:
            current_option += 1
        elif key == ord('\n'):
            # User selected an option
            stdscr.clear()
            stdscr.addstr(7, 10, f"You chose {options[current_option]}")
            stdscr.refresh()
            stdscr.getch()
            break

wrapper(main)