import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title="Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [
            state for state in all_states if state not in guessed_states]
        missed = pandas.DataFrame(missing_states)
        missed.to_csv("missed_states.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item())

    # else:
    #     if state in all_states != in guessed_states:
    #     missed = pandas.DataFrame(data_dict)
    #     missed.to_csv("missed_states.csv")
