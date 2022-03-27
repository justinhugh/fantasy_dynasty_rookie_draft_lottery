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

# Function to ask for the details of the league.
def Request_context():
    '''
    Requests input from the user to determine details about the league and
    lottery. Returns a dictionary which communicates the collected context.
    '''

    # create a dictionary which will keep league details
    league_info = {'num_teams':0,
        'num_lot':0,
        'num_lot_teams':0,
        'base_odds':{},
        'num_prizes':0,
        'prizes':{},
        'consolation_results':{},
        'adjusted_odds':{}}

    # 1 - Get the number of teams from the user
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

    # 2 - Get the number of lottery picks from the user
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

    # 3- Get the number of teams in lottery
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

    # 4 - Get base odds for lottery.

    response = input(('\nEnter the base odds for the' + " "
        + str(league_info['num_lot_teams']) + ' lottery eligible teams. Start from last'
        'place, and separate the odds with a comma.\n>>>: '))

    list = response.split(",")

    for i in range(league_info['num_lot_teams']):
        league_info['base_odds'][league_info['num_teams']-i] = int(list.pop(0))

    print(league_info)

    # 5 - Get the number of teams to win consolation odds (prizes)
    num_prizes = 0
    while True:
        response = input('\nHow many teams will win additional odds?\n>>>: ')

        try:
            num_prizes = int(response)
        except ValueError:
            print("You did not enter an integer between 0 and",
            str(league_info['num_lot_teams']) + ", try again")
            continue
        if (
                num_prizes > league_info['num_lot_teams'] or
                num_prizes < 0
            ):
            print("You did not enter an integer between", league_info['num_lot']
                +1, "and",
            str(league_info['num_teams']) + ", try again")

        league_info['num_prizes'] = num_prizes

        if num_prizes in [x for x in range(
            league_info['num_lot_teams']+1)]:
                break

    print('\n', league_info['num_prizes'],'teams will have their odds '
        'improved\n')

    # 6 - Get the size of the odds prizes

    response = input(('\nEnter the prize odds for the top' + " "
        + str(league_info['num_prizes']) + ' teams of the consolation'
        'tournament. Start from first'
        'place, and separate the odds with a comma.\n>>>: '))

    list = response.split(",")

    for i in range(league_info['num_prizes']):
        league_info['prizes'][i+1] = int(list.pop(0))

    print(league_info)

    # 7 - Get Results of Consolation
    response = input(('\nEnter the ' + str(league_info['num_prizes']) +
        ' teams who placed in the consolation tournament.'
         'Start from first place. Enter the teams\' regular season ranking.'
         'separate them with a comma.\n>>>: '))

    list = response.split(",")

    for i,j in zip(range(1, league_info['num_prizes']+1), list):
        league_info['consolation_results'][i] = int(j)

    print(league_info)

    # 7 - Adjust odds according to consolation

    # create a copy of base odds dictionary to adjust with the winnings
    league_info['adjusted_odds'] = league_info['base_odds']

    j=1
    for i in league_info['consolation_results']:
        league_info['adjusted_odds'][league_info['consolation_results'][i]] += (
            league_info['prizes'][i])
    print('\n\n\nadjusted odds:\n')
    print(league_info)
    # # 8 - Get names of all Teams
