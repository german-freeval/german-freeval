from msilib.schema import Error
from german_freeval.input.attributebuilder import AttributeBuilder
class SegmentBuilder:
    def __init__(self, id: int) -> None:
        self.id = id
        self.segments_in = {}
        self.segments_out = {}
        self.attribute_builders = []
        pass

    segment_types: list = ["ramp", "base"]
    id: int
    segments_in: dict
    segments_out: dict
    attribute_builders: list

    def add_attribute(self, new_attribute_builder: AttributeBuilder):
        self.attribute_builders.append(new_attribute_builder)

    def has_attribute(self, attribute_name:AttributeBuilder):
        pass

    def add_successor(self, successor: "SegmentBuilder", type: str):
        if type not in self.segment_types:
            raise Error("{} is not a valid type {}".format(type, self.segment_types))
        if type in self.segments_out:
            print(self.id, type, self.segments_out)
            raise Error("{} already exists in {}".format(type, self.segments_out))
        else:
            self.segments_out[type] = successor

    def add_predecessor(self, predecessor: "SegmentBuilder", type: str):
        if type not in self.segment_types:
            raise Error("{} is not a valid type {}".format(type, self.segment_types))
        if type in self.segments_in:
            print(self.segments_in)
            raise Error("{} already exists in {}".format(type, self.segments_in))
        else:
            self.segments_in[type] = predecessor

    def build(self):
        pass
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return str(self.id)

