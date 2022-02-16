"""
Problem:

7.1 Deck of Cards: Design the data structures for a generic deck of cards. Explain how you would
subclass the data structures to implement blackjack.

Hints:#153, #275

--

Questions:

- What cards are in a deck? How many?
- Should we consider the deck with or without the jokers? How many jokers?
- What are the rules of black jack?
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

BlackjackGame
- Receives a deck of cards
- Receives players/hands
- Deal card to player/hand
- Players each have a hand
- Players bet money and win or lose from the table
- We can consider that each player is a hand

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

    def value(self):
        return self.rank.value


class DeckFactory:
    @classmethod
    def create_standard_deck(cls):
        ranks = [rank for rank in Rank]
        suits = [suit for suit in Suit]

        cards = []
        for rank in ranks:
            for suit in suits:
                new_card = Card(suit, rank)
                cards.append(new_card)

        return Deck(cards)

    @classmethod
    def create_black_jack_deck(cls):
        ranks = [rank for rank in Rank]
        suits = [suit for suit in Suit]

        cards = []
        for rank in ranks:
            for suit in suits:
                new_card = BlackjackCard(suit, rank)
                cards.append(new_card)

        return Deck(cards)


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def score(self):
        score = 0
        for card in self.cards:
            score += card.value()

        return score


class BlackjackCard(Card):
    def __init__(self, suit: Suit, rank: Rank):
        super().__init__(suit, rank)

    def value(self):
        if self.rank == Rank.ACE:
            return 1
        elif self.rank.value >= 10:
            return 10
        else:
            return self.rank.value

    def min_value(self):
        if self.rank == Rank.ACE:
            return 1
        else:
            return self.value()

    def max_value(self):
        if self.rank == Rank.ACE:
            return 11
        else:
            return self.value()


class BlackjackHand(Hand):
    def __init__(self):
        super().__init__()

    def score(self):
        scores = self.possible_scores()

        min_over = float("+inf")
        max_under = float("-inf")
        for score in scores:
            if score > 21 and score < min_over:
                min_over = score
            elif score <= 21 and score > max_under:
                max_under = score

        return max_under if max_under != float("-inf") else min_over

    """
    We can have more than 1 ace in hand, giving us many possibilities.

    Let's say we receive an Ace:
    [1, 11] -> we have two possibilities.

    If we receive a 3, we then have to sum 3 to both possibilities:
    [4, 14]

    Now, if we receive another Ace, we have to split all possible values
    we already have.
    [4,    14]
    / \    / \
   +1 +11 +1 +11

   So, every time we get a new card, we have to iterate over all the possible
   scores we have and add this new value. If this new card also has a min_value
   and a max_value, we have to append this new possibility with every possibility we have.
    """

    def possible_scores(self):
        scores = []
        for card in self.cards:
            self.add_card_to_score_list(card, scores)

        return scores

    def add_card_to_score_list(self, card, scores):
        if len(scores) == 0:
            scores.append(0)

        for i, score in enumerate(scores[:]):
            scores[i] = score + card.min_value()
            if card.min_value() != card.max_value():
                scores.append(score + card.max_value())


if __name__ == "__main__":
    deck = DeckFactory.create_standard_deck()
    hand = Hand()
    for card in deck.cards[:3]:
        hand.add_card(card)

    print(hand.score())

    blackjack_deck = DeckFactory.create_black_jack_deck()
    blackjack_hand = BlackjackHand()

    blackjack_deck.shuffle()
    for card in blackjack_deck.cards[:3]:
        blackjack_hand.add_card(card)

    print(blackjack_hand.score())
