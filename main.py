import turtle

import pandas


screen = turtle.Screen()
screen.title("Us. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/50 States Correct", prompt = "Guess a State! Or type 'Exit' to end").title()


    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
    if answer_state not in all_states:
        stop_game = screen.textinput(title="Incorrect guess!", prompt=f"Sorry the state you guessed: '{answer_state}' is not a correct state. Press 'Okay' to continue playing or enter 'Exit'").title()
        if stop_game == "Exit":
            break




screen.exitonclick()




