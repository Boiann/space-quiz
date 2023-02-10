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
            else:
                print('ERROR, You are allowed to enter only A, B or C')

        question_number += 1        


start_quiz()