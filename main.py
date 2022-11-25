import turtle
import pandas
screen = turtle.Screen()

screen.title('U.S. States Game')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
game_is_on = True
counter = 0
correct_guess_list = []
while game_is_on:
    answer = screen.textinput(title= f"{counter}/50 Guess the state!", prompt= "What's the state name?")

    data = pandas.read_csv("50_states.csv")


    state_list = data['state'].to_list()

    for state in state_list:
        if answer == state:
            correct_guess_list.append(state)
            row = data[data.state == answer]
            xcor = int(row.x)
            ycor = int(row.y)
            map_coordinates = (xcor,ycor)
            counter += 1


            map_label = turtle.Turtle()
            map_label.hideturtle()
            map_label.penup()
            map_label.goto(map_coordinates)
            map_label.write(f"{state}")

        elif answer == "done" or counter == 50:

            game_is_on = False

need_to_learn = []
for each in state_list:
    if each not in correct_guess_list:
        need_to_learn.append(each)
    else:
        continue
dict = {"to study": need_to_learn}
df = pandas.DataFrame(dict)
df.to_csv("Needtolearn.csv")

