from german_freeval.macro.property import Property


class Segment:
    id: int
    ramp_in: "Segment"
    base_in: "Segment"
    ramp_out: "Segment"
    base_out: "Segment"
    name: Property

    def __init__(self, id: int) -> None:
        self.id = id
        self.ramp_in = None
        self.base_in = None
        self.ramp_out = None
        self.base_out = None

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return (
            f"{self.id}[{self.name}]:\n"
            + f"  in: ({self.base_in.id if self.base_in else ''},"
            + f"{self.ramp_in.id if self.ramp_in else ''})\n"
            + f"  out:({self.base_out.id if self.base_out else ''},"
            + f"{self.ramp_out.id if self.ramp_out else ''})\n"
        )
