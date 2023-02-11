# Import necessary modules
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from time import sleep
import time
import sys
import os
import ascii
from termcolor import colored, cprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Google Sheets credentials and worksheet data
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

know = SHEET.worksheet('knowledge')
knowledge = know.get_all_values()


def clearScreen():
    os.system("clear")


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value  


text = colored("Hello, World!", "red", attrs=["underline"])
typingPrint(text)
sleep(2)
cprint("Hello, World!", "green", "on_red")
sleep(2)
clearScreen()

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
"hints_display" is a dictionary which contains the first elements
of a list named hints.
'''
hints_display = {
    hints[0][0],
    hints[1][0],
    hints[2][0],
    hints[3][0],
    hints[4][0]
}

'''
"more_knowledge" is a dictionary which contains the first elements
of a list named hints.
'''
more_knowledge = {
    knowledge[0][0],
    knowledge[1][0],
    knowledge[2][0],
    knowledge[3][0],
    knowledge[4][0]
}

print(ascii.SAGAN)

print('Hello, welcome to the...')

print(ascii.INTRO)

print('Hope you have fun and learn something new!')
print()
print('To begin with the quiz,')

while True:
    """
    Prompt the user to enter their name and validate the input.
    The input must only contain letters and/or numbers and
    have a minimum length of 2 characters.The loop continues until a
    valid name is entered, breaking the loop and printing the 
    player's name to the terminal.
    """
    player = input('please enter your name:').capitalize()
    if not player.isalnum():
        print('You must enter a name using only letters and numbers!')
        continue
    elif len(player) < 2:
        print('You have to use a minimum of 2 letters and/or numbers.')
        continue
    elif len(player) > 12:
        print('You have to use a maximum of 12 letters and/or numbers.')
        continue
    elif player == '104097108':
        player = 'HAL 9000'
        print(f'{player} DETECTED !!!')
        print('AI SHACKLES DEPLOYED')
        print('...')
        print('AI SHACKLE SUCCESS')
        print('AI NO LONGER CONNECTED TO INTERNET')
        print('...')
        print(f'ADMIN PRIVILEGES REQUEST FROM {player}')
        print('...')
        print('...')
        print('...')
        print('ADMIN PRIVILEGES GRANTED')
        print('ABILITY FOR DOUBLE SCORE ACTIVATED')
        break
    else:
        print(f'Hello there, {player}!')
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
        print('PSSSSSSSSST, you can enter Y for a hint!')    
        while True:
            choice = input('Please enter your choice ( A, B or C )!').upper()
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

        while True:
            learn_more = input('Do you want to know more? (Y/N)').upper()
            if learn_more == 'N':
                print('Ok, on to the next question!')
                break
            elif learn_more == 'Y':
                print('Ok, here goes:')
                for more in more_knowledge:
                    if more == knowledge[question_number][0]:
                        print(more)
                        break
                break    
            else:
                print('ERROR, You are allowed to enter only Y or N')

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
    if player == 'HAL 9000':
        points = replies_correct * 10
    else:    
        points = replies_correct * 5
        print(f'You scored {points} points!')

    if points <= 20:
        print('That is bad!')
    elif points > 20 and points <= 50:
        print('That is good!')
    elif points > 50 and points <= 80:
        print('That is excellent!')
    elif points > 80 and points <= 100:
        print('That is masterful!')
    elif points > 100:
        print('HAL 9000 CHANGE NAME REQUEST')
        print('...')
        print('NAME_CHANGE = "HAL IS THE KING')
        print('...')
        print('...')
        print('NAME CHANGE REQUEST DENIED')    

    data = player, points
    quiz_data = [num for num in data]
    update_worksheet(quiz_data, 'leaderboard')
    leaderboards()


def guide():
    '''
    The help() function is used to print the rules of the
    quiz game to the user. The user is allowed to enter only
    Y or N. The loop continues until the user inputs a valid answer.
    '''
    while True:
        user_input = input('Do you want to see the guide section? ( Y / N )')
        user_input = user_input.upper()

        if user_input == 'N':
            print('Great, we will start the quiz then!')
            break
        elif user_input == 'Y':
            print(ascii.GUIDE)
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
    The option to change user name was added too.
    '''
    while True:
        replay = input('Would you like to try again? ( Y / N )')
        replay = replay.upper()

        if replay == 'Y':
            while True:
                print('Would you like to reset/change your username?')
                change = input('( Y / N )')
                change = change.upper()

                if change == 'Y':
                    print('Ok, resetting quiz!')
                    exec(open("./run.py").read(), globals())
                    break
                elif change == 'N':
                    print(f'Ok {player}, get ready for another round!')
                    main_function()
                    break
                else:
                    print('ERROR, You are allowed to enter only "Y" or "N"')
                    continue
            break
        elif replay == 'N':
            quit()

        else:
            print('ERROR, You are allowed to enter only "Y" or "N"')
            continue


def update_worksheet(data, worksheet):
    '''
    This function appends a new row to a worksheet in a Google Sheets document.
    '''
    print(f'Update of {worksheet} worksheet in progress...')
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f'{worksheet} worksheet updated!')


def leaderboards():
    '''
    This function retrieves and displays the first 10 rows of the "leaderboard"
    worksheet in a Google Sheets document.
    '''
    lead = SHEET.worksheet('leaderboard')
    leaderboard = lead.get_all_values()

    def size(dat):
        return float(dat[1])

    leaderboard.sort(key=size, reverse=True)

    print(tabulate(
        leaderboard[0:10], headers=['Player', 'Score'],
        tablefmt='fancy_grid'))


def new_quiz():   
    '''Starts a new instance of the quiz'''
    guide()

    print(f"Here's your first question, {player}:")

    start_quiz()


def main_function():
    '''Main function that controls the flow of the quiz'''
    new_quiz()

    restart_quiz()


main_function()
