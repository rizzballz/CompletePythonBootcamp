#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 21:56:19 2019

@author: Ryan McMillan
@title: playing_card_class.py
"""

class PlayingCard(object):
    '''
    Playing Card Class. 
    
    Attributes
    -----------
    self.value = Value of the playing card 2-10,JQKA
    self.suit = Suit of the playing card. Hearts, Diamonds, Spades, Clubs
    '''
    def __init__(self, value, suit):
        '''
        Initialisation method, value and suit must be passed on instantiation 
        of the object
        '''
        self.value = value
        self.suit = suit

import random        

# Constants for suits and values
SUITS = ['Hearts','Diamonds','Spades', 'Clubs']
VALUES = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

# Initialise an empty deck.
deck = []

# Iterate over each suit
for suit in SUITS:
    # Iterate over each value
    for val in VALUES:
        # Instantiate an instance of a Playing Card with the current 
        # Value and Suit.
        deck.append(PlayingCard(val,suit))
        
# Sanity check to ensure all cards have been created.
assert len(deck) == 52

# Shuffle the deck
random.shuffle(deck)

# Take the top card off the top of the deck
top_card = deck.pop()
# See what it is
print(top_card.value, top_card.suit)