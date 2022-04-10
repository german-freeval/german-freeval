from german_freeval.input.property_builder import PropertyBuilder
from german_freeval.macro.hbs_segments import Base, Drain, Merging, Source
from german_freeval.macro.segment_changer import SegmentChanger


class DummySegmentChanger(SegmentChanger):

    VEHICLES_PER_LANE_PER_KM = 100
    CAPACITY_PER_LANE = 2000

    def __init__(self, n_periods: int) -> None:
        super().__init__(n_periods)

    def apply(self, segment: Base):
        match segment:
            case Source() | Drain():
                return
            case Merging():
                self.compute_capacity(segment)
                self.compute_freeflow_speed(segment)
                self.compute_jam_density(segment)
                self.compute_demand_ramp(segment)
            case _:
                self.compute_capacity(segment)
                self.compute_freeflow_speed(segment)
                self.compute_jam_density(segment)

    def compute_capacity(self, segment: Base):
        capacity = [
            n_lanes * self.CAPACITY_PER_LANE for n_lanes in segment.lanes.values
        ]
        segment.capacity_hbs = PropertyBuilder(
            name="capacity_hbs", type="float", initial_values=capacity
        ).build(self.n_periods)

    def compute_freeflow_speed(self, segment: Base):
        segment.freeflow_speed_hbs = PropertyBuilder(
            name="freeflow_speed_hbs",
            type="float",
            initial_values=segment.speedlimit.values.copy(),
        ).build(self.n_periods)

    def compute_jam_density(self, segment: Base):
        density = [
            n_lanes * self.VEHICLES_PER_LANE_PER_KM for n_lanes in segment.lanes.values
        ]
        segment.jam_density = PropertyBuilder(
            name="jam_density", type="float", initial_values=density
        ).build(self.n_periods)

    def compute_demand_ramp(self, segment: Merging):
        incoming: Source = segment.ramp_in
        segment.demand_onramp = PropertyBuilder(
            name="demand_onramp",
            type="float",
            initial_values=incoming.demand.values.copy(),
        )
