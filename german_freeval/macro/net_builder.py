from german_freeval.input.segment_builder import SegmentBuilder
from german_freeval.macro.net import Net
from german_freeval.macro.segment_changer import SegmentChanger
from german_freeval.meta.context import Context


class NetBuilder:

    segmentbuilders: list[SegmentBuilder]
    changers: list[SegmentChanger]
    context: Context

    def __init__(self, context) -> None:

        self.segmentbuilders = []
        self.changers = []
        self.context = context

    def add_segment(self, segment: SegmentBuilder):
        self.segmentbuilders.append(segment)

    def add_changer(self, changer: SegmentChanger):
        self.changers.append(changer)

    def set_n_periods(self, n_periods: int):
        self.n_periods = n_periods

    def build(self) -> Net:

        net = Net(self.context)

        for segmentbuilder in self.segmentbuilders:
            for changer in self.changers:
                changer.apply(segmentbuilder)
            net.add_segment(segmentbuilder.build(self.context.n_periods))

        return net
