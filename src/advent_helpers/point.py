from typing import NewType

Point = NewType('Point', object)

class Point:

    def __init__(self):
        '''Creats a x, y point'''
        
        self.x = 0
        self.y = 0

    @classmethod
    def from_string(cls, coords: str) -> Point:
        '''Creates a x, y point from a string'''
        
        pts_str = coords.split(',')
        p = Point()
        p.x = int(pts_str[0])
        p.y = int(pts_str[1])
        return p

    @classmethod
    def from_nums(cls, x: int, y: int) -> Point:
        '''Creates an x, y point from 2 numbers'''

        p = Point()
        p.x = x
        p.y = y
        return p

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Point):
            return (self.x == other.x ) and (self.y == other.y)
        
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return "Point[{}, {}]".format(self.x, self.y)