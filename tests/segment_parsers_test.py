import unittest
from german_freeval.input.segment_parsers import CsvSegmentTopologyParser as topology

class SegmentParserTest(unittest.TestCase):
    
    def test_parse_topology(self):
        segments = topology.parse("tests/resources/topo.csv")
        print(segments)
        assert len(segments) == 5
        
        map = {s.id:s for s in segments}
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
        