from library import *

if __name__ == '__main__':
    cards = [x for x in range(1, 10) for i in range(4)] + [10] * 16
    ptotal, dtotal = BjTotal(10, 10), BjTotal(10)
    print(calodds(cards, ptotal, dtotal))
    pass
