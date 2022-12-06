# Day 6 of the Advent of Code 2022: Tuning Trouble
#
# https://adventofcode.com/2022/day/6


def detect_distinct_characters(buffer, num_dist):
    for i in range(num_dist-1, len(buffer)):
        if len(list(set(buffer[i-(num_dist-1):i+1]))) == len(buffer[i-(num_dist-1):i+1]):
            return i + 1


if __name__ == '__main__':
    # Read and prepare input
    datastream_buffer = ''
    with open('input.txt') as buffer_file:
        datastream_buffer = buffer_file.read().rstrip()
    
    print(f'Part one: start-of-packet detected at character '\
          f'{detect_distinct_characters(datastream_buffer, 4)}')
    print(f'Part two: start-of-message detected at character '\
          f'{detect_distinct_characters(datastream_buffer, 14)}')