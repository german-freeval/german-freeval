class Attribute:
    def __init__(self, name: str, type: str, values: list) -> None:
        self.name = name
        self.type = type
        self.values = values
        
    name: str
    type: str
    values: list

    def getValue(self, time: int):
        return self.values[time]