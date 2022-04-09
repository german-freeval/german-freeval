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
