from player import player
from deck import Deck


class GameState(object):

    def __init__(self):
        self.player_1 = Player("player-1")
        self.player_2 = Player("player-2")
        self.deck = Deck()
        self.deck.initializeDeck()
