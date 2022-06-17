# import helper functions from file sub.py, along with functions for randomness.
import sub

# Initiate boolean, indicating whether program should restart.
continue_var = True

# Print text to introduce user to purpose of program.
sub.Intro_blurb()

# Loop through asking for details until the user accepts them.
response=''
while response!='y':

    glob_league_info = sub.Request_context()
    sub.Detail_summary(glob_league_info)
    input("")

    # Draw until the user enters 'n'
    inner=''
    while inner !='n':

        # Get and set a random seed from user
        seed = input('\n\nInput an integer as a random seed:')
        sub.random.seed(seed)

        # Conduct a draw
        result = sub.Draw(glob_league_info)

        # Let user spoil the results
        spoil = input("\n\nShould we show you the results of the draw? (y/n): ")

        # Spoil the results or not based on input
        if spoil == 'y':
            print('\n\nThe draft order is:\n',result)

        # Let the user redraw
        inner = input('\n\nDraw again? (y/n):')
        print('\n\n')

    sub.Give_names(glob_league_info)
    sub.Present_drama(sub.Name_list(glob_league_info, result))

    response = input('\n\nWanna exit? (y/n):')
