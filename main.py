import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# print(answer_state)
write_state_in_screen = turtle.Turtle()
write_state_in_screen.penup()
write_state_in_screen.hideturtle()

game_is_on = True  # Initial statement to run the game for while loop

'''
    Reads data of the "50_states.csv" file, in short term it lets us access the 
    data in the file
'''
data = pandas.read_csv("50_states.csv")

states = data.state  # Access the data of all the states from "50_states.csv" file

already_guessed_states = []  # List of states that have already been guessed by the player

'''
    Function which gets the x and y coordinates of the answered state and write the answer_state name on the screen
'''


def create_turtle_and_write_states_name_on_screen(x, y, state_name):
    write_state_in_screen.goto(int(x), int(y))
    write_state_in_screen.write(f"{state_name}")


'''
    The game keeps running until game_is_on is true or the break statement isn't used
'''
while game_is_on:

    # Popup window where it asks for the player to guess the State name
    answer_state = screen.textinput(title=f"{len(already_guessed_states)}/50 States Correct", prompt="Whats another "
                                                                                                     "state's name")
    '''
    Exits out of the Screen after one or the other condition is fulfilled
        1. Player have guessed all 50 states
        2. Player used the exit code "Exit" to exit out of the game
    '''
    if len(already_guessed_states) == 50 or answer_state.title() == "Exit":
        missed_states = [s for s in states if s not in already_guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break

    '''
        Checks if the user input is in the states file, which basically means that the whole block of code checks
        if the user input matches one of the state in states(Derived from CSV file("50_states.csv))
        
        If the user input matches it then checks if the user has already guessed it
            - If the user already guessed it then the loop breaks and the code restarts back to answer_state
            - If the user already guessed is False then the state is appended it into the list of already_guessed_state
              and the code restarts back to answer_state
     '''
    for state in states:
        if answer_state.lower() == state.lower():
            if state in already_guessed_states:
                break
            create_turtle_and_write_states_name_on_screen(int(data[data["state"] == answer_state.title()].x),
                                                          int(data[data["state"] == answer_state.title()].y), state)
            already_guessed_states.append(state)
            break
    continue
