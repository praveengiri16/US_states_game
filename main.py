import turtle
import pandas
from turtle import Turtle, Screen
user_guess = []
score = 0
image = "blank_states_img.gif"
s = Screen()
s.title("U.S states Game")
s.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]

states_list = states.to_list()

while len(user_guess) <50:
    user_ans = s.textinput(title=f"{len(user_guess)}/50 States Correct",
                           prompt="What's the name of next state?").title()
    if user_ans == "Exit":
        remain = [state for state in states if state not in user_ans]
        to_learn = pandas.DataFrame(remain)
        to_learn.to_csv("learn_states.csv")
        break
    for state in states:
        if state == user_ans:
            user_guess.append(user_ans)
            map = Turtle()
            map.hideturtle()
            map.penup()
            state_data = data[data.state == user_ans] # Give the data in the row of the state that match
            map.goto(float(state_data.x), float(state_data.y))
            map.write(arg=f"{user_ans}", move=False, align= "center", font=('Arial', 12, "normal"))
            score += 1


turtle.mainloop()
