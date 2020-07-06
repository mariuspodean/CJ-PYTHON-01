from final_project.final_project_turcu_alexandru import leave_or_stay
from final_project.final_project_turcu_alexandru.zones.secret_tunnel import start_secret_tunnel
from final_project.final_project_turcu_alexandru.Player import Player

player1 = Player()
zones = leave_or_stay.zones
typewriter_decorator = leave_or_stay.typewriter_decorator
good_ending = leave_or_stay.good_ending
player_progress = leave_or_stay.player_progress

__header = r'''
    ###############################################################
    ##|010!@#!@#0101 _- !@#```_# @@@(#!!@ !# 0101010101010101~~| ##
    ##|      .-````````'.   -_- _- _- !@#01010!@#!@#01010101~  | ##
    ##|    .` |           `.  01010101&^(@!^*#$10101010'-_- _- | ##
    ##|   /   |             \     O                            | ##
    ##|  |    |              | %%%T%%%    , .--"`````""--.     | ##
    ##|  |    |              |    |       ("-.,_____,.-""/)    | ##
    ##|  |    |              |    |       \-., _____,.-- //    | ##
    ##|  |    |              |   /_\      |_______________|    | ##
    ##|  |    |______________|            |"-[=========]-"|    | ##
    ##|  |   /  __ ;   -     |            |"   X  X  X   "|    | ##
    ##|  |  / __  ...       -|        -    \-[=========]-"/ -_ | ##
    ##|  | /        __-- _   |   _- _ - __- `'-.,_____,.-' __- | ##
    ##|_-  _--        _- _---       -_- _- _-  _-- _--       -_| ##
    ###############################################################
'''


@typewriter_decorator(zones['Dark Dungeon']['DESCRIPTION'])
def start_dark_dungeon():
    player1.choice = input("> ")
    if player1.choice in zones['Dark Dungeon']['INSPECT_DUNGEON']:
        dark_dungeon_puzzle()
    else:
        print('Nothing happens')
        start_dark_dungeon()


@typewriter_decorator(zones['Dark Dungeon']['INSPECT'])
def dark_dungeon_puzzle():
    player1.choice = input("> ")
    if player1.choice in zones['Dark Dungeon']['ANSWERS_INSPECT']:
        print(__header)
        player_decision_dungeon()
        player1.level_up()
    elif player1.choice in 'ANSWERS_STAY':
        player_stay()
    else:
        print('Nothing happens')
        dark_dungeon_puzzle()


@typewriter_decorator(zones['Dark Dungeon']['PUZZLE'])
def player_decision_dungeon():
    player1.choice = input("> ")
    if player1.choice in zones['Dark Dungeon']['ANSWERS_PUZZLE']:
        player1.level_up()
        player1.location = 'Secret Tunnel'
        start_secret_tunnel()
    elif player1.choice in 'ANSWERS_STAY':
        player_stay()
    else:
        print('Nothing happens..')
        player_decision_dungeon()


@typewriter_decorator(zones['Dark Dungeon']['STAY'])
def player_stay():
    player1.choice = input("> ")
    if player1.choice == 'yes':
        good_ending()
    elif player1.choice == 'no':
        player_decision_dungeon()
    else:
        print('Nothing happens..')
        player_stay()

