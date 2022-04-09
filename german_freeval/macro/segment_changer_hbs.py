from german_freeval.input.hbs_handler import HBSHandler
from german_freeval.input.property_builder import PropertyBuilder
from german_freeval.macro.hbs_segments import Base
from german_freeval.macro.segment_changer import SegmentChanger


class SegmentChangerHBS(SegmentChanger):
    def __init__(self, n_periods: int, hbs_handler: HBSHandler = None) -> None:
        super().__init__(n_periods)
        if hbs_handler:
            self.hbs_handler = hbs_handler
        else:
            self.hbs_handler = HBSHandler()

    def apply(self, segment: Base):
        self.check_hbs_properties(segment)
        freeflow_speed_hbs = []
        capacity_hbs = []
        jam_density = []
        for i_periods in range(len(segment.slope)):
            freeflow_speed_hbs.append(
                self.hbs_handler.hbs_freeflow_speed(
                    slope=segment.slope[i_periods],
                    heavy_vehicle_share=segment.heavy_vehicle_share[i_periods],
                    is_urban=segment.is_urban[i_periods],
                    has_rampmeter=segment.has_rampmeter[i_periods],
                    lanes=segment.lanes[i_periods],
                    speed_limit=segment.speed_limit[i_periods],
                )
            )
            capacity_hbs.append(
                self.hbs_handler.hbs_capacity(
                    slope=segment.slope[i_periods],
                    heavy_vehicle_share=segment.heavy_vehicle_share[i_periods],
                    is_urban=segment.is_urban[i_periods],
                    has_rampmeter=segment.has_rampmeter[i_periods],
                    lanes=segment.lanes[i_periods],
                    speed_limit=segment.speed_limit[i_periods],
                )
            )
            jam_density.append(
                self.hbs_handler.hbs_jam_density(
                    lanes=segment.lanes[i_periods],
                    heavy_vehicle_share=segment.heavy_vehicle_share[i_periods],
                )
            )

        segment.freeflow_speed_hbs = PropertyBuilder(
            name="freeflow_speed_hbs", type="speed", initial_values=freeflow_speed_hbs
        ).build(self.n_periods)
        segment.capacity_hbs = PropertyBuilder(
            name="capacity_hbs", type="capacity", initial_values=capacity_hbs
        ).build(self.n_periods)
        segment.jam_density = PropertyBuilder(
            name="jam_density", type="density", initial_values=jam_density
        ).build(self.n_periods)

    def check_hbs_properties(self, segment: Base):
        necessary_hbs_properties = [
            "slope",
            "heavy_vehicle_share",
            "is_urban",
            "has_rampmeter",
            "lanes",
            "speed_limit",
        ]
        existing_attributes_segment = dir(segment)
        if not set(necessary_hbs_properties).issubset(existing_attributes_segment):
            raise ValueError(
                "segment does not contain all needed properties builders to \
                 calculate additional parameters"
            )
