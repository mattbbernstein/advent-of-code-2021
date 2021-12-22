import os
from advent_helpers import LanternfishSchool
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, '..', 'data'))

def main():
    with open(os.path.join(DATA_PATH, 'day6.txt')) as file:
        fish_str = file.read()
        fish = list(map(int,fish_str.split(',')))
        school = LanternfishSchool(fish)
        end_size = school.simulate(80)
        print("Part 1: School size = {}".format(end_size))
        school = LanternfishSchool(fish)
        end_size = school.simulate(256)
        print("Part 2: School size = {}".format(end_size))

if __name__ == '__main__':
    main()