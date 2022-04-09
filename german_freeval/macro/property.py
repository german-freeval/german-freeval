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

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        if len(set(self.values)) == 1:
            pass
        return (
            f"{self.name}[{self.type}]="
            + f"{[(v, self.values.index(v)) for v in set(self.values)]}"
        )
