from typing import Any

from german_freeval.macro.property import Property


class PropertyBuilder:
    name: str
    type: str
    values: dict

    def __init__(self, name: str, type: str, initial_values: Any | list | dict) -> None:
        self.name = name
        self.type = type

        match initial_values:
            case list():
                self.values = {k: v for k, v in enumerate(initial_values)}
            case dict():
                self.values = initial_values.copy()
            case _:
                self.values = {0: initial_values}

    def add_period_value(self, period: int, value):
        self.values[period] = value

    def build(self, n_periods: int):
        values = [0] * n_periods
        for p in sorted(self.values.keys()):
            values[p:] = [self.values[p]] * len(values[p:])

        property = Property(name=self.name, type=self.type, values=values)

        return property

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.name}[{self.type}]={self.values}"
