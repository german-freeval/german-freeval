import unittest

from german_freeval.input.property_builder import PropertyBuilder
from german_freeval.input.segment_builder import SegmentBuilder
from german_freeval.macro.segment import Segment


class SegmentBuilderTest(unittest.TestCase):
    def test_segment_builder_id(self):
        print("hi")

        builder = SegmentBuilder(17)
        assert builder.id == 17

    def test_segment_builder_build(self):
        builder_in = SegmentBuilder(1)
        builder_main = SegmentBuilder(2)
        builder_out = SegmentBuilder(3)

        builder_in.add_property(PropertyBuilder("name", "str", "alpha"))
        builder_main.add_property(PropertyBuilder("name", "str", "beta"))
        builder_out.add_property(PropertyBuilder("name", "str", "gamma"))

        builder_main.add_predecessor(builder_in, "base")
        builder_main.add_successor(builder_out, "base")
        builder_in.add_successor(builder_main, "base")
        builder_out.add_predecessor(builder_main, "base")

        segment: Segment = builder_main.build(5)
        print(segment)

        assert segment.ramp_in is None
        assert segment.ramp_out is None

        assert segment.base_in is not None
        assert segment.base_out is not None

        segment_in = builder_in.build_result
        segment_out = builder_out.build_result

        assert segment_in == segment.base_in
        assert segment_out == segment.base_out
