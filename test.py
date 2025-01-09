import curses
def main(stdscr):
    while 1:
        stdscr.keypad(True)
        Key = stdscr.getch()
        if Key == curses.KEY_UP:
            stdscr.addstr(0,0,'u pressed up key ')
            stdscr.addstr(0, 0, '%s' % Key == curses.KEY_UP)
            stdscr.refresh()
        elif Key == curses.KEY_DOWN:
            stdscr.addstr(0,0,'u pressed down key')
            stdscr.addstr(0, 0, '%s' % Key == curses.KEY_UP)
            stdscr.refresh()
        elif Key == curses.KEY_LEFT:
            stdscr.addstr(0,0,'u pressed left key')
            stdscr.addstr(0, 0, '%s' % Key == curses.KEY_UP)
            stdscr.refresh()
        elif Key == curses.KEY_RIGHT:
            stdscr.addstr(0,0,'u pressed right key')
            stdscr.addstr(0, 0, '%s' % Key == curses.KEY_UP)
            stdscr.refresh()
        elif Key == ord('q'):
            break
curses.wrapper(main)