from typing import Dict, List

from german_freeval.input.attributebuilder import AttributeBuilder
from german_freeval.input.segmentbuilder import SegmentBuilder


class CsvSegmentTopologyParser:

    @classmethod
    def parse(cls, file: str) -> List[SegmentBuilder]:
        rows = ParserUtil.read_file(path=file)

        segments: Dict[int, SegmentBuilder] = dict()
        for row in rows:
            s_from, s_to = cls.parseRow(row=row, segments=segments)

            segments[s_from.id] = s_from
            segments[s_to.id] = s_to

        return list(segments.values())

    @classmethod
    def parseRow(
            cls, row: List[str], segments: Dict[int, SegmentBuilder]
    ) -> List[SegmentBuilder]:

        assert len(row) == 4, (
            "Cannot parse connection "
            + str(row)
            + "! expected 4 values: fromId, fromIndex, toId, toIndex"
        )

        fromId: int = int(row[0])
        fromIndex: str = str(row[1])
        toId: int = int(row[2])
        toIndex: str = str(row[3])
        print(fromId, fromIndex, toId, toIndex)

        if fromId not in segments:
            segment_from: SegmentBuilder = SegmentBuilder(fromId)
        else:
            segment_from: SegmentBuilder = segments[fromId]

        if toId not in segments:
            segment_to: SegmentBuilder = SegmentBuilder(toId)
        else:
            segment_to: SegmentBuilder = segments[toId]

        segment_from.add_successor(segment_to, fromIndex)
        segment_to.add_predecessor(segment_from, toIndex)

        return (segment_from, segment_to)


class CsvSegmentAttributeParser:
    @classmethod
    def parse(cls, file: str, segments: List[SegmentBuilder]) -> None:
        rows = ParserUtil.read_file(path=file)
        map = {s.id: s for s in segments}

        for row in rows:
            cls.parseRow(row=row, segments=map)

    @classmethod
    def parseRow(cls, row: List[str], segments: Dict[int, SegmentBuilder]) -> None:
        assert len(row) == 5, (
            "Cannot parse attribute value "
            + str(row)
            + "! expected 5 values: id, name, type, value, period"
        )

        id: int = int(row[0])
        name: str = str(row[1])
        type: str = str(row[2])
        value = cls.parseValue(row[3], type)
        period: int = int(row[4])

        assert id in segments, (
            "Cannot add attribute " + name + " as the segment is missing: " + str(id)
        )
        segment = segments[id]
        attributes = {a.name: a for a in segment.attribute_builders}

        if name not in attributes:
            attribute = AttributeBuilder(name=name, type=type, startvalue=value)
        else:
            attribute = attributes[name]

        attribute.add_period_value(period=period, value=value)

    @classmethod
    def parseValue(cls, value: str, type):
        if type == "str":
            return value
        return eval(type + "(" + value + ")")


class ParserUtil:

    @classmethod
    def read_file(cls, path: str) -> str:
        """Read file content from the given file path and split lines and values.

        Args:
            path (str): Path of the file to be read.

        Returns:
            str: The file content.
        """
        csv_file = open(path, "r")
        data = csv_file.read()
        csv_file.close()

        lines = [
            line
            for mixed_line in data.splitlines()
            if len(mixed_line) > 0
            for line in mixed_line.split("|")
            if len(line) > 0
        ]
        rows = [[v for v in line.split(";")] for line in lines]

        return rows
