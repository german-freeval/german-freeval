from german_freeval.input.hbs_handler import HBSHandler
from german_freeval.macro.hbs_segments import Base
from german_freeval.macro.property import Property


class SegmentChanger:
    def __init__(self) -> None:
        pass

    def apply(self, segment: Base):
        pass


class SegmentChangerHBS(SegmentChanger):
    def __init__(self, hbs_handler: HBSHandler = None) -> None:
        super().__init__()
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
                    segment.slope[i_periods],
                    segment.heavy_vehicle_share[i_periods],
                    segment.is_urban[i_periods],
                    segment.has_rampmeter[i_periods],
                    segment.lanes[i_periods],
                    segment.speed_limit[i_periods],
                )
            )
            capacity_hbs.append(
                self.hbs_handler.hbs_capacity(
                    segment.slope[i_periods],
                    segment.heavy_vehicle_share[i_periods],
                    segment.is_urban[i_periods],
                    segment.has_rampmeter[i_periods],
                    segment.lanes[i_periods],
                    segment.speed_limit[i_periods],
                )
            )
            jam_density.append(
                self.hbs_handler.hbs_jam_density(
                    segment.lanes[i_periods],
                    segment.heavy_vehicle_share[i_periods],
                )
            )

        segment.freeflow_speed_hbs = Property(
            name="freeflow_speed_hbs", type="speed", values=freeflow_speed_hbs
        )
        segment.capacity_hbs = Property(
            name="capacity_hbs", type="capacity", values=capacity_hbs
        )
        segment.jam_density = Property(
            name="jam_density", type="density", values=jam_density
        )

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
