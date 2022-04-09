from german_freeval.input.property_builder import PropertyBuilder
from german_freeval.macro.hbs_segments import Base, Drain, Merging, Source
from german_freeval.macro.segment_changer import SegmentChanger


class DummySegmentChanger(SegmentChanger):
    def __init__(self, n_periods: int) -> None:
        super().__init__(n_periods)

    def apply(self, segment: Base):
        capacity = []
        speed = []
        density = []

        match segment:
            case Source() | Drain():
                return
            case Merging():
                ramp_demand = []
            case _:
                ramp_demand = None

        for period in range(self.n_periods):
            capacity.append(self.compute_capacity(segment, period))
            speed.append(self.compute_freeflow_speed(segment, period))
            density.append(self.compute_jam_density(segment, period))

            if ramp_demand:
                ramp_demand.append(self.compute_demand_ramp(segment, period))

        jam_density = PropertyBuilder(
            name="jam_density", type="float", initial_values=density
        )
        capacity_hbs = PropertyBuilder(
            name="capacity_hbs", type="float", initial_values=capacity
        )
        freeflow_speed_hbs = PropertyBuilder(
            name="freeflow_speed_hbs", type="float", initial_values=speed
        )

        segment.capacity_hbs = capacity_hbs.build(self.n_periods)
        segment.freeflow_speed_hbs = freeflow_speed_hbs.build(self.n_periods)
        segment.jam_density = jam_density.build(self.n_periods)

        if ramp_demand:
            demand_onramp = PropertyBuilder(
                name="demand_onramp", type="float", initial_values=ramp_demand
            )
            segment.demand_onramp = demand_onramp.build(self.n_periods)

    def compute_capacity(self, segment: Base, period: int):
        return segment.lanes[period] * 2000

    def compute_freeflow_speed(self, segment: Base, period: int):
        return segment.speedlimit[period]

    def compute_jam_density(self, segment: Base, period: int):
        return segment.lanes[period] * 100

    def compute_demand_ramp(self, segment: Merging, period: int):
        incoming: Source = segment.ramp_in
        return incoming.demand[period]
