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
    '''
    Function for cleaning the cli screen
    '''
    os.system("clear")


def typingPrint(text):
    '''
    Function for typewriter effect for printing the text
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)


def slowerTypingPrint(text):
    '''
    Function for typewriter effect for printing the text, slower speed
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)


def fasterTypingPrint(text):
    '''
    Function for typewriter effect for printing the text, faster speed
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)


def typingInput(text):
    '''
    Function for typewriter effect for printing the inputs text
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    value = input()  
    return value  


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
'''
Intro quote, text and ASCII art in specific order for better UX
'''
# ascii.SAGAN = colored(ascii.SAGAN, 'light_blue', attrs=['bold'])
# slowerTypingPrint(ascii.SAGAN)
# sleep(5)
# clearScreen()
# typingPrint('Hello, welcome to the...')
# sleep(1)
# clearScreen()
ascii.INTRO = colored(ascii.INTRO, 'blue', attrs=['bold'])
# fasterTypingPrint(ascii.INTRO)
# sleep(1)
# typingPrint('Hope you have fun and learn something new!')
# sleep(2)
# print()
# clearScreen()


while True:
    """
    Prompt the user to enter their name and validate the input.
    The input must only contain letters and/or numbers and
    have a minimum length of 2 characters.The loop continues until a
    valid name is entered, breaking the loop and printing the 
    player's name to the terminal.
    """
    typingPrint('To begin with the quiz, ')
    player = typingInput('Please enter your name:').capitalize()
    if not player.isalnum():
        cprint('Please enter a name using only letters/numbers!', 'red')
        continue
    elif len(player) < 2:
        cprint('Please use a minimum of 2 letters and/or numbers.', 'red')
        continue
    elif len(player) > 12:
        cprint('Please use a maximum of 12 letters and/or numbers.', 'red')
        continue
    elif player == '104097108':
        player = 'HAL_9000'
        cprint(f'{player} DETECTED !!!', 'red')
        sleep(1)
        slowerTypingPrint('AI SHACKLES DEPLOYED')
        print()
        sleep(1)
        slowerTypingPrint('...')
        print()
        sleep(1)
        slowerTypingPrint('AI SHACKLE SUCCESS')
        print()
        slowerTypingPrint('AI NO LONGER CONNECTED TO INTERNET')
        print()
        slowerTypingPrint('...')
        print()
        sleep(1)
        slowerTypingPrint(f'ADMIN PRIVILEGES REQUEST FROM {player}')
        print()
        sleep(1)
        slowerTypingPrint('...')
        print()
        slowerTypingPrint('...')
        print()
        slowerTypingPrint('...')
        print()
        sleep(1)
        slowerTypingPrint('ADMIN PRIVILEGES GRANTED')
        print()
        slowerTypingPrint('...')
        print()
        sleep(1)
        slowerTypingPrint('ABILITY FOR DOUBLE SCORE ACTIVATED')
        print()
        sleep(1)
        break
    else:
        typingPrint(f'Hello there, {player}!')
        print()
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
        clearScreen()
        typingPrint(key)
        print()
        sleep(3)
        for i in answer[question_number]:
            print()
            typingPrint(i)
            print()
            # sleep(1)
            
        while True:
            print()
            choice = input('Please enter your choice,(A, B, C), H for a hint!')
            choice = choice.upper()
            if choice in ('A', 'B', 'C'):
                replies.append(choice)
                break
            elif choice == 'H':
                for hint in hints_display:
                    if hint == hints[question_number][0]:
                        cprint(hint, 'light_blue')
                        break        
            else:
                cprint('ERROR, Please enter only A, B, C, H', 'red')
        
        replies_correct += check_answer(questions.get(key), choice)

        while True:
            learn_more = typingInput('Do you want to know more? ( Y / N )')
            learn_more = learn_more.upper()
            if learn_more == 'N':
                if question_number == 4:
                    clearScreen()
                    print()
                    typingPrint('The quiz is now over!')
                    sleep(2)
                    clearScreen()
                    break
                print()
                typingPrint('Ok, on to the next question!')
                sleep(1)
                break
            elif learn_more == 'Y':
                print()
                typingPrint('Ok, here goes:')
                sleep(1)
                print()
                for more in more_knowledge:
                    if more == knowledge[question_number][0]:
                        cprint(more, 'light_cyan')
                        if question_number == 4:
                            print()
                            typingPrint('Press ENTER to finish the quiz!')
                            input()
                            break
                        print()
                        typingPrint('Press ENTER when ready for next round!')
                        input()
                        break
                break    
            else:
                cprint('ERROR, You are allowed to enter only Y or N', 'red')

        question_number += 1

    score(replies_correct)


def check_answer(reply, choice):
    """
    This function checks whether the user's answer to a question is correct.
    The correct answer is passed as the `reply` argument,
    and the user's answer is passed as the `choice` argument.
    """
    if reply == choice:
        print()
        cprint(f'Your choice was {choice}. Correct!', 'green')
        print()
        return 1
    else:
        print()
        cprint(f'Sorry! The correct answer is {reply}.', 'light_red')
        print()
        return 0


def score(replies_correct):
    '''
    This function calculates the user's score based on the number
    of correct answers. The number of correct answers is passed
    as the `replies_correct` argument. The function returns the
    user's score, which is calculated as `replies_correct` multiplied by 5.
    '''
    if player == 'HAL_9000':
        points = replies_correct * 10
    else:    
        points = replies_correct * 5
    
    print()
    cprint(f'You scored {points} points!', 'light_magenta')
    print()

    if points <= 20:
        cprint('You need more space knowledge!', 'light_red')
    elif points > 20 and points <= 50:
        cprint('Ok result, needs improvement!', 'light_blue')
    elif points > 50 and points <= 80:
        cprint('Very good, you know about space!', 'light_green')
    elif points > 80 and points <= 100:
        cprint('This is amazing, congratulation!!!', 'light_magenta')
    elif points > 100:
        slowerTypingPrint('...')
        slowerTypingPrint('HAL_9000 CHANGE NAME REQUEST')
        slowerTypingPrint('...')
        slowerTypingPrint('NAME_CHANGE = "HAL IS THE KING')
        slowerTypingPrint('...')
        slowerTypingPrint('...')
        slowerTypingPrint('NAME CHANGE REQUEST DENIED')    
    
    print()
    typingPrint('Hope you had fun with this quiz!')
    print()
    print()
    typingPrint('Press ENTER to update the leaderboard!')
    input()

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
        user_input = typingInput('Do you want to see the guide? (Y / N)')
        user_input = user_input.upper()

        if user_input == 'N':
            print()
            typingPrint('Great, the quiz is starting!')
            sleep(1)
            break
        elif user_input == 'Y':
            typingPrint('Ok, here it goes:')
            sleep(1)
            clearScreen()
            cprint(ascii.GUIDE, 'light_cyan')
            typingPrint('Press ENTER key when ready!')
            input()
            break
        else:
            cprint('ERROR, You are allowed to enter only Y or N', 'red')
            print()
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
    clearScreen()
    print()
    typingPrint(f'Update of {worksheet} worksheet in progress...')
    print()
    slowerTypingPrint('...')
    print()
    slowerTypingPrint('...')
    print()
    slowerTypingPrint('...')
    print()
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    typingPrint(f'{worksheet} worksheet updated!')
    print()
    typingPrint('...')
    print()
    sleep(1)
    print('Preparing leaderboard...')
    slowerTypingPrint('...')
    print()
    slowerTypingPrint('...')
    print()
    slowerTypingPrint('...')
    print()
    print('DONE!')
    sleep(1)
    print()
    typingPrint('Press ENTER to see the leaderboard!')
    input()
    clearScreen()


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
    
    clearScreen()

    cprint(tabulate(
        leaderboard[0:10], headers=['Player', 'Score'],
        tablefmt='fancy_grid'), 'light_yellow')


def new_quiz():   
    '''Starts a new instance of the quiz'''
    guide()
    clearScreen()
    start_quiz()


def main_function():
    '''Main function that controls the flow of the quiz'''
    new_quiz()

    restart_quiz()


main_function()
