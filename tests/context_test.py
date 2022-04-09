import unittest
from german_freeval.meta.context import Context
from tests.segment_parsers_test import SegmentParserTest


class ContextTest(unittest.TestCase):
    def test_create_from(self):
        context = Context.create_from("tests/resources/config.yaml")

        assert context.n_periods == 10

        test = SegmentParserTest()
        test.check_topology(context.segment_builders)
        test.check_properties(context.segment_builders)
