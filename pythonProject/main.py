#exercise 1
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __int__(self):
        return int(self.amount)

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
            else:
                raise TypeError(f"Cannot add between Currency type {self.currency} and {other.currency}")
        else:
            return NotImplemented
        return self

    def __repr__(self):
        return f"{self.__class__.__name__} : {self.amount} {self.currency}"

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)
int(c1)
repr(c1)
c1 + 5
c1 + c2
c1
c1 += 5
c1
c1 += c2
c1
c1 + c3
