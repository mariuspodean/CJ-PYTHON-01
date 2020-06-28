from final_project.final_project_turcu_alexandru import leave_or_stay
from final_project.final_project_turcu_alexandru.zones.beach import start_beach
from final_project.final_project_turcu_alexandru.Player import Player

player1 = Player()
zones = leave_or_stay.zones
typewriter_decorator = leave_or_stay.typewriter_decorator
good_ending = leave_or_stay.good_ending
player_progress = leave_or_stay.player_progress

__header = r'''
    ############################################################################
    ##              ,.  _~-.,               .                                 ##
    ##           ~`_ '\/_. \_                                                 ##
    ##          / ,"_>@`,__`~.)             |           .                     ##
    ##          | |  @@@@'  ",! .           .          '                      ##
    ##          `' .^^^     ,'    '         |        .             .          ##
    ##           .^^^   .          \                /          .              ##
    ##          .^^^       '  .     \       |      /       . '                ##
    ##.,.,.     ^^^             ` .   .,+~'`^`'~+,.     , '                   ##
    ##&&&&&&,  ,^^^^.  . ._ ..__ _  .'             '. '_ __ ____ __ _ .. .  . ##
    ##%%%%%%%%%^^^^^^%%&&;_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,  ##
    ##&&&&&%%%%%%%%%%%%%%%%%%&&;,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=##
    ##%%%%%&&&&&&&&&&&%%%%&&&_,.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,##
    ##%%%%%%%%%&&&&&&&&&-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~'##
    ##"'                                                                      ##       
    ##_,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'##
    ##                                                                        ##
    ##~`"^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^##
    ############################################################################
'''


@typewriter_decorator(zones['Secret Tunnel']['DESCRIPTION'])
def start_secret_tunnel():
    player1.choice = input("> ")
    if player1.choice in zones['Secret Tunnel']['ANSWERS_PUZZLE']:
        secret_tunnel_puzzle()
    elif player1.choice in zones['Secret Tunnel']['ANSWERS_STAY']:
        player_stay()
    else:
        print('Nothing happens')
        start_secret_tunnel()


@typewriter_decorator(zones['Secret Tunnel']['FRIEND'])
def secret_tunnel_puzzle():
    player1.choice = input("> ")
    if player1.choice in zones['Secret Tunnel']['ANSWERS_INSPECT']:
        player_decision_tunnel()
        player1.level_up()
    elif player1.choice in zones['Secret Tunnel']['ANSWERS_STAY']:
        player_stay()
    elif player1.choice in zones['Secret Tunnel']['ANSWERS_LEAVE']:
        player1.location = 'Beach'
        print(__header)
        player1.level_up()
        start_beach()
    else:
        print('Nothing happens')
        secret_tunnel_puzzle()


@typewriter_decorator(zones['Secret Tunnel']['PUZZLE'])
def player_decision_tunnel():
    player1.choice = input("> ")
    if player1.choice in zones['Secret Tunnel']['ANSWERS_LEAVE']:
        player1.location = 'Beach'
        print(__header)
        player1.level_up()
        start_beach()
    elif player1.choice in zones['Secret Tunnel']['ANSWERS_STAY']:
        player_stay()
    else:
        print('Nothing happens..')
        player_decision_tunnel()


@typewriter_decorator(zones['Secret Tunnel']['STAY'])
def player_stay():
    player1.choice = input("> ")
    if player1.choice == 'yes':
        good_ending()
    elif player1.choice == 'no':
        secret_tunnel_puzzle()
    else:
        print('Nothing happens..')
        player_stay()


