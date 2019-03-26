from deck import Deck


class Player(object):

    def __init__(self, player_name):
        self.name = player_name
        self.inplay_cards = []
        self.__deck = Deck()

    def addNewCards(self):
        # add to deck
        pass

    def cardMatched():
        # both players flipped same card, so follow the protocol
        pass

    def addToInplayCards(self):
        # to keep track of what's been played
        pass
