import curses
import locale
from random import randint # gives a random interger
# setup window (screen)

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")  # Set locale for Unicode support

curses.initscr()
win = curses.newwin(20, 60, 0, 0) # y,x is order
win.keypad(1) #allows use of keyboard for terminal
win.border(0)
curses.curs_set(0) # hides the cursor

arrow = "←"

rock = "🧱"
paper = "📃"
scissors = "✂️"

ESC = 27
ENTER = 343
key = ord('d')
score = 0

# Set up options and initial index
options = ["Rock", "Paper", "Scissors"]
current_option = 0

while key != ESC:
    win.addstr(0, 2, 'score ' + str(score) + ' ')
    win.addstr(4, 2, "Welcome to Rock Paper Scissors Terminal Game")
    win.addstr(5, 2, "Use arrow keys to choose an option and press Enter")
    win.addstr(6, 2, "press Enter to play")
    key = win.getch() #get user input

    if key == ord('\n'): 
        win.clear()
        win.refresh()

curses.endwin()

