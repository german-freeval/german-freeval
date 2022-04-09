from typing import List
import unittest
from german_freeval.input.segment_parsers import CsvSegmentTopologyParser as topology
from german_freeval.input.segment_parsers import CsvSegmentAttributeParser as attributes
from german_freeval.input.segmentbuilder import SegmentBuilder


class SegmentParserTest(unittest.TestCase):

    def test_parse_topology(self):
        segments = topology.parse("tests/resources/topology.csv")
        self.check_topology(segments)

    def test_parse_attributes(self):
        segments = topology.parse("tests/resources/topology.csv")
        attributes.parse(file="tests/resources/attributes.csv", segments=segments)
        self.check_topology(segments=segments)
        self.check_attributes(segments=segments)

    def check_topology(self, segments):
        assert len(segments) == 5

        map = {s.id: s for s in segments}
        b = 'base'
        r = 'ramp'

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
        assert len(map[42].segments_out) == 0

    def check_attributes(self, segments: List[SegmentBuilder]):
        map = {s.id: s for s in segments}

        attributes_1 = {a.name: a for a in map[1].attribute_builders}
        attributes_2 = {a.name: a for a in map[2].attribute_builders}
        attributes_24 = {a.name: a for a in map[24].attribute_builders}
        attributes_3 = {a.name: a for a in map[3].attribute_builders}
        attributes_42 = {a.name: a for a in map[42].attribute_builders}
        print(attributes_1)
        print(attributes_2)
        print(attributes_24)
        print(attributes_3)
        print(attributes_42)

        assert attributes_1['name'].values[0] == 'alpha'
        assert attributes_2['name'].values[0] == 'beta'
        assert attributes_24['name'].values[0] == 'gamma'
        assert attributes_3['name'].values[0] == 'delta'
        assert attributes_42['name'].values[0] == 'epsilon'

        assert len(attributes_1['name'].values) == 1
        assert len(attributes_2['name'].values) == 1
        assert len(attributes_24['name'].values) == 1
        assert len(attributes_3['name'].values) == 1
        assert len(attributes_42['name'].values) == 1

        assert attributes_1['speedlimit'].values[0] == 80
        assert attributes_2['speedlimit'].values[0] == 90
        assert attributes_24['speedlimit'].values[0] == 100
        assert attributes_24['speedlimit'].values[5] == 110
        assert attributes_3['speedlimit'].values[0] == 120
        assert attributes_42['speedlimit'].values[0] == 130

        assert len(attributes_1['speedlimit'].values) == 1
        assert len(attributes_2['speedlimit'].values) == 1
        assert len(attributes_24['speedlimit'].values) == 2
        assert len(attributes_3['speedlimit'].values) == 1
        assert len(attributes_42['speedlimit'].values) == 1
