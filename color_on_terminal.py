from colorama import Fore, Back, Style, init
from termcolor import colored, cprint
import sys
print("colorama:")

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')

print("simple ANSI color coding...")

print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color

"""
Available formatting constants are:
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""

def autore():
    init(autoreset=True) #for colorama

"""
The only ANSI sequences that colorama converts into win32 calls are:

ESC [ 0 m       # reset all (colors and brightness)
ESC [ 1 m       # bright
ESC [ 2 m       # dim (looks same as normal brightness)
ESC [ 22 m      # normal brightness

# FOREGROUND:
ESC [ 30 m      # black
ESC [ 31 m      # red
ESC [ 32 m      # green
ESC [ 33 m      # yellow
ESC [ 34 m      # blue
ESC [ 35 m      # magenta
ESC [ 36 m      # cyan
ESC [ 37 m      # white
ESC [ 39 m      # reset

# BACKGROUND
ESC [ 40 m      # black
ESC [ 41 m      # red
ESC [ 42 m      # green
ESC [ 43 m      # yellow
ESC [ 44 m      # blue
ESC [ 45 m      # magenta
ESC [ 46 m      # cyan
ESC [ 47 m      # white
ESC [ 49 m      # reset

# cursor positioning
ESC [ y;x H     # position cursor at x across, y down
ESC [ y;x f     # position cursor at x across, y down
ESC [ n A       # move cursor n lines up
ESC [ n B       # move cursor n lines down
ESC [ n C       # move cursor n characters forward
ESC [ n D       # move cursor n characters backward

# clear the screen
ESC [ mode J    # clear the screen

# clear the line
ESC [ mode K    # clear the line
"""
###
"""
Multiple numeric params to the 'm' command can be combined into a single sequence:

ESC [ 36 ; 45 ; 1 m     # bright cyan text on magenta background
"""
#################################################################################
print("termcolor:")
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
cprint('Hello, World!', 'green', 'on_red')

print_red_on_cyan = lambda x: cprint(x, 'red', 'on_cyan')
print_red_on_cyan('Hello, World!')
print_red_on_cyan('Hello, Universe!')

for i in range(10):
    cprint(i, 'magenta', end=' ')

cprint("Attention!", 'red', attrs=['bold'], file=sys.stderr)

"""
Text colors:
    grey
    red
    green
    yellow
    blue
    magenta
    cyan
    white

Text highlights:
    on_grey
    on_red
    on_green
    on_yellow
    on_blue
    on_magenta
    on_cyan
    on_white

Attributes:
    bold
    dark
    underline
    blink
    reverse
    concealed
"""
