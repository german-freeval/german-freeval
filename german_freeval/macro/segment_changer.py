from german_freeval.macro.segment import Segment


class SegmentChanger:

    n_periods: int

    def __init__(self, n_periods: int) -> None:
        self.n_periods = n_periods

    def apply(self, segment: Segment):
        pass
