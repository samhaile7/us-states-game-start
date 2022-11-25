import turtle
import pandas
screen = turtle.Screen()

screen.title('U.S. States Game')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

while game_is_on:
    answer = screen.textinput(title= "Guess the state!", prompt= "What's the state name?")
    print(answer)

    data = pandas.read_csv("50_states.csv")
    print(data)
    column_list = data['state'].to_list
    for state in column_list:
        if answer == state:
            row = data[data.state == answer]
            #Print name on map here
        else:
            print('try again')

print(row)

