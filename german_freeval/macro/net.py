from german_freeval.macro.segment import Segment
from german_freeval.meta.context import Context


class Net:

    segments: list(Segment)
    context: Context

    def __init__(self, context: Context) -> None:
        self.context = context
        self.segments = []

    def add_segment(self, segment: Segment):
        self.segments.append(segment)
