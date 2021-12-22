import os
from collections import defaultdict
from advent_helpers import Point
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, '..', 'data'))



def main():
    with open(os.path.join(DATA_PATH, 'day5.txt')) as file:
        seafloor = defaultdict(lambda: 0)
        diagonals = []
        for line in file:
            line = line.strip()
            points = line.split()
            start = Point.from_string(points[0])
            end = Point.from_string(points[2])
            if start.x == end.x:
                # Vertical line
                y = min(start.y, end.y)
                while y <= max(start.y, end.y):
                    p = Point.from_nums(start.x, y)
                    seafloor[p] += 1
                    y += 1
            elif start.y == end.y:
                # Horizontal line
                x = min(start.x, end.x)
                while x <= max(start.x, end.x):
                    p = Point.from_nums(x, start.y)
                    seafloor[p] += 1
                    x += 1
            else:
                # Diagonals
                diagonals.append((start, end))
        
        count = sum([1 for _, v in seafloor.items() if v > 1])
        print("Part 1: Overlaps = {}".format(count))

        for points in diagonals:
            x_dir = int((points[1].x - points[0].x) / abs(points[1].x - points[0].x))
            y_dir = int((points[1].y - points[0].y) / abs(points[1].y - points[0].y))
            x = points[0].x
            y = points[0].y
            while Point.from_nums(x,y) != points[1]:
                p = Point.from_nums(x, y)
                seafloor[p] += 1
                x += x_dir
                y += y_dir
            seafloor[points[1]] += 1 # Take into account the end point
        
        count = sum([1 for _, v in seafloor.items() if v > 1])
        print("Part 2: Overlaps = {}".format(count))

        # [print(k, v) for k, v in seafloor.items() if v > 1]
if __name__ == "__main__":
    main()
