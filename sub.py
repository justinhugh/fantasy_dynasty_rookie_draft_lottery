# A file which defines the sub-functions required to facilitate a rookie draft
# lottery.

# Import libraries for file navigator.
import tkinter.filedialog
import os
import random

# Function to write introductory text at start of the program.
def Intro_blurb():
    '''
    Prints the initial text to introduce the purpose of this script.
    '''
    print('===================='
    '\n\nFANTASY NBA DRAFT LOTTERY'
    '\n\nThis is a python script that will help you conduct a lottery draw for '
    'draft picks you in your fantasty draft.\n\n'
    '====================')

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
        'adjusted_odds':{},
        'draw':[]
        }

    # 1 - Get the number of teams from the user
    num_teams = 0
    while num_teams not in [x for x in range(1,31)]:
        response = input('\nHow many teams are in your league?\n>>>: ')
        try:
            num_teams = int(response)
        except ValueError:
            print("\n!!!You did not enter an integer between 1 and 30, try again")
            continue
        if num_teams > 30 or num_teams < 1:
            print("\n!!!You did not enter an integer between 1 and 30, try again")
    league_info['num_teams'] = num_teams

    print('\nYour league has', league_info['num_teams'],'teams')

    # 2 - Get the number of lottery picks to be awarded from the user
    num_lot = 0
    while num_lot not in [x for x in range(1,league_info['num_teams']+1)]:
        response = input('\nHow many draft picks will be awarded in the lottery?\n>>>: ')
        try:
            num_lot = int(response)
        except ValueError:
            print("\n!!!You did not enter an integer between 1 and",
            str(league_info['num_teams']) + ", try again")
            continue
        if num_lot > league_info['num_teams'] or num_lot < 1:
            print("\n!!!You did not enter an integer between 1 and",
            str(league_info['num_teams']) + ", try again")
    league_info['num_lot'] = num_lot

    print('\nYour league has', league_info['num_lot'],'lottery picks to award')

    # 3- Get the number of teams in lottery
    num_lot_teams = 0
    while num_lot_teams not in [x for x in range(league_info['num_lot']+1,
            league_info['num_teams']+1)]:
        response = input('\nHow many teams in the lottery?\n>>>: ')
        try:
            num_lot_teams = int(response)
        except ValueError:
            print("\n!!!You did not enter an integer between", league_info['num_lot']
                +1, "and",
            str(league_info['num_teams']) + ", try again")
            continue
        if (
                num_lot_teams > league_info['num_teams'] or
                num_lot_teams < league_info['num_lot'] +1
            ):
            print("\n!!!You did not enter an integer between", league_info['num_lot']
                +1, "and",
            str(league_info['num_teams']) + ", try again")
    league_info['num_lot_teams'] = num_lot_teams

    print('\nYour league has', league_info['num_lot_teams'],'teams eligible to win a lottery pick.')

    # 4 - Get the base odds for lottery. These are the odds before prizes for consolation playoffs.

    response = input(('\nEnter the base odds for the' + " "
        + str(league_info['num_lot_teams']) + ' lottery eligible teams. These are the odds before prizes'
        ' have been awarded for the results of consolation playoffs. '
        'Start from last place, and separate the odds with a comma.\n>>>: '))

    list = response.split(",")

    for i in range(league_info['num_lot_teams']):
        league_info['base_odds'][league_info['num_teams']-i] = int(list.pop(0))

    #Print a summary
    print("\nSummary of Base Odds:\n", league_info['base_odds'])

    # 5 - Get the number of teams to win odds for consolation playoff prizes
    num_prizes = 0
    while True:
        response = input('\nHow many teams will win additional odds?\n>>>: ')

        try:
            num_prizes = int(response)
        except ValueError:
            print("\n!!!You did not enter an integer between 0 and",
            str(league_info['num_lot_teams']) + ", try again")
            continue
        if (
                num_prizes > league_info['num_lot_teams'] or
                num_prizes < 0
            ):
            print("\n!!!You did not enter an integer between", league_info['num_lot']
                +1, "and",
            str(league_info['num_teams']) + ", try again")

        league_info['num_prizes'] = num_prizes

        if num_prizes in [x for x in range(
            league_info['num_lot_teams']+1)]:
                break

    print('\n' + str(league_info['num_prizes']) +' teams will have their odds '
        'improved')

    # 6 - Get the size of the odds prizes

    response = input(('\nEnter the odds prizes for the top '
        + str(league_info['num_prizes']) + ' teams of the consolation'
        ' tournament. Start from first'
        ' place, and separate the odds with a comma.\n>>>: '))

    # TO ADD: Enforcement that the number of odds entered is appropriate
    
    list = response.split(",")

    for i in range(league_info['num_prizes']):
        league_info['prizes'][i+1] = int(list.pop(0))

    #Print a summary
    print("\nSummary of Odds Prizes:\n", league_info['prizes'])

    # 7 - Get Results of Consolation
    response = input(('\nEnter the ' + str(league_info['num_prizes']) +
        ' teams who placed in the consolation tournament.'
         ' Start from first place. Enter the teams\' regular season ranking.'
         ' Separate them with a comma.\n>>>: '))

    list = response.split(",")

     # TO ADD: Enforcement that the number of teams entered is appropriate

    for i,j in zip(range(1, league_info['num_prizes']+1), list):
        league_info['consolation_results'][i] = int(j)

    #Print a summary
    print("\nSummary of Consolation Results:\n", league_info['consolation_results'])

    # 7 - Adjust odds dictionary according to the results of consolation entered by user

    # create a copy of base odds dictionary to adjust with the winnings
    league_info['adjusted_odds'] = league_info['base_odds']

    j=1
    for i in league_info['consolation_results']:
        league_info['adjusted_odds'][league_info['consolation_results'][i]] += (
            league_info['prizes'][i])

    #Print a summary
    print("\nSummary of Odds After Awarding Prizes:\n", league_info['adjusted_odds'])

    # Creates the draw, a list of 100 ballots.
    for value, key in league_info['adjusted_odds'].items():
        league_info['draw'] += key * [value]

    # Print a Summary of the draw bag
    print("\nSummary of the current Draw Bag:\n", league_info['draw'])

    # 8 - Gets information about penalties applied to teams

    # create a copy of adjusted odds dictionary to now enhance with penalties
    league_info['penalized_adjusted_odds'] = league_info['adjusted_odds']

    response = input(('\nEnter the regular season rankings of each of the teams who will receive a penalty'
                      ' for illegal tanking. Separate each number with a comma' 
                      '.\n>>>: '))
    
    list1 = response.split(",")

    response = input(('\nEnter the percentage penalty to be applied, in the same order.'
                      'Separate each number with a comma' 
                      '.\n>>>: '))

    list2 = response.split(",")

    for i,j in zip(list1, list2):
        league_info['penalized_adjusted_odds'][int(i)] -= int(j)

    # Print a Summary of the odds after adjusting for penalties
    print("\nSummary of Odds After Adjusting for Penalties:\n", league_info['penalized_adjusted_odds'])

    # Recreates the draw, a list of 100 ballots.
    league_info['draw'] = []
    for value, key in league_info['penalized_adjusted_odds'].items():
        league_info['draw'] += key * [value]

    # Print a Summary of the adjusted draw bag
    print("\nSummary of the Draw Bag after adjusting for Penalties:\n", league_info['draw'])
    
    while(len(league_info['draw'])<100):
        league_info['draw'] += ['void']

    # Print a Summary of the adjusted draw bag
    print("\nSummary of the Draw Bag after adding Voided Lots:\n", league_info['draw'])

    return league_info

# Function to summarize details of the league.
def Detail_summary(league_info):
    '''
    Prints a summary of the provided information, and asks if the user wants to
    re-enter the details.
    '''

    print('\nThanks for entering those details. Let\'s summarize what you told'
    ' us:\n\n'
    'Number of teams in your league: ', league_info['num_teams'],'\n'
    'Number of lottery picks: ', league_info['num_lot'],'\n'
    'Number of lottery-eligible teams: ', league_info['num_lot_teams'],'\n'
    #Future update required, the below line should be dependent on whether penalties were applied.
    'Summary of lottery odds: ', league_info['penalized_adjusted_odds']
    )

# Conduct the draw
def Draw(league_info):

    # List that will store the draft order
    li = [i for i in range(league_info['num_teams'],0,-1)]

    # Make a list of numbers already drawn
    drawn = []

    # Draw the winners until number of drawn teams is num of lottery teams.
    while len(drawn) < league_info['num_lot']:

        # Make a pick
        pick = random.choice(league_info['draw'])

        # Skip the rest if we've already drawn this number
        if pick in drawn:
            continue
        if not isinstance(pick, int):
            print("\nVoided Lot Drawn!\n")
            continue

        # Add the picked number to the list of drawn teams
        drawn.append(pick)

        # Take the drawn number out of the ordered list
        li.remove(pick)

    # put the drawn numbers at the start of the list
    result = drawn + li

    return result

# Collect the names of the teams in the league
def Give_names(league_info):

    league_info['team_names']={}

    for i in range(league_info['num_teams']):
        name = input(("Enter the name the team that ranked " + (str(i+1)) + ":"))

        league_info['team_names'][i+1] = name

# Make a list in which numbers are replaced by team names
def Name_list(league_info, li):
    subs = league_info['team_names']
    name_li = [subs.get(item,item) for item in li]
    return name_li

# Present the contents of a list in a dramatic way
def Present_drama(li):
    print('\n\n<<<<<<<The results of the lottery are in !!!>>>>>>>\n')
    input(".")
    input(".")
    input(".")

    while li != []:
        input("")
        print("\nThe team with pick number ", len(li), " is:")
        input(".")
        input(".")
        input(".")
        print(li.pop(),'\n\n')
