from alive_progress import alive_bar
from enum import Enum
import random


class Cards(Enum):
    DEUS = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    ACE = 9

    def __str__(self):
        return 

    def get_point(self):
        return 1 if self == Cards.ACE else self.value + 2

    def get_index(self):
        return self.value


class Decision(Enum):
    HIT = 0
    STAND = 1
    DOUBLE = 2
    SPLIT = 3


class BlackjackTotal:
    def __init__(self, total: int, is_soft: bool = False):
        self.total = total
        self.is_soft = is_soft

    def add(self, point: int):
        if point == 1 and self.total < 11:
            self.total += 11
            self.is_soft = True
            return

        self.total += point

        if self.total > 21 and self.is_soft:
            self.total -= 10
            self.is_soft = False

    def is_busted(self) -> bool:
        return self.total > 21 and not self.is_soft

    def is_blackjack(self) -> bool:
        return self.is_21() and self.is_soft

    def is_21(self) -> bool:
        return self.total == 21


class Simulation:
    blackjacks = busts = wins = ties = loses = []

    def __init__(self, deck_count: int, player_total: BlackjackTotal, dealer_total: BlackjackTotal,
                 certain_cards: list[Cards], player_decision, depth: int):
        self.deck_count = deck_count
        self.player_total = player_total
        self.dealer_total = dealer_total
        self.certain_cards = certain_cards
        self.player_decision = player_decision
        self.depth = depth

    def start(self):
        if self.player_total.is_blackjack():
            print('Simulation with player having blackjack is redundant')
            return

        print('Welcome to the blackjack odds simulator developed by Mattzm2023')
        print('Dealer\'s blackjack is INCLUDED within the odds')
        print('===============================================')
        print(generate_shuffled_cards(self.deck_count, self.certain_cards))
        # self.fill_data()

    def fill_data(self):
        with alive_bar(10 ** (self.depth * 2), force_tty=True) as bar:
            pass
        pass




def generate_shuffled_cards(deck_count: int, exceptions: list[Cards]) -> list[Cards]:
    card_counts = [deck_count * 4] * 8 + [deck_count * 16] + [deck_count * 4]
    deck = []

    for exception in exceptions:
        card_counts[exception.get_index()] -= 1

    for i in range(len(card_counts)):
        deck.extend([Cards(i)] * card_counts[i])

    random.shuffle(deck)
    return deck
