import  turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_column = data.state
states = states_column.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's the another state name?").title()
    if answer_state == "Exit":
        # missing_states = []
        # for item in states:
        #     if item not in guessed_states:
        #         missing_states.append(item)
        missing_states = [item for item in states if item not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        location = (state_data.x.item(), state_data.y.item())
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(location)
        t.write(arg=answer_state, align="center", font=("Arial", 8, "normal"))
