import os
import signal
from final_project.final_project_turcu_alexandru import leave_or_stay
from final_project.final_project_turcu_alexandru.zones.hello_friend import start_hello_friend
from final_project.final_project_turcu_alexandru.Player import Player

player1 = Player()
zones = leave_or_stay.zones
typewriter_decorator = leave_or_stay.typewriter_decorator
player_progress = leave_or_stay.player_progress

__header = r'''
    ###############################################################################
    ##(@@@@)                    (#########)                   (@@@@@@@@(@@@@@@@@@##
    ##@@@@@@)___                 (####)~~~   /\                ~~(@@@@@@@(@@@@@@@##
    ##@@@@@@@@@@)                 ~~~~      /::~-__               ~~~(@@@@@@@@)~~##
    ##@@@)~~~~~~                           /::::::/\                  ~~(@@@@)   ##
    ##~~~                              O  /::::::/::~--,                 ~~~~    ##
    ##                                 | /:::::/::::::/{                         ##
    ##                 |\              |/::::/::::::/:::|                        ##
    ##                |:/~\           ||:::/:::::/::::::|                        ##
    ##               |,/:::\          ||/"::: /::::::::::|                       ##
    ##              |#__--~~\        |"#::,,/::::::::: __|   ,,''.               ##
    ##             |__# :::::\       |-#"":::::::__--~~::| ,'     ',.....,,^/^/^/##
    ##,    ,,     |____#~~~--\,'',.  |_#____---~~:::::::::|         '""  ',..\/..##
    ##            |::::##~~~--\    `,||#|::::::_____----~~~|         ,,,   """"""##
    ##____________----###__:::\_____||#|--~~~~::::: ____--~______,,''____________##
    ##^^^  ^^^^^   |#######\~~~^^O, | ### __-----~~~~_____########"  ^^^^  ^^^...##
    ##,^^^^^' '^^^^,|#########\_||\__O###~_######___###########;" ^^^^  ^^^   ^^.##
    ##^^/\/^^^^/\/\^^|#######################################;/\/\/^^^/\/^^^/\/^ ##
    ##   /\/\/\/\/\  /\|####################################      /\/\/\/\/\     ##
    ##\/\/\     /\/\/\  /\/\/\/\    /\/\/\/\/\   /\/\/\    /\/\/\/\      /\/\/\/\##
    ##\/\/\    /\/\/\/\    /\/\/\/\    /\/\/\/\   /\/\/\/\    /\/\/\/\/\     /\/^##
    ###############################################################################
'''


@typewriter_decorator(zones['Beach']['DESCRIPTION'])
def start_beach():
    player1.choice = input("> ")
    if player1.choice in zones['Beach']['INSPECT_BEACH']:
        print(__header)
        beach_puzzle()
    else:
        print('Nothing happens')
        start_beach()


@typewriter_decorator(zones['Beach']['INSPECT'])
def beach_puzzle():
    player1.choice = input("> ")
    if player1.choice in zones['Beach']['ANSWERS_INSPECT']:
        player_decision_beach()
        player1.level_up()
    else:
        print('Nothing happens')
        beach_puzzle()


@typewriter_decorator(zones['Beach']['PUZZLE'])
def player_decision_beach():
    player1.choice = input("> ")
    if player1.choice in zones['Beach']['ANSWERS_PUZZLE']:
        player1.level_up()
        player_decision_binary()
    elif player1.choice in zones['Beach']['ANSWERS_ENDING']:
        bad_ending()
    else:
        print('Nothing happens..')
        player_decision_beach()


@typewriter_decorator(zones['Beach']['DECISION'])
def player_decision_binary():
    player1.choice = input("> ")
    if player1.choice in zones['Beach']['ANSWERS_LEAVE']:
        bad_ending()
    elif player1.choice == zones['Beach']['ANSWERS_STAY']:
        player1.location = 'Hello Friend'
        player1.level_up()
        player_friend()
    else:
        print('Nothing happens..')
        player_decision_binary()


@typewriter_decorator(zones['Beach']['FRIEND'])
def player_friend():
    player1.choice = input("> ")
    if player1.choice == 'yes':
        player1.location = 'Hello Friend'
        player1.level_up()
        start_hello_friend()
    elif player1.choice == 'no':
        bad_ending()
    else:
        print('Nothing happens..')
        player_friend()


@typewriter_decorator(zones['Beach']['BAD_ENDING'])
def bad_ending():
    print('\n\x1B[3mYou have failed to defuse the reactor resulting in a worldwide catastrophe..\x1B[23m\n')
    print('Au revoir...' + player1.name)
    os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
