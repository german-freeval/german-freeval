import unittest

from german_freeval.macro.property import Property


class PropertyTest(unittest.TestCase):
    def test_get_item(self):
        property = Property("test", "str", [1, 2, 3, 4])

        for i in range(4):
            assert property[i] == i + 1

    def test_name(self):
        property = Property("test", "str", [1, 2, 3, 4])

        assert property.name == "test"

    def test_type(self):
        property = Property("test", "str", [1, 2, 3, 4])

        assert property.type == "str"
