import os
import signal
import sys
import time
import threading
from playsound import playsound
from final_project.final_project_turcu_alexandru.zones import scenario
from final_project.final_project_turcu_alexandru.Player import Player, AsciiHeader


def play_theme():
    playsound('theme_song.mp3')


player1 = Player()

QUESTIONS = {
    'get_name': 'What is your name?\n',
    'get_difficulty': 'Are you a cheetah or a lion\n',
    'get_ready': 'Is the key in the room?\n',
}

zones = {

    'Scenario': {
        'DESCRIPTION': 'You wake up to the sound of tremors and the ringing of a telephone \n'
                       'and appear to be in a small isolated room with no windows \n'
                       'What do you do?',
        'INSPECT': 'All that you see is an armored door and in the middle of the room there is a desk..\n'
                   '..that has an antique computer along the ringing telephone.\nWhat do you do ?',
        'INSPECT_ROOM': ['inspect room', 'inspect'],
        'ANSWERS_INSPECT': ['inspect door', 'inspect telephone'],
        'ANSWERS_COMPUTER': ['inspect desk', 'inspect computer'],
        'PUZZLE1': 'The door is locked and it appears to have a keypad lock built into the wall\nWhat do you do?',
        'PUZZLE2': 'The computer seems to have a button on it.\nWhat do you do?',
        'PUZZLE3': 'You answer the telephone to a robotic voice that says:\n'
                   'The code for the nuclear reactor bunker room is 1 3 3 7..\nWhat do you do?',
        'ANSWERS_PUZZLE': ['press button', 'press the button', 'push it', 'push the button', 'push button'],
        'ANSWERS_ENDING': ['type code', 'enter code', 'enter code into door', 'type code into door', 'insert code'],
        'GAME_WITHIN_GAME': 'The computer boots up and it starts a text-based adventure game\n'
                            'Its title says: "Leave or Stay"\n',
        'BAD_ENDING': 'The code automatically unlocks the door and a huge burst of ionizing radiation hits you..\n'
                      'Instantly paralysing your body.. making your throat so dry that you can barely gasp for air..\n'
                      'It seems your journey must come to an end. . .\n'
    },

    'Dark Dungeon': {
        'DESCRIPTION': "You're trapped in a dark dungeon with your friend.\nWhat do you do?",
        'INSPECT_DUNGEON': ['inspect', 'inspect dungeon', 'inspect dark dungeon'],
        'INSPECT':  "You feel a barrel next to you.\nWhat do you do?",
        'ANSWERS_INSPECT': ['move the barrel', 'move barrel', 'inspect barrel'],
        'PUZZLE': 'The barrel rolls aside and you find a secret tunnel.\nWhat do you do?',
        'ANSWERS_PUZZLE': ['enter the tunnel', 'enter tunnel', 'go inside', 'inspect tunnel'],
        'STAY': 'Are you sure you want to stay here with your friend?',
        'ANSWERS_STAY': ['stay', 'stay with my friend'],
    },

    'Secret Tunnel': {
        'DESCRIPTION': 'As you start crawling through the tunnel..\n'
                       'You realise your friend is too weak to go with you..\nWhat do you do?',
        'FRIEND': 'When you are about to leave..your friend grasped your arm and gave you a note.\nWhat do you do ?',
        'ANSWERS_INSPECT': ['read note', 'read', 'read the note', 'inspect', 'inspect note'],
        'ANSWERS_PUZZLE': ['leave', 'leave your friend behind', 'leave friend', 'leave without friend', 'enter tunnel'],
        'PUZZLE': 'It is too dark to read the note.\nWhat do you do?',
        'ANSWERS_LEAVE': ['leave', 'leave friend', 'go', 'run', 'leave your friend', 'enter tunnel'],
        'STAY': 'Are you sure you want to stay here with your friend?\n',
        'ANSWERS_STAY': ['stay', 'stay with my friend'],
    },

    'Beach': {
        'DESCRIPTION': 'You crawl through the tunnel and it leads you to a beach.\nWhat do you do?',
        'INSPECT_BEACH': ['inspect', 'inspect beach'],
        'INSPECT': 'In the water you see a boat.\nWhat do you do ?',
        'ANSWERS_INSPECT': ['get on the boat', 'inspect boat', 'go to boat', 'go to the boat', 'get on boat'],
        'PUZZLE': 'In the boat you find a lantern\nWhat do you do ?',
        'ANSWERS_PUZZLE': ['take the lantern', 'pick lantern', 'take lantern', 'inspect lantern'],
        'FRIEND': 'Are you sure you want to go back for your friend?\n',
        'ANSWERS_ENDING': ['leave', 'sail', 'escape', ],
        'DECISION': 'Are you a 0 or are you a 1?\nDo you leave? or do you stay?',
        'ANSWERS_LEAVE': ['leave', '0', 'zero'],
        'ANSWERS_STAY': ['stay', '1', 'one'],
        'BAD_ENDING': 'There it is again..that feeling slowly creeping in..\n'
                      'The overwhelming fear building.. the burrowing.. the nesting.. the scream..\n'
                      'Next my consciousness will go..\n'
                      "The panic isn't settling anymore.. it's just there\n"
                      'The scream in my mind is coming back..What have I done..\n',
    },

    'Hello Friend': {
        'DESCRIPTION': 'You run back to the secret tunnel, slowly crawling your way back to the dark dungeon\n'
                       'Your friend was here waiting for you all along..\nWhat do you do?',
        'INSPECT': 'Your friend hands you back the note...\n '
                   'The lantern provides enough light allowing you to read the note\nWhat do you do?',
        'ANSWERS_INSPECT': ['read', 'read the note', 'read note'],
        'PUZZLE': "The note says: 'Please don't leave me here alone..'\nWhat do you do?",
        'ANSWERS_ENDING': ['leave', 'stay'],
        'BAD_ENDING': 'There it is again..that feeling slowly creeping in..\n'
                      'The overwhelming fear building.. the burrowing.. the nesting.. the screams\n'
                      "The panic isn't settling anymore.. it's just there\n",
    }
}

CREDITS = {
    'good_ending': 'You have managed to defuse the reactor in time..\n'
                   "But after all we've been through friend.. was it all.. worth it?\n"
                   "Saving a world that is made to divide us.. so its easier to rule us?\n"
                   "Are we crazy enough to believe this.. distortion of reality?\n"
                   'The key to a better world... you.. me.. this is how we own it\n'
                   'Because friendship is not a weakness but a power\n'
                   'And if we manage to harness this power..nothing can stop us\n'
                   "It's an exciting time in the world...\nThank you for playing..THE END\n"

}


def main_menu_options():
    option = ''
    while option.lower() not in ['play', 'help', 'quit']:
        option = input("> ")
        if option.lower() == 'play':
            get_name()
            get_difficulty()
            player1.location = zones['Scenario']
        elif option.lower() == 'help':
            help_menu()
        elif option.lower() == 'quit':
            os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)

        else:
            print('Nothing happens..')
        main_menu_options()


@AsciiHeader()
def title_screen():
    print('###.____########################################################__,#####################')
    print('###|    |    ____ _____ ___  __ ____     ___________    _______/  |______  ___.__.######')
    print('###|    |  _/ __ \\\__  \\\  \/ // __ \   /  _ \_  __ \  /  ___/\   __\__  \<   |  |######')
    print('###|    |__\  ___/ / __ \\\   /\  ___/  (  <_> )  | \/  \___ \  |  |  / __ \\\___  |######')
    print('###|_______ \___  >____  /\_/  \___  >  \____/|__|    /____  > |__| (____  / ____|######')
    print('##########\/##\/######\/##########\/######################\/############\/\/############')
    print('########################################################################################')
    print('#####%%#####%%#####>>#####>>#####=##### - Play - #####=#####<<#####<<#####%%#####%%#####')
    print('#####%%#####%%#####>>#####>>#####=##### - Help - #####=#####<<#####<<#####%%#####%%#####')
    print('#####%%#####%%#####>>#####>>#####=##### - Quit - #####=#####<<#####<<#####%%#####%%#####')
    print('########################################################################################')
    main_menu_options()


@AsciiHeader()
def help_menu():
    print('###.____########################################################__,#####################')
    print('###|    |    ____ _____ ___  __ ____     ___________    _______/  |______  ___.__.######')
    print('###|    |  _/ __ \\\__  \\\  \/ // __ \   /  _ \_  __ \  /  ___/\   __\__  \<   |  |######')
    print('###|    |__\  ___/ / __ \\\   /\  ___/  (  <_> )  | \/  \___ \  |  |  / __ \\\___  |######')
    print('###|_______ \___  >____  /\_/  \___  >  \____/|__|    /____  > |__| (____  / ____|######')
    print('##########\/##\/######\/##########\/######################\/############\/\/############')
    print('#####%%#####%%#####> Play - #####%%#####- Help -#####%%##### - Quit <#####%%#####%%#####')
    print('#####%%#####%##>>Type in your commands to do them but try to be specific <<##%####%%####')
    print('#####%%#####%%#####>> Use the "inspect" command and look for clues <<#####%%#####%%#####')
    print('#####%%#####%%#####>>  Solve the riddle and find the "key" to win  <<#####%%#####%%#####')
    print('####################################>Have fun !<########################################')
    main_menu_options()


def typewriter_decorator(text):
    def writer(func):
        def typewriter():
            time.sleep(0.5)
            for elem in text:
                sys.stdout.write(elem)
                sys.stdout.flush()
                time.sleep(0.03)
            func()
        return typewriter
    return writer


def player_progress():
    if player1.completion < 1:
        player1.location = 'Scenario'
    elif 1 > player1.completion < 2:
        player1.location = 'Dark Dungeon'
    elif 2 > player1.completion < 3:
        player1.location = 'Dark Tunnel'
    elif 3 > player1.completion < 4:
        player1.location = 'Beach'
    elif 4 > player1.completion < 5:
        player1.location = 'Hello Friend'


@typewriter_decorator(QUESTIONS['get_difficulty'])
def get_difficulty():
    player1.choice = input("> ")
    if player1.choice == 'cheetah':
        player1.difficulty = 270
        print(f'\n\x1B[3mYou have been granted {player1.difficulty} seconds to play the game\x1B[23m\n')
        threading.Thread(target=countdown).start()
        scenario.start_scenario()
    elif player1.choice == 'lion':
        player1.difficulty = 135
        print(f'\n\x1B[3mYou have been granted {player1.difficulty} seconds to play the game\x1B[23m\n')
        threading.Thread(target=countdown).start()
        scenario.start_scenario()
    else:
        print('Nothing happens..')
    get_difficulty()


def countdown():
    time.sleep(player1.difficulty)
    print('\n\x1B[3mYou have failed to defuse the reactor in time resulting in a worldwide catastrophe..\x1B[23m\n')
    os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)


@typewriter_decorator(QUESTIONS['get_name'])
def get_name():
    player1.name = input('> ')
    sys.stdout.write("Bonsoir, " + player1.name + "\n")


def good_ending():
    for element in CREDITS['good_ending']:
        sys.stdout.write(element)
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n')
    os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)


def generate_pressure():
    yield_str = '''
    \x1B[3mThe ceiling started to crack dropping a piece of debris..\x1B[23m
    \x1B[3mIt has destroyed the telephone.. luckily it wasn't you but that was very close..\x1B[23m
    '''
    yield yield_str
    yield_str = '\t\x1B[3mThe earth is trembling..and you hear loud sirens from outside the room..\x1B[23m\n'
    yield yield_str
    yield_str = '\t\x1B[3mThe room is shivering..and you hear screams from outside the room..\x1B[23m\n'
    yield yield_str
    yield_str = '\t\x1B[3mYou hear crackling explosions in the distance..\x1B[23m\n'
    yield yield_str


def time_pressure():
    string_object = generate_pressure()
    array = [False, False, False, False]
    while False in array:
        if player1.completion == 1 and array[0] is False:
            array[0] = True
            print(next(string_object))
        elif player1.completion == 1.5 and array[1] is False:
            array[1] = True
            print(next(string_object))
        elif player1.completion == 2 and array[2] is False:
            array[2] = True
            print(next(string_object))
        elif player1.completion == 2.5 and array[3] is False:
            array[3] = True
            print(next(string_object))


def start_game():
    title_screen()
    player_progress()
    scenario.start_scenario()


if __name__ == '__main__':
    threading.Thread(target=play_theme).start()
    game = threading.Thread(target=start_game).start()
    pressure = threading.Thread(target=time_pressure).start()
