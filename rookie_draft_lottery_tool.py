# import helper functions from file sub.py, along with functions for randomness.
import sub
import random

# Initiate boolean, indicating whether program should restart.
continue_var = True

# Print text to introduce user to purpose of program.
sub.Intro_blurb()
sub.Request_context()
#
# while continue_var == True:
#
#     # Get the user's input for league info
#     requested_prompt = sub.Request_prompt_type()
#
#     # Print confirmation of selection
#     sub.Print_prompt_selection(requested_prompt)
#
#
#     # collect number of teams
#
#     # collect number of lottery slots
#
#     # collect lots per team for regular season
#
#     # collect bonus odds for consolation
#
#     # collect names of teams
#
#     # collect ranking (overall)
#
#     # collect result of consolation
#
#     # draw lots & assign order
#
#     # display order
#
#
#
#
#
#     # Read the corresponding text file, get list of strings
#     # Initialize a switch statement, which gives the correct function to use.
#
#     # Create the appropriate list of prompts
#
#     # If single type, run Read_from_file function.
#     if requested_prompt != 'all':
#         prompt_list = sub.Read_from_file(requested_prompt)
#         print('\nHere is your random', requested_prompt, ':\n')
#         # Return random string from list
#         print(prompt_list[random.randrange(0,len(prompt_list))])
#     else:
#         prompt_list = sub.Read_all()
#         for each in prompt_list:
#             print('\nHere is your random', each, ':\n')
#             # Return random string from list
#             print(prompt_list[each][random.randrange(0,len(prompt_list[each]))])
#
#     # Return to start of program
#     continue_response = ''
#
#     while continue_response not in ('yes', 'no'):
#         continue_response = input('\nWould you like another prompt? enter "yes"'
#                                   'or "no"\n>>>:')
#
#     if continue_response == 'no':
#         continue_var = False
#         sub.Thanks_for_using()
