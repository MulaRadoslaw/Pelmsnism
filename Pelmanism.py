import random

card1 = 0
card2 = 0

game_still_going = True
# Create a cards
# Create a list
# assign a "random list" to cards

class Board:
    number_of_cards = 8

    board = {1: ['[01]', '[AA]'],2: ['[02]', '[AA]'],3: ['[03]', '[BB]'],4: ['[04]', '[BB]'],
             5: ['[05]', '[CC]'],6: ['[06]', '[CC]'],7: ['[07]', '[DD]'],8: ['[08]', '[DD]']}

    def __init__(self, name):
        self.name = name

    @classmethod
    def cards_count(cls):
        return cls.number_of_cards

    @classmethod
    def remove_cards(cls):
        cls.number_of_cards -= 1

def display_board():
        print(Board.board[1][0], Board.board[2][0], Board.board[3][0], Board.board[4][0])
        print(Board.board[5][0], Board.board[6][0], Board.board[7][0], Board.board[8][0])

# Local cards like ('[01]') swap to global and return back to local card.

returned_card1 = None
returned_card2 = None

def handle_turn_1():
    global card1
    global returned_card1
    card1 = int(input("Podaj 1 karte: "))
    if card1 in Board.board.keys():
        returned_card1 = Board.board[card1][1]
        print(Board.board[card1][1])
        return card1
        return returned_card1
def handle_turn_2():
    global card2
    global returned_card2
    card2 = int(input("Podaj 1 karte: "))
    if card2 in Board.board.keys():
        returned_card2 = Board.board[card2][1]
        print(Board.board[card2][1])

        return card2
        return returned_card2

def deleting_cards():
    if returned_card1 == returned_card2:
        Board.board[card1][0] = "[  ]"
        Board.board[card2][0] = "[  ]"
        Board.remove_cards()
        display_board()
    else:
        print(Board.board)

def game():
    global game_still_going
    display_board()
    while game_still_going:
        handle_turn_1()
        display_board()
        handle_turn_2()
        print(f"Your cards: {returned_card1}, {returned_card2}")
        deleting_cards()
        print(Board.number_of_cards)
        if Board.number_of_cards == 0:
            game_still_going = False

game()
