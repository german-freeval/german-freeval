import unittest

from german_freeval.macro.net_builder import NetBuilder
from german_freeval.meta.context import Context


class NetBuilderTest(unittest.TestCase):
    def test_net_builder(self):
        context = Context.create_from("tests/resources/config.yaml")
        net_builder = NetBuilder(context=context)
        print(context.segment_builders)
        for segment in context.segment_builders:
            net_builder.add_segment(segment)

        net = net_builder.build()
        print(net)
        assert len(net.segments) == 6

        segments = {s.id: s for s in net.segments}
        assert segments[1].base_in is None
        assert segments[1].ramp_in is None
        assert segments[1].base_out == segments[2]
        assert segments[1].ramp_out is None

        assert segments[2].base_in == segments[1]
        assert segments[2].ramp_in is None
        assert segments[2].base_out == segments[24]
        assert segments[2].ramp_out == segments[3]

        assert segments[24].base_in == segments[2]
        assert segments[24].ramp_in is None
        assert segments[24].base_out == segments[42]
        assert segments[24].ramp_out is None

        assert segments[3].base_in == segments[2]
        assert segments[3].ramp_in is None
        assert segments[3].base_out == segments[42]
        assert segments[3].ramp_out is None

        assert segments[42].base_in == segments[24]
        assert segments[42].ramp_in == segments[3]
        assert segments[42].base_out == segments[100]
        assert segments[24].ramp_out is None

        assert segments[100].base_in == segments[42]
        assert segments[100].ramp_in is None
        assert segments[100].base_out is None
        assert segments[100].ramp_out is None
