# Import necessary modules
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('space_quiz')

quest = SHEET.worksheet('questions')
question = quest.get_all_values()

answ = SHEET.worksheet('answers')
answer = answ.get_all_values()

hnt = SHEET.worksheet('hints')
hints = hnt.get_all_values()

'''
"questions" is a dictionary that maps the first element of each
row in the question list to the corresponding letter of the answer.
'''
questions = {
    question[0][0]: 'A',
    question[1][0]: 'C',
    question[2][0]: 'B',
    question[3][0]: 'C',
    question[4][0]: 'B'
}

'''
"answers" is a list of lists, where each inner list contains the
first three elements of a row in the answer list.
'''
answers = [
    [answer[0][0], answer[0][1], answer[0][2]],
    [answer[1][0], answer[1][1], answer[1][2]],
    [answer[2][0], answer[2][1], answer[2][2]],
    [answer[3][0], answer[3][1], answer[3][2]],
    [answer[4][0], answer[4][1], answer[4][2]]
]

'''
"hints_display is a dictionary which contains the first elements
of a list named hints.
'''
hints_display = {
    hints[0][0],
    hints[1][0],
    hints[2][0],
    hints[3][0],
    hints[4][0]
}


print('ASCII ART, intro text')

"""
Prompt the user to enter their name and validate the input.
The input must only contain letters and/or numbers and
have a minimum length of 2 characters.The loop continues until a
valid name is entered, breaking the loop and printing the 
player's name to the terminal.
"""
while True:
    player = input('Please enter your name:').capitalize()
    if not player.isalnum():
        print('You must enter a name using only letters and numbers!')
        continue
    elif len(player) < 2:
        print('You have to use a minimum of 2 letters and/or numbers.')
        continue
    else:
        print(f'Hello {player}!')
        break


def start_quiz():
    '''
    This function presents a quiz to the user and collects their answers.
    The quiz is defined by the global dictionaries `questions` and `answers`.
    The user is prompted to enter their answer to each question (A, B, or C).
    If the user's input is not one of the accepted answers (A, B, or C),
    they are prompted again until a valid answer is entered.
    '''
    replies = []
    replies_correct = 0
    question_number = 0

    for key in questions:
        print(key)
        for i in answer[question_number]:
            print(i)

        while True:
            choice = input('Please enter your choice; A, B, or C!').upper()

            if choice in ('A', 'B', 'C'):
                replies.append(choice)
                break
            elif choice == 'Y':
                for hint in hints_display:
                    if hint == hints[question_number][0]:
                        print(hint)
                        break
            else:
                print('ERROR, You are allowed to enter only A, B or C')

        replies_correct += check_answer(questions.get(key), choice)
        question_number += 1

    score(replies_correct)


def check_answer(reply, choice):
    """
    This function checks whether the user's answer to a question is correct.
    The correct answer is passed as the `reply` argument,
    and the user's answer is passed as the `choice` argument.
    """
    if reply == choice:
        print(f'Your choice was {choice}. Correct!')
        return 1
    else:
        print(f'Sorry! The correct answer is {reply}.')
        return 0


def score(replies_correct):
    '''
    This function calculates the user's score based on the number
    of correct answers. The number of correct answers is passed
    as the `replies_correct` argument. The function returns the
    user's score, which is calculated as `replies_correct` multiplied by 5.
    '''
    points = replies_correct * 5
    print(f'You scored {points} points!')


def guide():
    '''
    The help() function is used to print the rules of the
    quiz game to the user. The user is allowed to enter only
    Y or N. The loop continues until the user inputs a valid answer.
    '''
    print('Do you want to see the guide/help section?')
    while True:
        user_input = input('Please enter Y for yes, N for no!')
        user_input = user_input.upper()

        if user_input == 'N':
            print('Great, we will start the quiz then!')
            break
        elif user_input == 'Y':
            print('The Rules')
            print('Press ENTER key when ready!')
            input()
            break
        else:
            print('ERROR, You are allowed to enter only Y or N')
            continue    


def restart_quiz():
    '''
    The restart_quiz function asks the user if they would
    like to try the quiz again. The user is allowed to enter only
    Y or N. The loop continues until the user inputs a valid answer.
    '''
    print('Would you like to try again?')
    while True:
        replay = input('Please enter "Y" for yes, "N" for no!')
        replay = replay.upper()

        if replay == "Y":
            new_quiz()
            break
        elif replay == 'N':
            quit()
        else:
            print('ERROR, You are allowed to enter only "Y" or "N"')
            continue


def new_quiz():   

    guide()

    print(f"Here's your first question, {player}:")

    start_quiz()


def main_function():
    
    new_quiz()

    restart_quiz()


main_function()
