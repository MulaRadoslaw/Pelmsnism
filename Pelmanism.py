# PELMANISM

# board
# display
# play game
# handle a turn
# check win
# scoring
# flip player

import random
import time
import os

print("Welcome to Pelmanism!\n")

card1 = 0
card2 = 0

# If game still going
game_still_going = True

# Who win
winner = None


# Creating players
class Player:

    def __init__(self, name):
        self.name = name

# Players names

player1 = Player(input("Player1 name: ").capitalize())
player2 = Player(input("Player2 name: ").capitalize())

# Whos turn is it?
current_player = player2.name

# Players points
player1.name_points = 0
player2.name_points = 0

# Game board

l = ['[AA]', '[AA]', '[BB]', '[BB]', '[CC]', '[CC]', '[DD]', '[DD]', '[EE]', '[EE]', '[FF]',
     '[FF]', '[GG]', '[GG]', '[HH]', '[HH]', '[II]', '[II]', '[JJ]', '[JJ]', '[KK]', '[KK]',
     '[LL]', '[LL]', '[MM]', '[MM]', '[NN]', '[NN]', '[OO]', '[OO]', '[PP]', '[PP]', '[QQ]',
     '[QQ]', '[RR]', '[RR]', '[SS]', '[SS]', '[TT]', '[TT]', '[UU]', '[UU]', '[VV]', '[VV]',
     '[WW]', '[WW]', '[XX]', '[XX]', '[YY]', '[YY]', '[ZZ]', '[ZZ]',
     ]
random.shuffle(l)

def display_board():
    print("     " + Board.board[1][0], Board.board[2][0], Board.board[3][0], Board.board[4][0], Board.board[5][0],
          Board.board[6][0])
    print(Board.board[7][0], Board.board[8][0], Board.board[9][0], Board.board[10][0], Board.board[11][0],
          Board.board[12][0], Board.board[13][0], Board.board[14][0])
    print(Board.board[15][0], Board.board[16][0], Board.board[17][0], Board.board[18][0], Board.board[19][0],
          Board.board[20][0], Board.board[21][0], Board.board[22][0])
    print(Board.board[23][0], Board.board[24][0], Board.board[25][0], Board.board[26][0], Board.board[27][0],
          Board.board[28][0], Board.board[29][0], Board.board[30][0])
    print(Board.board[31][0], Board.board[32][0], Board.board[33][0], Board.board[34][0], Board.board[35][0],
          Board.board[36][0], Board.board[37][0], Board.board[38][0])
    print(Board.board[39][0], Board.board[40][0], Board.board[41][0], Board.board[42][0], Board.board[43][0],
          Board.board[44][0], Board.board[45][0], Board.board[46][0])
    print("     " + Board.board[47][0], Board.board[48][0], Board.board[49][0], Board.board[50][0],
          Board.board[51][0], Board.board[52][0])

class Board:
    number_of_cards = 52

    board = {1: ['[01]', '[]'], 2: ['[02]', '[]'], 3: ['[03]', '[]'], 4: ['[04]', '[]'], 5: ['[05]', '[]'],
             6: ['[06]', '[]'], 7: ['[07]', '[]'], 8: ['[08]', '[]'], 9: ['[09]', '[]'], 10: ['[10]', '[]'],
             11: ['[11]', '[]'], 12: ['[12]', '[]'], 13: ['[13]', '[]'], 14: ['[14]', '[]'], 15: ['[15]', '[]'],
             16: ['[16]', '[]'], 17: ['[17]', '[]'], 18: ['[18]', '[]'], 19: ['[19]', '[]'], 20: ['[20]', '[]'],
             21: ['[21]', '[]'], 22: ['[22]', '[]'], 23: ['[23]', '[]'], 24: ['[24]', '[]'], 25: ['[25]', '[]'],
             26: ['[26]', '[]'], 27: ['[27]', '[]'], 28: ['[28]', '[]'], 29: ['[29]', '[]'], 30: ['[30]', '[]'],
             31: ['[31]', '[]'], 32: ['[32]', '[]'], 33: ['[33]', '[]'], 34: ['[34]', '[]'], 35: ['[35]', '[]'],
             36: ['[36]', '[]'], 37: ['[37]', '[]'], 38: ['[38]', '[]'], 39: ['[39]', '[]'], 40: ['[40]', '[]'],
             41: ['[41]', '[]'], 42: ['[42]', '[]'], 43: ['[43]', '[]'], 44: ['[44]', '[]'], 45: ['[45]', '[]'],
             46: ['[46]', '[]'], 47: ['[47]', '[]'], 48: ['[48]', '[]'], 49: ['[49]', '[]'], 50: ['[50]', '[]'],
             51: ['[51]', '[]'], 52: ['[52]', '[]']}

    x = 1
    while x <= number_of_cards:
        board[x][1] = l[x - 1]
        x += 1

    @classmethod
    def cards_count(cls):
        return cls.number_of_cards

    @classmethod
    def remove_cards(cls):
        cls.number_of_cards -= 2


def play_game():
    while game_still_going:
        # Handle turn of an arbitary player
        handle_turn_1(current_player)
        handle_turn_2()
        
        print(f"Your cards: {Board.board[card1][1]}, {Board.board[card2][1]}")
        time.sleep(1)

        # Scoring system
        getting_a_points()
        time.sleep(2)
        
        # Screen clear
        os.system('cls')
        
        # Cleaning
        deleting_cards()

        # Checking for winner
        check_if_game_over()

def handle_turn_1(current_player):
    global card1
    global returned_card1
    display_board()
    print(f"Now is {current_player}'s turn.")
    card1 = ""
    valid = False
    while not valid:
        while card1 not in Board.board.keys():
            try:
                card1 = int(input("Choose a card between 1 and 52: "))

            except ValueError:
                pass

        returned_card1 = Board.board[card1][1]

        if Board.board[card1][0] != '--':
            valid = True
        else:
            print("Card already taken.")
        print(returned_card1)
        return card1
        return returned_card1

def handle_turn_2():
    global card1
    global card2
    global returned_card2
    valid = False
    card2 = ""
    while not valid:
        while card2 not in Board.board.keys() or card2 == card1:
            try:
                card2 = int(input(f"Choose a card, except {card1}, between 1 and 52: "))

            except ValueError:
                pass
        returned_card2 = Board.board[card2][1]
        if Board.board[card2][0] != '--':
            valid = True
        else:
            print("Card already taken.")
        print(returned_card2)
        return card2
        return returned_card2

def deleting_cards():
    if returned_card1 == returned_card2:
        Board.board[card1][0] = "[--]"
        Board.board[card2][0] = "[--]"

def getting_a_points():
    global player1_points
    global player2_points
    global card1
    global card2
    if Board.board[card1][1] == Board.board[card2][1]:

        if current_player == player1.name:
            player1.name_points += 2
            deleting_cards()
            Board.remove_cards()

        elif current_player == player2.name:
            player2.name_points += 2
            deleting_cards()
            Board.remove_cards()
    else:
        print("Wrong")
        flip_player()
    print(f"\n{player1.name} have", player1.name_points, "points")
    print(f"{player2.name} have", player2.name_points, "points\n")

def check_if_game_over():
    if Board.number_of_cards == 0:
        check_for_winner()

def check_for_winner():
    global game_still_going
    global winner
    if player1.name_points > player2.name_points:
        winner = player1.name
        game_still_going = False
    else:
        winner = player2.name
        game_still_going = False
    print(winner + " won!")

def flip_player():
    global current_player
    if current_player == player1.name:
        current_player = player2.name
    elif current_player == player2.name:
        current_player = player1.name
    return

play_game()
