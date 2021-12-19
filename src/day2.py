import os, re, mmap
import numpy as np
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, '..', 'data'))

def sum_values(match_list: 'list') -> int:
    return np.sum(list(map(int, match_list)))

def main():
    '''Reads in the specified file of numbers'''
    out = []
    depth = 0
    horizontal = 0
    file_name = os.path.join(DATA_PATH, 'day2.txt')
    with open(file_name, 'r') as file:
        data = file.read()
        forward = re.findall(r"forward (\d+)", data)
        up = re.findall(r"up (\d+)", data)
        down = re.findall(r"down (\d+)", data)
        horizontal += sum_values(forward)
        depth += sum_values(down)
        depth -= sum_values(up)
        print("Final position: (%d, %d) -> Part 1 = %d" % (horizontal, depth, horizontal * depth))

    with open(file_name, 'r') as file:
        aim = 0
        depth = 0
        horizontal = 0
        for line in file:
            line = line.strip()
            forward = re.match(r"forward (\d+)", line)
            up = re.match(r"up (\d+)", line)
            down = re.match(r"down (\d+)", line)
            if forward:
                horizontal += int(forward[1])
                depth += aim * int(forward[1])
            elif up:
                aim -= int(up[1])
            elif down:
                aim += int(down[1])
        print("Final position: (%d, %d) -> Part 2 = %d" % (horizontal, depth, horizontal * depth))

    return out

if __name__ == '__main__':
    main()