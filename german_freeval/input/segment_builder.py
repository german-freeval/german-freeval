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
from german_freeval.macro.segment import Segment


class SegmentBuilder:

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
    build_result: Segment

    def __init__(self, id: int) -> None:
        self.id = id
        self.segments_in = {}
        self.segments_out = {}
        self.property_builders = []
        self.build_result = None

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
        if self.build_result:
            return self.build_result

        self.build_result: Segment = self.segment_types[
             (len(self.segments_in), len(self.segments_out))
        ](id=self.id)

        for property_builder in self.property_builders:
            setattr(self.build_result, property_builder.name, property_builder.build())

        base_in = self.segments_in.get("base")
        ramp_in = self.segments_in.get("ramp")
        base_out = self.segments_out.get("base")
        ramp_out = self.segments_out.get("ramp")

        if base_in:
            self.build_result.base_in = base_in.build()
        if base_out:
            self.build_result.base_out = base_out.build()
        if ramp_in:
            self.build_result.ramp_in = ramp_in.build()
        if ramp_out:
            self.build_result.ramp_out = ramp_out.build()

        return self.build_result

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
