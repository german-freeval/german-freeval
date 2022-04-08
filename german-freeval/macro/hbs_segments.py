from macro.segment import Segment
from macro.attribute import Attribute


class Base(Segment):
    # infrastructure input
    length: Attribute
    lanes: Attribute
    slope: Attribute
    ballungsraum: Attribute  # TODO: Englisch?
    speedlimit: Attribute
    has_zra: Attribute

    # demand input
    demand: Attribute
    heavyvehicle_share: Attribute

    # model parameters
    capacity_factor: Attribute


class Merging(Base):
    # infrastructure input
    type_onramp: Attribute
    speedlimit_onramp: Attribute

    # demand input
    demand_onramp: Attribute
    heavyvehicle_share_onramp: Attribute

    # model parameters
    capacity_factor_onramp: Attribute


class Diverging(Base):
    # infrastructure input
    type_offramp: Attribute
    speedlimit_offramp: Attribute

    # demand input
    demand_offramp: Attribute
    heavyvehicle_share_offramp: Attribute

    # model parameters
    capacity_factor_offramp: Attribute


class Weaving(Base):
    # infrastructure input
    type_onramp: Attribute
    speedlimit_onramp: Attribute
    type_offramp: Attribute
    speedlimit_offramp: Attribute

    # demand input
    demand_onramp: Attribute
    heavyvehicle_share_onramp: Attribute
    demand_offramp: Attribute
    heavyvehicle_share_offramp: Attribute

    # model parameters
    capacity_factor_onramp: Attribute
