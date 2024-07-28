from turtle import Screen, Turtle
import pandas as pd
# File Setup
states_data = pd.read_csv("50_states.csv")
states_data = states_data.to_dict()
# print(states_data)
#
# print(type(states_data["x"][0]))
missed_states = []
guessed_states = []
# Screen Setup
win = Screen()
win.setup(725, 491)
win.bgpic("blank_states_img.gif")
win.title("Name the States")
# Turtle Setup
deliver = Turtle()
deliver.penup()
deliver.hideturtle()


while len(guessed_states) != 50:
    state_guess = win.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state name?").title()
    if state_guess == "Exit":
        # using list comprehensions i know it looks awful but i understood it at the time so yeah..... fuck it
        missed_states = [states_data["state"][index] for index in states_data["state"] if states_data["state"][index] not in guessed_states]
        # This code looks like shit i know 
        # for index in states_data["state"]:
        #     if states_data["state"][index] not in guessed_states:
        #         missed_states.append(states_data["state"][index])
        missed = pd.DataFrame(missed_states)
        missed.to_csv("missed_states")
        break
    for index in states_data["state"]:
        if state_guess == states_data["state"][index]:
            if state_guess not in guessed_states:
                deliver.goto(states_data["x"][index], states_data["y"][index])
                deliver.write(state_guess, align="center", font=("arial", 8, "normal"))
                guessed_states.append(state_guess)

