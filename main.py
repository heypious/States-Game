import turtle

import pandas

screen = turtle.Screen()
screen.title("States Game")

country_list = ["india", "usa"]
print("Choose Country")
for country in country_list:
    print(country)
choose = input("-> ").lower()

if choose in country_list:

    image = f'{choose}.gif'
    screen.addshape(image)
    turtle.shape(image)

    data = pandas.read_csv(f"{choose}.csv")
    states = data.state.tolist()


    def write_state(name, position):
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.setpos(position)
        state.write(name)


    guessed_states = []
    game_is_on = True

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(states)} States Correct",
                                        prompt="What's another state's name?").title()

        if answer_state in states:
            guessed_states.append(answer_state)
            xcor = data.x[states.index(answer_state)]
            ycor = data.y[states.index(answer_state)]
            write_state(answer_state, (int(xcor), int(ycor)))

        elif answer_state == "Exit":
            states_to_learn = []

            for x in states:
                if x not in guessed_states:
                    states_to_learn.append(x)

            pandas.Series(states_to_learn).to_csv('states_to_learn.csv')
            break
