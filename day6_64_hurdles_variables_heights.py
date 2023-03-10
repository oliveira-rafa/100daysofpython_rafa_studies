#http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

"""
What do you need to know:
The functions move() and turn_left().
The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
How to use a while loop and an if statement.
"""

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left()
    
#action
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()