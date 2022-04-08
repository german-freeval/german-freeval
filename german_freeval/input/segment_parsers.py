from typing import Dict, List
from segmentbuilder import SegmentBuilder

class CsvSegmentTopologyParser:
    
    @classmethod
    def parse(cls, file:str) -> List[SegmentBuilder]:
        rows = ParserUtil.read_file(path=file)
        
        segments: Dict[int,SegmentBuilder] = dict()
        for row in rows:
            s_from, s_to = cls.parseRow(row=row, segments=segments)
            
            segments[s_from.id] = s_from
            segments[s_to.id] = s_to
    
        return segments.values()
           
    
    @classmethod
    def parseRow(cls, row: List[str], segments: Dict[int,SegmentBuilder]) -> List[SegmentBuilder]:
        assert len(row) == 4, "Cannot parse connection " + str(row) + "! expected 4 values: fromId, fromIndex, toId, toIndex"
        
        fromId: int = int(row[0])
        fromIndex: int = int(row[1])
        toId: int = int(row[2])
        toIndex: int = int(row[3])
        
        if not segments[fromId]:
            segment_from: SegmentBuilder = SegmentBuilder(fromId)
        else:
            segment_from: SegmentBuilder = segments[fromId]
        
        if not segments[toId]:
            segment_to: SegmentBuilder = SegmentBuilder(fromId)
        else:
            segment_from: SegmentBuilder = segments[fromId]
            
        segment_from.add_successor(segment_to, toIndex)
        segment_to.add_predecessor(segment_from, fromIndex)
        
        return (segment_from, segment_to)
       
    
class CsvSegmentAttributeParser:
    
    @classmethod
    def parse(cls, file:str) -> None:
           rows = ParserUtil.read_file(path=file)
       
       

class ParserUtil:
    
    @classmethod
    def read_file(cls, path: str) -> str:
        """Read file content from the given file path.

        Args:
            path (str): Path of the file to be read.

        Returns:
            str: The file content.
        """
        csv_file = open(path, "r")
        data = csv_file.read()
        csv_file.close()
        
        lines = [ln for l in data.splitlines() if len(l) > 0 for ln in l.split('|') if len(ln) > 0]
        rows = [[v for v in l.split(';')] for l in lines]
        
        return rows