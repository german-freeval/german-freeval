from german_freeval.macro.hbs_segments import Base
from german_freeval.input.hbs_handler import HBSHandler
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
        self.check_hbs_property_builders(segment)
        freeflow_speed_hbs = []
        capacity_hbs = []
        jam_density = []
        for i_periods in range(len(segment.slope)):
            freeflow_speed_hbs.append(
                self.hbs_handler.hbs_freeflow_speed(
                    slope=segment.slope[i_periods],
                    heavy_vehicle_share=segment.heavy_vehicle_share[i_periods],
                    ballungsraum=segment.ballungsraum[i_periods],
                    has_zra=segment.has_zra[i_periods],
                    lanes=segment.lanes[i_periods],
                    speed_limit=segment.speed_limit[i_periods],
                )
            )
            capacity_hbs.append(
                self.hbs_handler.hbs_capacity(
                    slope=segment.slope[i_periods],
                    heavy_vehicle_share=segment.heavy_vehicle_share[i_periods],
                    ballungsraum=segment.ballungsraum[i_periods],
                    has_zra=segment.has_zra[i_periods],
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

        segment.freeflow_speed_hbs = Property(
            name="freeflow_speed_hbs", type="speed", values=freeflow_speed_hbs
        )
        segment.capacity_hbs = Property(
            name="capacity_hbs", type="capacity", values=capacity_hbs
        )
        segment.jam_density = Property(
            name="jam_density", type="density", values=jam_density
        )

    def check_hbs_property_builders(self, segment: Base):
        necessary_hbs_properties = [
            "slope",
            "heavy_vehicle_share",
            "ballungsraum",
            "has_zra",
            "lanes",
            "speed_limit",
        ]
        existing_attributes_segment = dir(segment)
        if set(necessary_hbs_properties).issubset(existing_attributes_segment):
            pass
        else:
            raise Exception(
                "segment does not contain all needed properties builders to calculate additional parameters"
            )
