import os
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, '..', 'data'))


def diff(vals: 'list') -> 'list':
    '''Returns a list of size len(vals)-1 of the difference between 2 consecutive values'''
    out = [vals[i] - vals[i - 1] for i in range(1, len(vals))]
    return out

def sum_sliding(vals: 'list', window_size: int = 3) -> 'list':
    '''Returns a list of sliding window sums of a list'''
    i = 0
    n = window_size - 1
    out = []
    for i in range(n, len(vals)):
        out.append(sum(vals[i - n : i + 1]))
    return out

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
    data_diff = diff(data)
    pos = [1 for d in data_diff if d > 0]
    print("Part 1: %d" % sum(pos))

    three_sliding = sum_sliding(data, window_size = 3)
    three_diff = diff(three_sliding)
    pos_three = [1 for d in three_diff if d > 0]
    print("Part 2: %d" % sum(pos_three))
        

if __name__ == '__main__':
    main()