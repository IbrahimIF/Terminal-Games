# a tic tac toe game plaed int he terminal against an AI

import curses
import locale
import random
import os

# Setup Unicode support for drawing characters
locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

def main(win):
    """
    Main function to run the Tic-Tac-Toe game.
    This function is wrapped by curses.wrapper.
    """
    # Curses setup
    curses.curs_set(0) # Hide cursor
    win.keypad(True) # Enable special keys
    win.nodelay(False) # Wait for user input
    win.clear()

    # Define game constants and variables
    ESC = 27
    ENTER = 10
    players = ["X", "O"]
    current_player_index = 0
    message = ""
    # The board is a 3x3 list of lists, initialized with spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    game_over = False
    
    # Cursor position for player input
    cursor_row = 0
    cursor_col = 0

    # Player Mode Selection
    game_mode = None
    arrow = "→"
    modes = ["Play vs AI", "2 Player"]
    current_mode_index = 0

    def draw_menu(current_mode_index):
        """Draws the main menu for game mode selection."""
        win.clear()
        win.border(0)
        win.addstr(1, 3, "TIC-TAC-TOE", curses.A_BOLD)
        win.addstr(2, 3, "Select Game Mode:")
        
        for idx, mode in enumerate(modes):
            if idx == current_mode_index:
                win.addstr(4 + idx, 5, f"{arrow} {mode}")
            else:
                win.addstr(4 + idx, 7, mode)
        win.addstr(8, 3, "Use W/S to choose, ENTER to select, ESC to quit.")
        win.refresh()
    
    def draw_board(board, cursor_row, cursor_col, current_player_index, game_mode):
        """
        Draws the Tic-Tac-Toe board and the cursor.
        """
        win.clear()
        win.border(0) # Draw a border around the game area
        win.addstr(1, 3, "TIC-TAC-TOE", curses.A_BOLD)
        win.addstr(2, 3, "Use arrow keys to move, ENTER to select, ESC to quit.")
        
        # Display the current player and game message
        win.addstr(3, 3, f"Player {players[current_player_index]}'s turn.")
        win.addstr(4, 3, message)

        # Draw the board grid and the marks
        start_y = 6
        start_x = 5
        
        # Draw vertical lines
        for y in range(5):
            win.addstr(start_y + y, start_x + 2, "|")
            win.addstr(start_y + y, start_x + 6, "|")
        
        # Draw horizontal lines
        for x in range(10):
            win.addstr(start_y + 1, start_x + x, "-")
            win.addstr(start_y + 3, start_x + x, "-")
            
        # Draw board intersections
        win.addstr(start_y + 1, start_x + 2, "+")
        win.addstr(start_y + 1, start_x + 6, "+")
        win.addstr(start_y + 3, start_x + 2, "+")
        win.addstr(start_y + 3, start_x + 6, "+")

        # Add the player's marks
        for r in range(3):
            for c in range(3):
                y_pos = start_y + r * 2
                x_pos = start_x + c * 4
                
                # Check if this is the current cursor position
                if r == cursor_row and c == cursor_col:
                    # Highlight the selected cell
                    win.addstr(y_pos, x_pos, board[r][c], curses.A_REVERSE)
                else:
                    win.addstr(y_pos, x_pos, board[r][c])

        win.refresh()

    def show_end_screen(result_message):
        """Displays the end-of-game screen."""
        win.clear()
        win.border(0)
        win.addstr(5, 5, result_message, curses.A_BOLD)
        win.addstr(7, 5, "Press any key to play again.")
        win.addstr(8, 5, "Press ESC to quit.")
        win.refresh()
        key = win.getch()
        if key == ESC:
            return False # Return False to exit the game loop
        return True # Return True to reset the game

    def get_empty_cells(board):
        """Returns a list of tuples for all empty cells on the board."""
        empty_cells = []
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    empty_cells.append((r, c))
        return empty_cells

    def ai_move(board):
        """
        Simple AI logic for the computer player (O).
        This function is self-contained.
        """
        empty_cells = get_empty_cells(board)
        
        # Win or Block Logic
        for player in ["O", "X"]:
            for r, c in empty_cells:
                temp_board = [row[:] for row in board]
                temp_board[r][c] = player
                if check_win(temp_board, player):
                    return (r, c)
        
        # Center, Corners, Sides Logic
        if (1, 1) in empty_cells:
            return (1, 1)
        
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        available_corners = [c for c in corners if c in empty_cells]
        if available_corners:
            return random.choice(available_corners)
            
        sides = [(0, 1), (1, 0), (1, 2), (2, 1)]
        available_sides = [s for s in sides if s in empty_cells]
        if available_sides:
            return random.choice(available_sides)
            
        return random.choice(empty_cells)

    def check_win(board, player):
        """
        Checks if the current player has won the game.
        """
        # Check rows
        for row in board:
            if all([cell == player for cell in row]):
                return True
        
        # Check columns
        for col in range(3):
            if all([board[row][col] == player for row in range(3)]):
                return True
        
        # Check diagonals
        if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
           (board[0][2] == player and board[1][1] == player and board[2][0] == player):
            return True
            
        return False

    def check_draw(board):
        """
        Checks if the game is a draw.
        """
        for row in board:
            if " " in row:
                return False
        return True
    
    while True:
        # Show mode selection menu
        while game_mode is None:
            draw_menu(current_mode_index)
            key = win.getch()
            if key == ord('w') and current_mode_index > 0:
                current_mode_index -= 1
            elif key == ord('s') and current_mode_index < len(modes) - 1:
                current_mode_index += 1
            elif key == ENTER:
                game_mode = modes[current_mode_index]
            elif key == ESC:
                return # Exit the entire program
        while not game_over:
            draw_board(board, cursor_row, cursor_col, current_player_index, game_mode)
                
                # Human player's turn
            if current_player_index == 0 or game_mode == "2 Player":
                key = win.getch()
    
                if key == ord('w') and cursor_row > 0:
                    cursor_row -= 1
                elif key == ord('s') and cursor_row < 2:
                    cursor_row += 1
                elif key == ord('a') and cursor_col > 0:
                     cursor_col -= 1
                elif key == ord('d') and cursor_col < 2:
                    cursor_col += 1
                elif key == ENTER:
                    if board[cursor_row][cursor_col] == " ":
                        board[cursor_row][cursor_col] = players[current_player_index]
                        
                        if check_win(board, players[current_player_index]):
                            message = f"Player {players[current_player_index]} wins!"
                            game_over = True
                        elif check_draw(board):
                            message = "It's a draw!"
                            game_over = True
                        else:
                            current_player_index = (current_player_index + 1) % 2
                            message = "" # Clear message after a successful move
                    else:
                        message = "That spot is already taken! Try again."
                elif key == ESC:
                    return # Exit the entire program
                
            # AI's turn
            if not game_over and game_mode == "Play vs AI" and current_player_index == 1:
                message = "Computer is thinking..."
                draw_board(board, cursor_row, cursor_col, current_player_index, game_mode)
                curses.napms(500)
                    
                ai_r, ai_c = ai_move(board)
                board[ai_r][ai_c] = "O"
    
                if check_win(board, "O"):
                    message = "The computer wins!"
                    game_over = True
                elif check_draw(board):
                    message = "It's a draw!"
                    game_over = True
                else:
                    current_player_index = 0
                    message = "" # Clear message after a successful move
    
        # Game is over, show end screen
        keep_playing = show_end_screen(message)
        if keep_playing:
            # Reset game state
            board = [[" " for _ in range(3)] for _ in range(3)]
            game_over = False
            current_player_index = 0
            message = ""
            cursor_row = 0
            cursor_col = 0
            game_mode = None # Go back to the mode selection screen
        else:
            break # Exit the main while loop and end the program

    curses.endwin()

# Run the game
curses.wrapper(main)
