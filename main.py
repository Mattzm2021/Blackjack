from alive_progress import alive_bar
from library import *
import statistics

if __name__ == '__main__':
    player_total, dealer_total = BlackjackTotal(20), BlackjackTotal(10)
    simulation = Simulation(1, player_total, dealer_total, [], Decision.STAND, 3)
    simulation.start()
