from german_freeval.macro.property import Property
from german_freeval.macro.segment import Segment


class Base(Segment):
    # infrastructure input
    length: Property
    lanes: Property
    slope: Property
    is_urban: Property
    speedlimit: Property
    has_rampmeter: Property

    # demand input
    demand: Property
    heavyvehicle_share: Property

    # model parameters
    capacity_factor: Property

    # ctm parameters
    freeflow_speed_hbs: Property
    capacity_hbs: Property
    jam_density: Property


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
