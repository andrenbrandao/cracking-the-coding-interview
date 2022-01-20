"""
Problem:

7.1 Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack.

Hints:#153, #275

--

Questions:

- What cards are in a deck? How many?
- Should we consider the deck with or without the jokers? How many jokers?
- What the rules of black jack?
- What cards are available in the game?

--

Algorithm:

*1st Problem - Generic Deck of Cards*

Requirements
- 52 cards
- 4 suits: clubs, diamonds, hearts and spades
- 13 of each suit: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King
- Let's exclude the jokers

Design
- Deck with 52 cards
- Card is going to have a suit, rank, value
- Card belongs_to a Deck, Deck has_many Cards

*2nd Problem - Black Jack*

"""

"""
This would be the simplest way to implement a Card
However, it breaks encapsulation because anyone can try to insert
a suit or rank that is invalid.

"""


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value(rank)


"""
Another option would be to create an abstract class and create
Cards for each value and type. But this would end up creating
too many classes.
"""

from abc import ABC, abstractmethod


class AbstractCard(ABC):
    def __init__(self):
        self.suit = self.get_suit()
        self.value = self.get_value()

    @abstractmethod
    def get_value(self):
        pass

    @abstractmethod
    def get_suit(self):
        pass


class AceDiamondsCard(AbstractCard):
    def get_suit(self):
        return "diamonds"

    def get_value(self):
        return 1


"""
Another approach favoring composition over inheritance is to receive
a Suit and Rank enumerable.
"""

from enum import Enum, auto


class Suit(Enum):
    CLUBS = auto()
    HEARTS = auto()
    DIAMONDS = auto()
    SPADES = auto()


class Rank(Enum):
    ACE = auto()
    NUMBER2 = auto()
    NUMBER3 = auto()
    NUMBER4 = auto()
    NUMBER5 = auto()
    NUMBER6 = auto()
    NUMBER7 = auto()
    NUMBER8 = auto()
    NUMBER9 = auto()
    NUMBER10 = auto()
    JACK = auto()
    QUEEN = auto()
    KING = auto()


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank
        self.value = self.get_value(rank)


"""
Now, looking at it, taking the suit as an enumerable looks like a good solution.
However, with the rank, we would have to implement the get_value method
for the Card class considering all possible values. For this case,
creating a different class for each rank looks like a better approach.
"""

from enum import Enum, auto
from abc import ABC, abstractmethod
from typing import List


class Suit(Enum):
    CLUBS = "clubs"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    SPADES = "spades"


class AbstractCard(ABC):
    def __init__(self, suit: Suit):
        self.__suit = suit

    @abstractmethod
    def get_value(self):
        pass

    def get_suit(self):
        return self.__suit.value


class CardAce(AbstractCard):
    def get_value(self):
        return 1


class Card2(AbstractCard):
    def get_value(self):
        return 2


class Card3(AbstractCard):
    def get_value(self):
        return 3


class Card4(AbstractCard):
    def get_value(self):
        return 4


class Card5(AbstractCard):
    def get_value(self):
        return 5


class Card6(AbstractCard):
    def get_value(self):
        return 6


class Card7(AbstractCard):
    def get_value(self):
        return 7


class Card8(AbstractCard):
    def get_value(self):
        return 8


class Card9(AbstractCard):
    def get_value(self):
        return 9


class Card10(AbstractCard):
    def get_value(self):
        return 10


class CardJack(AbstractCard):
    def get_value(self):
        return 11


class CardQueen(AbstractCard):
    def get_value(self):
        return 12


class CardKing(AbstractCard):
    def get_value(self):
        return 13


"""
We also have to create the Deck of cards. It will receive a list of cards
and will have behaviours, such as:

- Shuffle
- Get card from the top of stack
- Insert card back to deck at the top
- Insert card back to deck at the bottom

"""

import random


class Deck:
    def __init__(self, cards: List[AbstractCard]):
        self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def get_top(self):
        if len(self.cards) == 0:
            raise Exception("Deck is empty")

        return self.cards.pop()

    def insert_at_top(self, card: AbstractCard):
        self.cards.append(card)

    def insert_at_bottom(self, card: AbstractCard):
        self.cards.insert(0, card)


"""
Now, to create a Deck, we would need a Factory, so that it knows exactly how to create
a specific Deck. Different games might need different types of decks.
"""


class DeckFactory:
    @classmethod
    def create_standard_deck(cls):
        ranks = [
            CardAce,
            Card2,
            Card3,
            Card4,
            Card5,
            Card6,
            Card7,
            Card8,
            Card9,
            Card10,
            CardJack,
            CardQueen,
            CardKing,
        ]
        suits = [Suit.DIAMONDS, Suit.HEARTS, Suit.SPADES, Suit.CLUBS]

        cards = []
        for rank in ranks:
            for suit in suits:
                new_card = rank(suit)
                cards.append(new_card)

        return cards


"""
In Blackjack, aces are worth 1 or 11 and face cards are 10.

Thinking about it, what the cards are worth is a game responsibility, not of the
card class. So, should we go back to the idea of creating a Card class and injecting
the rank? That way, the game can check the rank and make up their own rules for each card.

Having to subclass the AceCard just to change the value it represents will just make
our code more complicated.

Other classes we will need:

BlackJackGame
- Receives a deck of cards
- Receives players
- Deal card to player
- Players each have a hand

Hand
- Add a card
- Get Score

For the Blackjack specific game, a hand have different scores, because of
how the Ace card behaves. For that, we might want to subclass Hand.

BlackjackHand extends Hand
- Override get score to take care of aces
"""

from enum import Enum, auto
from abc import ABC, abstractmethod
from typing import List


class Suit(Enum):
    CLUBS = "clubs"
    HEARTS = "hearts"
    DIAMONDS = "diamonds"
    SPADES = "spades"


class Rank(Enum):
    ACE = 1
    NUMBER2 = 2
    NUMBER3 = 3
    NUMBER4 = 4
    NUMBER5 = 5
    NUMBER6 = 6
    NUMBER7 = 7
    NUMBER8 = 8
    NUMBER9 = 9
    NUMBER10 = 10
    JACK = 11
    QUEEN = 12
    KING = 13


class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit = suit
        self.rank = rank


if __name__ == "__main__":
    king_card = CardKing(Suit.DIAMONDS)
    print(king_card.get_value())
    print(king_card.get_suit())

    standard_deck = DeckFactory.create_standard_deck()
