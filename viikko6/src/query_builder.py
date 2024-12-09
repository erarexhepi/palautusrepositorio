from matchers import And, Or, PlaysIn, HasAtLeast, HasFewerThan, All

class QueryBuilder:
    def __init__(self):
        self._matchers = []

    def plays_in(self, team):
        self._matchers.append(PlaysIn(team))
        return self

    def has_at_least(self, value, attribute):
        self._matchers.append(HasAtLeast(value, attribute))
        return self

    def has_fewer_than(self, value, attribute):
        self._matchers.append(HasFewerThan(value, attribute))
        return self

    def one_of(self, *matchers):
        self._matchers.append(Or(*matchers))
        return self

    def build(self):
        if not self._matchers:
            return All()
        return And(*self._matchers)
