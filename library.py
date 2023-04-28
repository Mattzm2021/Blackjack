from enum import Enum
import copy


class BjTotal:
    def __init__(self, cards: list[int]) -> None:
        self.cards = cards
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


class BjOdds:
    def __init__(self, win: float, tie: float, lose: float) -> None:
        self.win = win
        self.tie = tie
        self.lose = lose
        self.expvalue = self.calexpvalue()

    def __str__(self) -> str:
        _str = f'Win: {self.win}, Tie: {self.tie}, Lose: {self.lose}'
        return _str + f'\nExpected Value: {self.expvalue}'

    def calexpvalue(self) -> float:
        return self.win - self.lose


class BjOddsCol(Enum):
    WIN = BjOdds(1, 0, 0)
    TIE = BjOdds(0, 1, 0)
    LOSE = BjOdds(0, 0, 1)


def calodds(cards: list[int], ptotal: BjTotal, dtotal: BjTotal) -> list[BjOdds]:
    odds = [calodds_s(cards, ptotal, dtotal)]
    return odds


def calodds_s(cards: list[int], ptotal: BjTotal, dtotal: BjTotal) -> BjOdds:
    if dtotal.isbj() and ptotal.isbj():
        return BjOddsCol.TIE.value
    elif dtotal.isbj():
        return BjOddsCol.LOSE.value
    elif ptotal.isbj():
        return BjOddsCol.WIN.value
    elif ptotal.isbust():
        return BjOddsCol.LOSE.value
    elif dtotal.isbust():
        return BjOddsCol.WIN.value
    elif dtotal.total >= 17:
        if dtotal.total > ptotal.total:
            return BjOddsCol.LOSE.value
        elif dtotal.total == ptotal.total:
            return BjOddsCol.TIE.value
        else:
            return BjOddsCol.WIN.value
    win = tie = lose = 0
    for i in range(1, 11):
        if i not in cards:
            continue
        cardsdup = cards.copy()
        cardsdup.remove(i)
        dtotaldup = copy.deepcopy(dtotal)
        dtotaldup.add(i)
        odds = calodds_s(cardsdup, ptotal, dtotaldup)
        win += odds.win * cards.count(i) / len(cards)
        tie += odds.tie * cards.count(i) / len(cards)
        lose += odds.lose * cards.count(i) / len(cards)
    return BjOdds(win, tie, lose)
