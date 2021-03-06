import unittest

from german_freeval.input.segment_builder import SegmentBuilder
from german_freeval.input.segment_parsers import CsvSegmentPropertyParser as Properties
from german_freeval.input.segment_parsers import CsvSegmentTopologyParser as Topology


class SegmentParserTest(unittest.TestCase):
    def test_parse_topology(self):
        segments = Topology.parse("tests/resources/topology.csv")
        self.check_topology(segments)

    def test_parse_attributes(self):

        segments = Topology.parse("tests/resources/topology.csv")
        Properties.parse("tests/resources/properties.csv", segments)

        self.check_topology(segments)
        self.check_properties(segments)

    def check_topology(self, segments):
        assert len(segments) == 6

        map = {s.id: s for s in segments}
        b = "base"
        r = "ramp"

        assert len(map[1].segments_in) == 0
        assert map[1].segments_out[b].id == 2
        assert r not in map[1].segments_out

        assert map[2].segments_in[b].id == 1
        assert r not in map[2].segments_in
        assert map[2].segments_out[b].id == 24
        assert map[2].segments_out[r].id == 3

        assert map[24].segments_in[b].id == 2
        assert r not in map[24].segments_in
        assert map[24].segments_out[b].id == 42
        assert r not in map[24].segments_out

        assert map[3].segments_in[b].id == 2
        assert r not in map[3].segments_in
        assert map[3].segments_out[b].id == 42
        assert r not in map[3].segments_out

        assert map[42].segments_in[b].id == 24
        assert map[42].segments_in[r].id == 3
        assert map[42].segments_out[b].id == 100
        assert r not in map[42].segments_out

        assert map[100].segments_in[b].id == 42
        assert r not in map[100].segments_in
        assert len(map[100].segments_out) == 0

    def check_properties(self, segments: list[SegmentBuilder]):
        map = {s.id: s for s in segments}

        properties_1 = {a.name: a for a in map[1].property_builders}
        properties_2 = {a.name: a for a in map[2].property_builders}
        properties_24 = {a.name: a for a in map[24].property_builders}
        properties_3 = {a.name: a for a in map[3].property_builders}
        properties_42 = {a.name: a for a in map[42].property_builders}
        properties_100 = {a.name: a for a in map[100].property_builders}

        assert properties_1["name"].values[0] == "alpha"
        assert properties_2["name"].values[0] == "beta"
        assert properties_24["name"].values[0] == "gamma"
        assert properties_3["name"].values[0] == "delta"
        assert properties_42["name"].values[0] == "epsilon"
        assert properties_100["name"].values[0] == "zeta"

        assert len(properties_1["name"].values) == 1
        assert len(properties_2["name"].values) == 1
        assert len(properties_24["name"].values) == 1
        assert len(properties_3["name"].values) == 1
        assert len(properties_42["name"].values) == 1
        assert len(properties_100["name"].values) == 1

        assert properties_1["speedlimit"].values[0] == 80
        assert properties_2["speedlimit"].values[0] == 90
        assert properties_24["speedlimit"].values[0] == 100
        assert properties_24["speedlimit"].values[5] == 110
        assert properties_3["speedlimit"].values[0] == 120
        assert properties_42["speedlimit"].values[0] == 130
        assert properties_100["speedlimit"].values[0] == 140

        assert len(properties_1["speedlimit"].values) == 1
        assert len(properties_2["speedlimit"].values) == 1
        assert len(properties_24["speedlimit"].values) == 2
        assert len(properties_3["speedlimit"].values) == 1
        assert len(properties_42["speedlimit"].values) == 1
        assert len(properties_100["speedlimit"].values) == 1
