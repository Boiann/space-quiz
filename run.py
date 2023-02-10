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
