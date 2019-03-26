from card import Card


class Deck(object):

    def __init__(self):
        self.cards = []
        self.suits = ['Heart', 'Diamond', 'Club', 'Spade']
        self.faces = ['Ace', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      '10', 'Jack', 'Queen', 'King']

    def initialize(self):
        # Initialize deck by creating cards and adding to list of cards
        pass

    def shuffle(self):
        # deck is shuffled
        pass

    def addCardtoDeck(self):
        # add single card to deck
        pass

    def addCardstoDeck(self):
        # add a small pile of card to deck
        pass

    def flipTopCard(self):
        # return top card from deck and remove from deck queue
        pass

    def cardMatchSequence(self):
        # both players matched cards, so need to return a small pile of
        # flipped cards

        # NOTE: The actions taken for card matchsequence is by the player, so
        #   maybe it shouldn't be implemented here
        pass
