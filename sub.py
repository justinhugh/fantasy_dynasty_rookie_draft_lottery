# A file which defines the sub-functions required to facilitate a rookie draft
# lottery.

# Import libraries for file navigator.
import tkinter.filedialog
import os
import pandas as pd

# Function to write introductory text at start of the program.
def Intro_blurb():
    print('\n\nThis is a script that will help you create a draft order for a '
    'fantasty dynasty draft, using lottery odds for the primary picks.\n')

# Function to ask for the details for the league this tool is used for.
def Request_context():
    '''
    Requests input from the user to determine details about the league and
    lottery. Returns a dictionary which communicates the collected context.
    '''

    # create a dictionary which will
    league_info = {'num_teams':0,
        'num_lot':0,
        'num_lot_teams':0}

    # Get the number of teams from the user
    num_teams = 0
    while num_teams not in [x for x in range(1,31)]:
        response = input('\nHow many teams are in your league?\n>>>: ')
        try:
            num_teams = int(response)
        except ValueError:
            print("You did not enter an integer between 1 and 30, try again")
            continue
        if num_teams > 30 or num_teams < 1:
            print("You did not enter an integer between 1 and 30, try again")
    league_info['num_teams'] = num_teams

    print('\nYour league has', league_info['num_teams'],'teams')

    # Get the number of lottery picks from the user
    num_lot = 0
    while num_lot not in [x for x in range(1,league_info['num_teams']+1)]:
        response = input('\nHow many lottery picks?\n>>>: ')
        try:
            num_lot = int(response)
        except ValueError:
            print("You did not enter an integer between 1 and",
            str(league_info['num_teams']) + ", try again")
            continue
        if num_lot > league_info['num_teams'] or num_lot < 1:
            print("You did not enter an integer between 1 and",
            str(league_info['num_teams']) + ", try again")
    league_info['num_lot'] = num_lot

    print('\nYour league has', league_info['num_lot'],'lottery picks to draw'
    '\n')

    # Get the number of teams in lottery
    num_lot_teams = 0
    while num_lot_teams not in [x for x in range(league_info['num_lot']+1,
            league_info['num_teams']+1)]:
        response = input('\nHow many teams in the lottery?\n>>>: ')
        try:
            num_lot_teams = int(response)
        except ValueError:
            print("You did not enter an integer between", league_info['num_lot']
                +1, "and",
            str(league_info['num_teams']) + ", try again")
            continue
        if (
                num_lot_teams > league_info['num_teams'] or
                num_lot_teams < league_info['num_lot'] +1
            ):
            print("You did not enter an integer between", league_info['num_lot']
                +1, "and",
            str(league_info['num_teams']) + ", try again")
    league_info['num_lot_teams'] = num_lot_teams

    print('\nYour league has', league_info['num_lot_teams'],'teams eligible'
    ' for the lottery\n')

    # Get base odds for lottery.
    league_info['base_odds'] = {}
    for i in range(league_info['num_lot_teams']):
        league_info['base_odds'][league_info['num_teams']-i]=0

    response = input(('\nEnter the base odds for the' + " "
        + str(league_info['num_lot_teams']) + ' lottery eligible teams. Start from last'
        'place, and separate the odds with a comma.\n>>>: '))

    list = response.split(",")

    for i in range(league_info['num_lot_teams']):
        league_info['base_odds'][league_info['num_teams']-i] = list.pop(0)

    print(league_info)

    # Get the number of teams to win consolation odds (prizes)
    num_prize_teams = 0
    while True:
        response = input('\nHow many teams will win additional odds?\n>>>: ')

        try:
            num_prize_teams = int(response)
        except ValueError:
            print("You did not enter an integer between 0 and",
            str(league_info['num_lot_teams']) + ", try again")
            continue
        if (
                num_prize_teams > league_info['num_lot_teams'] or
                num_prize_teams < 0
            ):
            print("You did not enter an integer between", league_info['num_lot']
                +1, "and",
            str(league_info['num_teams']) + ", try again")

        league_info['num_prize_teams'] = num_prize_teams

        if num_prize_teams in [x for x in range(
            league_info['num_lot_teams']+1)]:
                break

    print('\n', league_info['num_prize_teams'],'teams will have their odds '
        'improved\n')
