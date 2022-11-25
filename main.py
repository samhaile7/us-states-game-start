import turtle
import pandas
screen = turtle.Screen()

screen.title('U.S. States Game')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
game_is_on = True
counter = 0
while game_is_on:
    answer = screen.textinput(title= f"{counter}/50 Guess the state!", prompt= "What's the state name?")
    #print(answer)

    data = pandas.read_csv("50_states.csv")

    #print(data)
    state_list = data['state'].to_list()
    #print(state_list)
    for state in state_list:
        if answer == state:
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

        elif answer == "done":

            game_is_on = False



#
# print(row)
#
