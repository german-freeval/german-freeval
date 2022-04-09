from german_freeval.input.segmentbuilder import SegmentBuilder


class SegmentChanger:
    def __init__(self) -> None:
        pass

    def apply(self, segment_builder: SegmentBuilder):
        pass


class SegmentChangerHBS(SegmentChanger):
    def apply(self, segment_builder: SegmentBuilder):
        self.freeflow_speed_hbs(segment_builder)
        self.capacity_hbs(segment_builder)
        self.critical_density_hbs(segment_builder)

    def freeflow_speed_hbs(self, segment_builder: SegmentBuilder):
        pass

    def capacity_hbs(self, segment_builder: SegmentBuilder):
        pass

    def critical_density_hbs(self, segment_builder: SegmentBuilder):
        pass
