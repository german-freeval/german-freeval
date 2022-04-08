from macro.attribute import Attribute


class AttributeBuilder:
    name: str
    type: str
    values: dict

    def __init__(self, name: str, type: str, startvalue) -> None:
        self.name = name
        self.type = type
        self.values = {0: startvalue}

    def add_period_value(self, period: int, value):
        self.values[period] = value

    def build(self, n_periods: int):
        values = [0] * n_periods
        for p in sorted(self.values.keys()):
            values[p:] = [self.values[p]] * len(values[p:])

        attribute = Attribute(name=self.name, type=self.type, values=values)

        return attribute
