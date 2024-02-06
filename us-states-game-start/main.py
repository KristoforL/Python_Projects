import turtle as t
import pandas as p
#These paths need to change for the computer you are working on. Relative path for windows seems to work just fine.
screen = t.Screen()
screen.title("U.S. State Game")
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)

t.shape(image)


##Not necessary but would have shown the coordinates to the place clicked so you could get the x y coordinates to place the name of the state
# def get_mouse_click_coor(x,y):
#     print(x,y)
# t.onscreenclick(get_mouse_click_coor)
# t.mainloop()



US = p.read_csv("us-states-game-start\50_states.csv")

states = US["state"].tolist()
#print(states)
guessed = []

while len(guessed)<50:

    name_state = screen.textinput(title=f"{len(guessed)}/50", prompt="What's a state on the map?").title()
   

    if name_state == "Exit":
        missed = [state for state in states if state not in guessed]
        # missed = []
        # for state in states:
        #     if state not in guessed:
        #         missed.append(state)
        
        learn = p.DataFrame(missed)
        learn.to_csv("us-states-game-start\learn.csv")
        break

    if name_state in states and name_state not in guessed:
        guessed.append(name_state)

        newturt = t.Turtle()
        newturt.hideturtle()
        newturt.pu()
        guess = US[US.state == name_state]
        newturt.goto(int(guess.x), int(guess.y))
        newturt.write(name_state)


     


screen.exitonclick()

