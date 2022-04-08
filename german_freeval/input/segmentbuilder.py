from german_freeval.input.attributebuilder import AttributeBuilder
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
        self.attribute_builders = []
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
    segments_in: dict
    segments_out: dict
    attribute_builders: list

    def add_attribute(self, new_attribute_builder: AttributeBuilder):
        self.attribute_builders.append(new_attribute_builder)

    def has_attribute(self, attribute_name: AttributeBuilder):
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

        for attribute_builder in self.attribute_builders:
            setattr(segment, attribute_builder.name, attribute_builder.build())

        return segment

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return (
            str(self.id)
            + "[>"
            + ",".join(map(lambda s: str(s.id), self.segments_in))
            + "; "
            + ",".join(map(lambda s: str(s.id), self.segments_out))
            + ">]"
        )
