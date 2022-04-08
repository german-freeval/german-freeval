class AttributeBuilder:
    def __init__(self, name: str, type: str, startvalue) -> None:
        self.name = name
        self.type = type
        self.values = {0: startvalue}

    name: str
    type: str
    values: dict

    def insert(self, period: int, value):
        self.values[period] = value

    def build():
        pass
