import turtle
import pandas
screen = turtle.Screen()

screen.title('U.S. States Game')
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)

answer = screen.textinput(title= "Guess the state!", prompt= "What's the state name?")
print(answer)

data = pandas.read_csv("50_states.csv")
print(data)
row = data[data.state == answer]
print(row)

