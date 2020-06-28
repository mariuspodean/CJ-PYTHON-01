import os
import signal
from final_project.final_project_turcu_alexandru import leave_or_stay
from final_project.final_project_turcu_alexandru.zones.dark_dungeon import start_dark_dungeon
from final_project.final_project_turcu_alexandru.Player import Player

player1 = Player()
zones = leave_or_stay.zones
typewriter_decorator = leave_or_stay.typewriter_decorator
title_screen = leave_or_stay.title_screen
QUESTIONS = leave_or_stay.QUESTIONS
player_progress = leave_or_stay.player_progress


@typewriter_decorator(zones['Scenario']['DESCRIPTION'])
def start_scenario():
    player1.choice = input("> ")
    if player1.choice in zones['Scenario']['INSPECT_ROOM']:
        scenario_puzzle()
        player1.level_up()
    else:
        print('Nothing happens')
        start_scenario()


@typewriter_decorator(zones['Scenario']['INSPECT'])
def scenario_puzzle():
    player1.choice = input("> ")
    if player1.choice in zones['Scenario']['ANSWERS_COMPUTER']:
        player_decision_computer()
    elif player1.choice == 'inspect door':
        player_decision_door()
    elif player1.choice == 'inspect telephone':
        player_decision_telephone()
    elif player1.choice == 'answer telephone':
        player_decision_telephone()
    else:
        print('Nothing happens')
        scenario_puzzle()


@typewriter_decorator(zones['Scenario']['PUZZLE1'])
def player_decision_door():
    player1.choice = input("> ")
    if player1.choice in zones['Scenario']['ANSWERS_ENDING']:
        goodbye_friend()
    elif player1.choice == 'inspect telephone':
        player_decision_telephone()
    elif player1.choice == 'answer telephone':
        player_decision_telephone()
    elif player1.choice in zones['Scenario']['ANSWERS_COMPUTER']:
        player_decision_computer()
    else:
        print('Nothing happens..')
        player_decision_door()


@typewriter_decorator(zones['Scenario']['PUZZLE2'])
def player_decision_computer():
    player1.choice = input("> ")
    if player1.choice in zones['Scenario']['ANSWERS_PUZZLE']:
        player1.level_up()
        game_within_game()
    elif player1.choice == 'inspect door':
        player_decision_door()
    elif player1.choice == 'inspect telephone':
        player_decision_telephone()
    else:
        print('Nothing happens..')
        player_decision_computer()


@typewriter_decorator(zones['Scenario']['PUZZLE3'])
def player_decision_telephone():
    player1.choice = input("> ")
    if player1.choice in zones['Scenario']['ANSWERS_ENDING']:
        goodbye_friend()
    elif player1.choice == 'inspect door':
        player_decision_door()
    elif player1.choice in zones['Scenario']['ANSWERS_COMPUTER']:
        player_decision_computer()
    else:
        print('Nothing happens..')
        player_decision_telephone()


def player_ending():
    player1.choice = input("> ")
    if player1.choice in zones['Scenario']['ANSWERS_ENDING']:
        goodbye_friend()
    elif player1.choice in zones['Scenario']['ANSWERS_COMPUTER']:
        player_decision_computer()
    elif player1.choice == 'inspect door':
        player_decision_door()
    else:
        print('Nothing happens..')
        player_ending()


@typewriter_decorator(zones['Scenario']['GAME_WITHIN_GAME'])
def game_within_game():
    get_ready()
    player1.choice = input("> ")
    if player1.choice == 'yes':
        player1.level_up()
        start_dark_dungeon()
    elif player1.choice == 'no':
        scenario_puzzle()
    else:
        print('Nothing happens..')
        game_within_game()


@typewriter_decorator(QUESTIONS['get_ready'])
def get_ready():
    player1.choice = input("> ")
    if player1.choice == 'yes':
        player1.location = 'Dark Dungeon'
        player1.level_up()
        start_dark_dungeon()
    elif player1.choice == 'no':
        scenario_puzzle()
    else:
        print('Nothing happens..')
        get_ready()


@typewriter_decorator(zones['Scenario']['BAD_ENDING'])
def goodbye_friend():
    print('Au revoir..' + player1.name)
    os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)




