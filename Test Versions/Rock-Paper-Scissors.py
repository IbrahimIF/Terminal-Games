
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




