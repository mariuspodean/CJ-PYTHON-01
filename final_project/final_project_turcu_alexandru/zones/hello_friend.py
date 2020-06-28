import os
import signal
from final_project.final_project_turcu_alexandru import leave_or_stay
from final_project.final_project_turcu_alexandru.Player import Player

player1 = Player()
zones = leave_or_stay.zones
typewriter_decorator = leave_or_stay.typewriter_decorator
player_progress = leave_or_stay.player_progress
good_ending = leave_or_stay.good_ending


@typewriter_decorator(zones['Hello Friend']['DESCRIPTION'])
def start_hello_friend():
    player1.choice = input("> ")
    if player1.choice == 'inspect':
        friend_puzzle()
    else:
        print('Nothing happens')
        start_hello_friend()


@typewriter_decorator(zones['Hello Friend']['INSPECT'])
def friend_puzzle():
    player1.choice = input("> ")
    if player1.choice in zones['Hello Friend']['ANSWERS_INSPECT']:
        player_decision_friend()
    else:
        print('Nothing happens')
        friend_puzzle()


@typewriter_decorator(zones['Hello Friend']['PUZZLE'])
def player_decision_friend():
    player1.choice = input("> ")
    if player1.choice == 'leave':
        bad_ending()
    elif player1.choice == 'stay':
        good_ending()
    else:
        print('Nothing happens..')
        player_decision_friend()


@typewriter_decorator(zones['Hello Friend']['BAD_ENDING'])
def bad_ending():
    print('\n\x1B[3mYou have failed to defuse the reactor resulting in a worldwide catastrophe..\x1B[23m\n')
    print('Au revoir...' + player1.name)
    os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
