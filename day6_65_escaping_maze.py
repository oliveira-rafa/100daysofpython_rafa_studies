#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

lw = False
rw = False
fw = False

def check_position(lw, rw, fw):
    if front_is_clear():
        fw = False
    if right_is_clear():
        rw = False
    turn_left()
    if front_is_clear():
        lw = False
    turn_left()
    turn_left()
    turn_left()
    
    return lw, rw, fw
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
def step():
    if not wall_in_front() and wall_on_right():
        move()
    elif not wall_in_front():
        move()
    else:
        pass

def check_clear():
    while wall_in_front():
        turn_left()
        step()

def jump():
    turn_left()
    step()
    turn_right()
    step()
    turn_right()
    step()
    turn_left()
    
#action
while not at_goal():
    if right_is_clear() and front_is_clear():
        move()
    elif right_is_clear() and not wall_in_front() and not is_facing_north():
        turn_right()
    elif not right_is_clear() and front_is_clear():
        move()
    elif right_is_clear() and wall_in_front():
        turn_right()
        move()
    elif right_is_clear() and is_facing_north():
        move()
    elif not front_is_clear():
        turn_right()
    else:
        turn_left()