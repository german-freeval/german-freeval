from german_freeval.input.property_builder import PropertyBuilder
from german_freeval.input.segment_builder import SegmentBuilder


class CsvSegmentTopologyParser:
    @classmethod
    def parse(cls, file: str) -> list[SegmentBuilder]:
        rows = ParserUtil.read_file(path=file)

        segments: dict[int, SegmentBuilder] = dict()
        for row in rows:
            s_from, s_to = cls.parseRow(row=row, segments=segments)

            segments[s_from.id] = s_from
            segments[s_to.id] = s_to

        return list(segments.values())

    @classmethod
    def parseRow(
        cls, row: list[str], segments: list[int, SegmentBuilder]
    ) -> list[SegmentBuilder]:

        assert len(row) == 4, (
            "Cannot parse connection "
            + str(row)
            + "! expected 4 values: fromId, fromIndex, toId, toIndex"
        )

        from_id: int = int(row[0])
        from_index: str = str(row[1])
        to_id: int = int(row[2])
        to_index: str = str(row[3])

        if from_id not in segments:
            segment_from: SegmentBuilder = SegmentBuilder(from_id)

        else:
            segment_from: SegmentBuilder = segments[from_id]

        if to_id not in segments:
            segment_to: SegmentBuilder = SegmentBuilder(to_id)
        else:
            segment_to: SegmentBuilder = segments[to_id]

        segment_from.add_successor(segment_to, from_index)
        segment_to.add_predecessor(segment_from, to_index)

        return (segment_from, segment_to)


class CsvSegmentPropertyParser:
    @classmethod
    def parse(cls, file: str, segments: list[SegmentBuilder]) -> None:
        rows = ParserUtil.read_file(path=file)
        map = {s.id: s for s in segments}

        for row in rows:
            cls.parseRow(row=row, segments=map)

    @classmethod
    def parseRow(cls, row: list[str], segments: dict[int, SegmentBuilder]) -> None:
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
            "Cannot add property " + name + " as the segment is missing: " + str(id)
        )
        segment = segments[id]
        properties = {p.name: p for p in segment.property_builders}

        if name not in properties:
            property = PropertyBuilder(name=name, type=type, initial_values=value)
            segment.add_property(property)
        else:
            property = properties[name]

        property.add_period_value(period=period, value=value)

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
