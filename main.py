from library import *
import sys

if __name__ == '__main__':
    print('\nWelcome to Blackjack odds simulator developed by Mattzm2023!')
    deck = int(input('Please enter the deck count: '))
    ecps = input('Please enter extra exceptions: ')
    ecps = [] if ecps == '' else [int(x) for x in ecps.split(' ')]
    player = [int(x) for x in input('Please enter player\'s cards: ').split(' ')]
    dealer = [int(x) for x in input('Please enter dealer\'s cards: ').split(' ')]
    cards = [x for x in range(1, 10) for i in range(4 * deck)] + [10] * deck * 16
    for card in ecps + player + dealer:
        cards.remove(card)
    ptotal, dtotal = BjTotal(player), BjTotal(dealer)
    if ptotal.isbj() and dtotal.cards != [1]:
        print('\nSimulation with player having blackjack and without insurance is redundant!')
        sys.exit(1)
    odds = calodds(cards, ptotal, dtotal)
    print(f'\nSuccessfully calculated the odds and the expected value:\n{odds[0]}')
