import os
import numpy as np
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, '..', 'data'))

def read_data(file_name: str) -> 'list':
    '''Reads in the specified file of numbers'''
    out = []
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line.isdigit():
                out.append(int(line))

    return out

def main() :
    data = read_data(os.path.join(DATA_PATH, 'day1.txt'))
    data_diff = np.diff(data)
    print("Part 1: %d" % np.sum(data_diff > 0))

    three_sliding = np.convolve(data, np.ones(3, dtype = int), 'valid')
    three_diff = np.diff(three_sliding)
    print("Part 2: %d" % np.sum(three_diff > 0))
        

if __name__ == '__main__':
    main()