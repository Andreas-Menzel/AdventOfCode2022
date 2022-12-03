# Day 3 of the Advent of Code 2022: Rucksack Reorganization
#
# https://adventofcode.com/2022/day/3


def calc_item_prio(item):
    item_prio = 0

    # Use ASCII values to calculate the priorities
    if item.islower():
        item_prio = ord(item) - 96
    else:
        item_prio = ord(item) - 64 + 26

    return item_prio


def part_one(rucksacks):
    sum_of_priorities = 0

    for rucksack in rucksacks:
        # "Split" rucksack into two compartments
        comp1 = rucksack[:len(rucksack)//2]
        comp2 = rucksack[len(rucksack)//2:]

        # Get the single item type that remains after an intersection
        item_type = list(set(comp1) & set(comp2))[0]

        item_prio = calc_item_prio(item_type)

        sum_of_priorities = sum_of_priorities + item_prio

    print(f'Part one: Sum of priorities = {sum_of_priorities}')


def part_two(rucksacks):
    groups = []

    # Split elves into groups of three
    current_group = []
    for rucksack in rucksacks:
        current_group.append(rucksack)
        if len(current_group) == 3:
            groups.append(current_group)
            current_group = []

    sum_of_priorities = 0
    for group in groups:
        # Get the single item type that remains after an intersection
        item = list(set(group[0]) & set(group[1]) & set(group[2]))[0]

        sum_of_priorities = sum_of_priorities + calc_item_prio(item)

    print(f'Part two: Sum of priorities = {sum_of_priorities}')


if __name__ == '__main__':
    # Read rucksack contents from file
    rucksacks = []
    with open('input.txt') as file:
        rucksacks = [line.rstrip() for line in file.readlines()]
    
    part_one(rucksacks)
    part_two(rucksacks)