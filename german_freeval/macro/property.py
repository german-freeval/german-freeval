class Property:
    def __init__(self, name: str, type: str, values: list) -> None:
        self.name = name
        self.type = type
        self.values = values

    name: str
    type: str
    values: list

    def __getitem__(self, time: int):
        return self.values[time]
