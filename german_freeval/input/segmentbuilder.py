from german_freeval.macro.segment import Segment
from input.attributebuilder import AttributeBuilder
from macro.hbs_segments import Base, Merging, Diverging, Weaving, Source, Drain


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
            raise
        if self.segments_out[type]:
            raise
        else:
            self.segments_out[type] = successor

    def add_predecessor(self, predecessor: "SegmentBuilder", type: str):
        if type not in self.link_types:
            raise
        if self.segments_in[type]:
            raise
        else:
            self.segments_in[type] = predecessor

    def build(self):
        segment = self.segment_types[(len(self.segments_in), len(self.segments_out))](
            id=self.id, name="unnamed"
        )  # TODO: name noch als Attribut des Builders?

        for attribute_builder in self.attribute_builders:
            setattr(segment, attribute_builder.name, attribute_builder.build())

        return segment

    def __str__(self) -> str:
        return (
            str(self.id)
            + "[>"
            + ",".join(map(lambda s: str(s.id), self.segments_in))
            + "; "
            + ",".join(map(lambda s: str(s.id), self.segments_out))
            + ">]"
        )
