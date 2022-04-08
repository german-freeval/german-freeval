from attributebuilder import AttributeBuilder
class SegmentBuilder:
    def __init__(self, id: int) -> None:
        self.id = id
        self.segments_in = {}
        self.segments_out = {}
        self.attributes = []
        pass

    id: int
    segments_in: dict
    segments_out: dict
    attributes: list

    def add_attribute(self, new_attribute: AttributeBuilder):
        self.attributes.append(new_attribute)

    def has_attribute(self, attribute_name:AttributeBuilder):
        pass

    def add_successor(self, successor: "SegmentBuilder", index):
        if self.segments_out[index]:
            raise
        else:
            self.segments_out[index] = successor

    def add_predecessor(self, predecessor: "SegmentBuilder", index):
        if self.segments_in[index]:
            raise
        else:
            self.segments_in[index] = predecessor

    def build():
        pass
    
    def __str__(self) -> str:
        return str(self.id) + "[>" + ','.join(map(lambda s: str(s.id), self.segments_in))\
                            + "; " + ','.join(map(lambda s: str(s.id), self.segments_out)) + ">]"

