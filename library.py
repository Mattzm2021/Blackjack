import random
import copy


class BjTotal:
    def __init__(self, *cards: int) -> None:
        self.cards = list(cards)
        self.soft = 1 in cards and sum(cards) <= 11
        self.total = sum(cards) + (10 if self.soft else 0)

    def __str__(self) -> str:
        _str = 'Total = '
        _str += f'{self.total - 10} / {self.total}' if self.soft else f'{self.total}'
        return _str + f' ; {self.cards}'

    def add(self, card: int) -> None:
        self.cards.append(card)
        self.total += card
        if self.total > 21 and self.soft:
            self.total -= 10
            self.soft = False
        elif self.total <= 11 and card == 1:
            self.total += 10
            self.soft = True

    def is21(self) -> bool:
        return self.total == 21

    def isbj(self) -> bool:
        return self.is21() and self.soft

    def isbust(self) -> bool:
        return self.total > 21 and not self.soft


def calodds(cards: list[int], ptotal: BjTotal, dtotal: BjTotal) -> tuple[float, float, float]:
    if dtotal.isbj() and ptotal.isbj():
        return 0, 1, 0
    elif dtotal.isbj():
        return 0, 0, 1
    elif ptotal.isbj():
        return 1, 0, 0
    elif ptotal.isbust():
        return 0, 0, 1
    elif dtotal.isbust():
        return 1, 0, 0
    elif dtotal.total >= 17:
        if dtotal.total > ptotal.total:
            return 0, 0, 1
        elif dtotal.total == ptotal.total:
            return 0, 1, 0
        else:
            return 1, 0, 0
    win = tie = lose = 0
    for i in range(1, 11):
        if i not in cards:
            continue
        cardsdup = cards.copy()
        cardsdup.remove(i)
        dtotaldup = copy.deepcopy(dtotal)
        dtotaldup.add(i)
        odds = calodds(cardsdup, ptotal, dtotaldup)
        win += odds[0] * cards.count(i) / len(cards)
        tie += odds[1] * cards.count(i) / len(cards)
        lose += odds[2] * cards.count(i) / len(cards)
    return win, tie, lose
