# Day 13 of the Advent of Code 2022: Distress Signal
#
# https://adventofcode.com/2022/day/13


import json


def get_packet_pairs():
    packet_pairs = []

    packet_log = ''
    with open('input.txt') as packet_log_file:
        packet_log = packet_log_file.read()

    packet_pairs = [ i for i in packet_log.split('\n\n') ]
    packet_pairs = [ pair.split('\n') for pair in packet_pairs ]

    for i in range(len(packet_pairs)):
        packet_pairs[i][0] = json.loads(packet_pairs[i][0])
        packet_pairs[i][1] = json.loads(packet_pairs[i][1])

    # packet_pairs: [ [ pair1_1, pair1_2 ], [ pair2_1, pair2_2 ], ... ]

    return packet_pairs


# 0: right order
# 1: wrong order
# 2: indifferent
def pair_right_order(_pair1, _pair2):
    for i in range(min(len(_pair1), len(_pair2))):
        pair1_elem = _pair1[i]
        pair2_elem = _pair2[i]
        #print(f'Checking "{pair1_elem}" and "{pair2_elem}":')
        if isinstance(pair1_elem, int) and isinstance(pair1_elem, type(pair2_elem)):
            #print('Same type and int. - ', end='')
            if pair1_elem < pair2_elem:
                #print('right order.')
                return 0
            elif pair1_elem > pair2_elem:
                #print('wrong order.')
                return 1
            else:
                pass
                #print('indifferent. Check next.')
        elif isinstance(pair1_elem, list) and isinstance(pair1_elem, type(pair2_elem)):
            #print('Same type and list. Check order within lists:')
            check_order = pair_right_order(pair1_elem, pair2_elem)
            if check_order == 0:
                #print('right order.')
                return 0
            elif check_order == 1:
                #print('wrong order.')
                return 1
            else:
                pass
                #print(f'indifferent for "{pair1_elem}" and "{pair2_elem}". Check next.')
        else:
            if not isinstance(pair1_elem, list):
                pair1_elem = [pair1_elem]
            if not isinstance(pair2_elem, list):
                pair2_elem = [pair2_elem]
            

            #print(f'Different type. Converted to "{pair1_elem}" and "{pair2_elem}". Check order within lists:')

            check_order = pair_right_order(pair1_elem, pair2_elem)
            if check_order == 0:
                #print('right order.')
                return 0
            elif check_order == 1:
                #print('wrong order.')
                return 1
            else:
                pass
                #print(f'indifferent for "{pair1_elem}" and "{pair2_elem}". Check next.')
    
    if len(_pair1) < len(_pair2):
        return 0
    elif len(_pair1) > len(_pair2):
        return 1
    else:
        return 2


def part_one(_packet_pairs):
    indices = []
    for i in range(len(_packet_pairs)):
        #print(f'{i} / {i+1}: "{_packet_pairs[i][0]}" and "{_packet_pairs[i][1]}": ', end='')
        right_order = pair_right_order(_packet_pairs[i][0], _packet_pairs[i][1])
        #print(right_order)

        if right_order == 0:
            indices.append(i+1)

    print(f'Part one: The sum of the indices of the pairs in the correct order is '\
        f'{sum(indices)}')


def main():
    packet_pairs = get_packet_pairs()

    part_one(packet_pairs)


if __name__ == '__main__':
    main()
