# Day 4 of the Advent of Code 2022: Camp Cleanup
#
# https://adventofcode.com/2022/day/4


def fully_contains(pair1, pair2):
    pair1 = [int(i) for i in pair1.split('-')]
    pair2 = [int(i) for i in pair2.split('-')]

    if pair1[0] <= pair2[0] and pair1[1] >= pair2[1]:
        return True
    else:
        return False


def overlaps(pair1, pair2):
    pair1 = [int(i) for i in pair1.split('-')]
    pair2 = [int(i) for i in pair2.split('-')]

    if pair1[0] <= pair2[0] and pair1[1] >= pair2[0] \
            or pair2[0] <= pair1[1] and pair2[1] >= pair1[0]:
        return True
    else:
        return False


def part_one(cleanup_plan):
    counter = 0

    for group in cleanup_plan:
        pairs = group.split(',')
        
        if fully_contains(pairs[0], pairs[1]) or fully_contains(pairs[1], pairs[0]):
            counter = counter + 1

    return counter


def part_two(cleanup_plan):
    counter = 0

    for group in cleanup_plan:
        pairs = group.split(',')
        
        if overlaps(pairs[0], pairs[1]) or overlaps(pairs[1], pairs[0]):
            counter = counter + 1

    return counter


if __name__ == '__main__':
    # Read cleanup plan
    cleanup_plan = []
    with open('input.txt') as file:
        cleanup_plan = [line.rstrip() for line in file.readlines()]

    print(f'Part 1: {part_one(cleanup_plan)} pairs have a complete overlap situation.')
    print(f'Part 2: {part_two(cleanup_plan)} pairs have an overlap situation.')
