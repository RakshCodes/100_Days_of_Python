'''
Day 6 - Reeborg's World Maze Challenge

Run this code on:
https://reeborg.ca/reeborg.html

Note:
This code uses Reeborg's World built-in functions such as:
move(), turn_left(), right_is_clear(), front_is_clear(), at_goal().
It will not run in a standard Python interpreter like VS Code without the Reeborg environment.
'''

# CODE:
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while (not at_goal()):
    if right_is_clear():
        turn_right()
        move()
    elif (front_is_clear()):
        move()
    else:
        turn_left()












