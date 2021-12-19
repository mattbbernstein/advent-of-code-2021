import os
from collections import defaultdict
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, '..', 'data'))

def opposite(x: int, len: int) -> int:
    '''Bitwise not of x (as if it was an unsigned int'''
    return ~x & ((2 ** len) - 1)

def filter_bits(bits: 'list', n: int, least_common: bool = False) -> 'list':
    '''
    Filters a list of binary representation strings to only include values
    that have the most common (or least comming if most_common = false) nth bit
    '''
    num_vals = len(bits)
    nth_bits = [int(x[n]) for x in bits]
    filter_val = 1 if sum(nth_bits) >= (num_vals / 2) else 0
    if least_common: 
        filter_val = 1 if sum(nth_bits) < (num_vals / 2) else 0

    out = [x for x in bits if int(x[n]) == filter_val]
    return out

def main():
    with open(os.path.join(DATA_PATH, 'day3.txt')) as file:
        bits = defaultdict(lambda: list())
        line_count = 0
        for line in file:
            line_count += 1
            line = line.strip()
            for i, c in enumerate(line):
                bits[i].append(int(c))
        
        num_bits = len(bits.keys())
        gamma_bits = [0] * num_bits
        for i in sorted(bits.keys()):
            if sum(bits[i]) > (line_count / 2):
                gamma_bits[i] = 1
        gamma = int("".join(map(str, gamma_bits)), base = 2)
        epsilon = opposite(gamma, num_bits)
        print("Gamma   = {0} [{1:012b}]".format(gamma, gamma))
        print("Epsilon = {0} [{1:012b}]".format(epsilon, epsilon))
        print("Part 1 = {}".format(gamma * epsilon))

        file.seek(0)
        data = file.read().splitlines()
        o2_gen_list = data
        i = 0
        while o2_gen_list and len(o2_gen_list) != 1:
            o2_gen_list = filter_bits(o2_gen_list, i)
            i += 1
        o2_gen = int(o2_gen_list[0], base = 2)

        co2_scrubber_list = data
        i = 0
        while co2_scrubber_list and len(co2_scrubber_list) != 1:
            co2_scrubber_list = filter_bits(co2_scrubber_list, i, least_common = True)
            i += 1
        co2_scrubber = int(co2_scrubber_list[0], base = 2)

        print()
        print("O2 Generator  = {0} [{1}]".format(o2_gen, o2_gen_list[0]))
        print("CO2 Scrubber = {0} [{1}]".format(co2_scrubber, co2_scrubber_list[0]))
        print("Part 2 = {}".format(o2_gen * co2_scrubber))
        


    
if __name__ == '__main__':
    main()