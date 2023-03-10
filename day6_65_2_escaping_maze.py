#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

    
#action
while not at_goal():
    if right_is_clear() and front_is_clear():
        move()
    elif right_is_clear() and not wall_in_front() and not is_facing_north():
        turn_right()
    elif right_is_clear() and not wall_in_front() and if_facing_north():
        move()
    elif not right_is_clear() and front_is_clear():
        move()
    elif right_is_clear() and wall_in_front():
        turn_right()
        move()
    elif right_is_clear() and is_facing_north():
        move()
    else:
        turn_left()
    
   
    
    