from typing import Dict, List
from german_freeval.input.property_builder import PropertyBuilder
from german_freeval.macro.hbs_segments import (
    Base,
    Diverging,
    Drain,
    Merging,
    Source,
    Weaving,
)


class SegmentBuilder:
    def __init__(self, id: int) -> None:
        self.id = id
        self.segments_in = {}
        self.segments_out = {}
        self.property_builders = []
        pass

    link_types: list = ["ramp", "base"]
    segment_types = {
        (1, 1): Base,
        (2, 1): Merging,
        (1, 2): Diverging,
        (2, 2): Weaving,
        (0, 1): Source,
        (1, 0): Drain,
    }
    id: int
    segments_in: Dict[str, "SegmentBuilder"]
    segments_out: Dict[str, "SegmentBuilder"]
    property_builders: List[PropertyBuilder]

    def add_property(self, new_property_builder: PropertyBuilder):
        self.property_builders.append(new_property_builder)

    def has_property(self, property_name: PropertyBuilder):
        pass

    def add_successor(self, successor: "SegmentBuilder", type: str):
        if type not in self.link_types:
            raise Exception(
                "{} is not a valid type {}".format(type, self.segment_types)
            )
        if type in self.segments_out:
            print(self.id, type, self.segments_out)
            raise Exception("{} already exists in {}".format(type, self.segments_out))
        else:
            self.segments_out[type] = successor

    def add_predecessor(self, predecessor: "SegmentBuilder", type: str):
        if type not in self.link_types:
            raise Exception(
                "{} is not a valid type {}".format(type, self.segment_types)
            )
        if type in self.segments_in:
            print(self.segments_in)
            raise Exception("{} already exists in {}".format(type, self.segments_in))
        else:
            self.segments_in[type] = predecessor

    def build(self):
        segment = self.segment_types[(len(self.segments_in), len(self.segments_out))](
            id=self.id, name="unnamed"
        )  # TODO: name noch als Attribut des Builders?

        for property_builder in self.property_builders:
            setattr(segment, property_builder.name, property_builder.build())

        return segment

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return (
            str(self.id)
            + "[>"
            + ",".join(map(lambda s: str(s.id), self.segments_in.values()))
            + "; "
            + ",".join(map(lambda s: str(s.id), self.segments_out.values()))
            + ">]"
        )
