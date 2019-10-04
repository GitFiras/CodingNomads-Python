class Card:
    """Represents a standard playing card.
    Spades	↦	3
    Hearts	↦	2
    Diamonds	↦	1
    Clubs	↦	0

    Jack	↦	11
    Queen	↦	12
    King	↦	13
    """
    # inside class Card:

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

# inside class Card:

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit: return True
        if self.suit > other.suit: return False

        # suits are the same... check ranks
        return self.rank < other.rank

        # You can write this more concisely using tuple comparison:

# inside class Card:

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

queen_of_diamonds = Card(1, 12)


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    #Here is a __str__ method for Deck:
    #inside class Deck:
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    # This method demonstrates an efficient way to accumulate a large string: building a list of strings and then using the string method join. The built-in function str invokes the __str__ method on each card and returns the string representation.
    # Since we invoke join on a newline character, the cards are separated by newlines. Here’s what the result looks like:
    # >>> deck = Deck()
    # >>> print(deck)
    # Ace of Clubs
    # 2 of Clubs
    # 3 of Clubs
    # ...
    # 10 of Spades
    # Jack of Spades
    # Queen of Spades
    # King of Spades
    # Even though the result appears on 52 lines, it is one long string that contains newlines.


    #To deal cards, we would like a method that removes a card from the deck and returns it. The list method pop provides a convenient way to do that:
    #inside class Deck:

    def pop_card(self):
        return self.cards.pop()
    #Since pop removes the last card in the list, we are dealing from the bottom of the deck.

    #To add a card, we can use the list method append:
    #inside class Deck:

    def add_card(self, card):
        self.cards.append(card)

    import random
    # inside class Deck:
    def shuffle(self):
        random.shuffle(self.cards)

#inside class Deck:

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
# move_cards takes two arguments, a Hand object and the number of cards to deal.
# It modifies both self and hand, and returns None.
# In some games, cards are moved from one hand to another, or from a hand back to the deck.
# You can use move_cards for any of these operations:
# self can be either a Deck or a Hand, and hand, despite the name, can also be a Deck.

class Hand(Deck):
        """Represents a hand of playing cards."""
#If we provide an init method in the Hand class, it overrides the one in the Deck class:
# inside class Hand:

    def __init__(self, label=''):
        self.cards = []
        self.label = label
#When you create a Hand, Python invokes this init method, not the one in Deck.

# >>> hand = Hand('new hand')
# >>> hand.cards
# []
# >>> hand.label
# 'new hand'
# The other methods are inherited from Deck, so we can use pop_card and add_card to deal a card:

# >>> deck = Deck()
# >>> card = deck.pop_card()
# >>> hand.add_card(card)
# >>> print(hand)
# King of Spades