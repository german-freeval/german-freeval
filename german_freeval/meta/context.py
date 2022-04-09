from typing import List
import yaml
from german_freeval.input.segment_parsers import CsvSegmentPropertyParser as Property
from german_freeval.input.segment_parsers import CsvSegmentTopologyParser as Topology
from german_freeval.input.segment_builder import SegmentBuilder


class Context:
    segment_builders: List[SegmentBuilder]
    n_periods: int

    def __init__(self) -> None:
        pass

    @classmethod
    def create_from(cls, file: str) -> "Context":
        context = Context()

        with open(file, "r") as stream:
            config = yaml.safe_load(stream)

        topology_path = config["topology"]
        properties_path = config["properties"]

        context.segment_builders = Topology.parse(file=topology_path)
        Property.parse(file=properties_path, segments=context.segment_builders)

        context.n_periods = config["periods"]

        return context
