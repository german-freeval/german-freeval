from german_freeval.macro.property import Property
from german_freeval.macro.segment import Segment


class Base(Segment):
    # infrastructure input
    length: Property
    lanes: Property
    slope: Property
    ballungsraum: Property  # TODO: Englisch?
    speedlimit: Property
    has_zra: Property

    # demand input
    demand: Property
    heavyvehicle_share: Property

    # model parameters
    capacity_factor: Property

    def __str__(self) -> str:
        return (
            self.__class__.__name__
            + super().__str__()
            #           + f"  length: {self.length}\n"
            #           + f"  lanes : {self.lanes}\n"
            #           + f"  speedlimit: {self.speedlimit}\n"
        )


class Source(Base):
    pass


class Drain(Base):
    pass


class Merging(Base):
    # infrastructure input
    type_onramp: Property
    speedlimit_onramp: Property

    # demand input
    demand_onramp: Property
    heavyvehicle_share_onramp: Property

    # model parameters
    capacity_factor_onramp: Property


class Diverging(Base):
    # infrastructure input
    type_offramp: Property
    speedlimit_offramp: Property

    # demand input
    demand_offramp: Property
    heavyvehicle_share_offramp: Property

    # model parameters
    capacity_factor_offramp: Property


class Weaving(Base):
    # infrastructure input
    type_onramp: Property
    speedlimit_onramp: Property
    type_offramp: Property
    speedlimit_offramp: Property

    # demand input
    demand_onramp: Property
    heavyvehicle_share_onramp: Property
    demand_offramp: Property
    heavyvehicle_share_offramp: Property

    # model parameters
    capacity_factor_onramp: Property
    capacity_factor_offramp: Property
