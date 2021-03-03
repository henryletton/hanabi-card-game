'''
    File name: my_classes.py
    Author: Henry Letton
    Date created: 2021-03-03
    Python Version: 3.8.3
    Desciption: Defining object classes used in the game
'''

import random

# Possible colours and numbers for cards, with relative prevalence
colours = ['blue','white','green','yellow','red']
numbers = [1,1,1,2,2,3,3,4,4,5]

#%% Class for a card
class Card:
    """ Card class represents a card in the game. """
    
    def __init__(self, colour, number):
        """ Create card with given colour and value. """
        self.colour = colour
        self.number = number
        
    def __repr__(self):
        return f'<Card colour:{self.colour} number:{self.number}>'
    
    def __str__(self):
        """ When printed, we want the card information. """
        return f'Card: colour is {self.colour}, number is {self.number}'
        


#%% Class for the card deck
class Deck:
    """ Deck class represents the central deck of cards to draw from. """
    
    def __init__(self):
        """ Create deck with correct cards randomly shuffled. """
        cards = []
        for colour in colours:
            for number in numbers:
                cards.append(Card(colour, number))
        random.shuffle(cards)
        self.cards = cards
        self.size = len(self.cards)
        
    def __repr__(self):
        return f'<Deck size:{self.size}>'
    
    def __str__(self):
        """ When printed, we want the deck information and card information. """
        print_lines = f'Deck: contains {self.size} cards'
        card_num = 1
        for card in self.cards:
            new_line = f'\nCard {card_num}: colour is {card.colour}, number is {card.number}'
            print_lines = print_lines + new_line
            card_num += 1
        return print_lines
    

#%% Class for the discard pile


#%% Class for a player


#%% Class for bomb
class Bomb:
    """ Bomb class to represent wrong guess countdown. """
    
    def __init__(self):
        """ Create bomb with 2 safe guesses, 1 unsafe. """
        self.fuse_length = 3
        self.blown = False
        
    def __repr__(self):
        return f'<Bomb fuse_length:{self.fuse_length}, blown:{self.blown}>'
    
    def __str__(self):
        """ When printed, we want the Bomb information. """
        if self.blown:
            blown_text = 'bomb has blown'
        else:
            blown_text = 'bomb has not blown'
        return f'Bomb: fuse_length is {self.fuse_length}, {blown_text}'
        
    def wrong_guess(self):
        """ Each wrong guess reduces the fuse length. """
        self.fuse_length -= 1
        if self.fuse_length < 1:
            self.blown = True

#%% Class for firework piles
class BlueTokens:
    """ BlueTokens class to represent remaining clues. """
    
    def __init__(self):
        """ Create BlueTokens with 8 guesses, the maximm. """
        self.clues = 8
        self.can_give_clue = True
        self.can_discard = False
        
    def __repr__(self):
        return f'<BlueTokens clues:{self.clues}, can_give_clue:{self.can_give_clue}, can_discard:{self.can_discard}>'
    
    def __str__(self):
        """ When printed, we want the BlueTokens information. """
        if not self.can_give_clue:
            restict_text = ', no clues left to give'
        elif not self.can_discard:
            restict_text = ', full clues so no discarding'
        else:
            restict_text = ''
        return f'BlueTokens: {self.clues} clues{restict_text}'
        
    def give_clue(self):
        """ Each clue uses up a token. """
        self.clues -= 1
        if self.clues < 1:
            self.can_give_clue = False
        if self.clues < 8:
            self.can_discard = True

    def get_clue(self):
        """ Discarding a card gives a token. """
        self.clues += 1
        if self.clues > 0:
            self.can_give_clue = True
        if self.clues > 7:
            self.can_discard = False

#%% Class for clues


