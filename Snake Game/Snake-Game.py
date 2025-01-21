import curses
import locale

from random import randint # gives a random interger
# setup window (screen)

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")  # Set locale for Unicode support

curses.initscr()
win = curses.newwin(20, 60, 0, 0) # y,x is order
win.keypad(1) #allows use of keyboard for terminal
curses.noecho() # dosen't allow listening to other input characters
curses.curs_set(0) # hides the cursor
win.border(0) # draws a boarder
win.nodelay(1) # -1 # not waiting for the next user input until the user enters the next key

# snake and food
snake = [(4, 10), (4, 9), (4,8)] #a list containing a tuple for snake coordinates (the front is the head the last is the tail)
food = (10, 20) # a tuple for food coordinates

food_emoji = "🍎"
snake_emoji = "#"

win.addstr(food[0], food[1], food_emoji)

# game logic
score = 0

ESC = 27 # the number 27 represents ESC as mentioned in curses module
key =  ord('d')


while key != ESC:
    win.addstr(0, 2, 'score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120) # increase size of snake based on the size

    prev_key = key
    event = win.getch() # get the next character
    key = event if event != -1 else prev_key # allwos the snake to continue in one direction if the key was not pressed
    
    if key not in [ ord('w'), ord('a'), ord('s'), ord('d'), ESC]: # if none of the keys have been found
        key = prev_key
    
    # calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == ord('w'):
        y -= 1 #increases the coordinate (moves the snake) based on the key
    if key == ord('s'):
        y += 1 #increases the coordinate (moves the snake) based on the key
    if key == ord('a'):
        x -= 1 #increases the coordinate (moves the snake) based on the key
    if key == ord('d'):
        x += 1 #increases the coordinate (moves the snake) based on the key
    
    snake.insert(0, (y, x)) # even though .append is faster then .insert, using .insert shouldn't be a worry 
    # this moves the snakes head depeneding on the key pressed

    # check if we hit the border
    if y == 0: break
    if y == 19: break
    if x == 0: break
    if x == 59: break


    # if snake runs over itself
    if snake[0] in snake[1:]: break
    
    if snake[0] == food: 
        # eat the food
        score += 1
        food = ()
        while food == (): # a loop to spawn food in area
            food = (randint(1,18), randint(1,58)) # uses random to place food around area
            if food in snake:
                food = () # removes the food
        win.addstr(food[0], food[1], '  ') # emojis take up two spaces, clearing two spaces
    else:
        # move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    win.addch(snake[0][0], snake[0][1], snake_emoji)

    for c in snake:
        win.addch(c[0], c[1], snake_emoji)
    
    win.addstr(food[0], food[1], food_emoji)

curses.endwin()
print(f"Final score = {score}") # returns the score

