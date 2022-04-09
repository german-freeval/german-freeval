from german_freeval.macro.property import Property
import numpy as np


class PropertyBuilder:
    name: str
    type: str
    values: dict

    def __init__(self, name: str, type: str, startvalue) -> None:
        self.name = name
        self.type = type
        self.values = {0: startvalue}

    def add_period_value(self, period: int, value):
        self.values[period] = value

    def get_value(self, period: int):
        periods = np.sort(self.values.keys())
        for i in range(len(periods)):
            if periods[i] - period > 0:
                key_period = periods[i - 1]
        return self.values[key_period]

    def build(self, n_periods: int):
        values = [0] * n_periods
        for p in sorted(self.values.keys()):
            values[p:] = [self.values[p]] * len(values[p:])

        property = Property(name=self.name, type=self.type, values=values)

        return property

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return "{}[{}]={}".format(self.name, self.type, self.values)
