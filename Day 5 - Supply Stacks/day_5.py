# Day 5 of the Advent of Code 2022: Supply Stacks
#
# https://adventofcode.com/2022/day/5

from copy import deepcopy


# part one
def operate_CrateMover_9000(stacks, num_of_crates, stack_from, stack_to):
    stack_from = stack_from - 1
    stack_to = stack_to - 1

    for i in range(num_of_crates):
        stacks[stack_to].append(stacks[stack_from].pop())

    return stacks


# part two
def operate_CrateMover_9001(stacks, num_of_crates, stack_from, stack_to):
    stack_from = stack_from - 1
    stack_to = stack_to - 1

    crane_cargo_holder = []
    for i in range(num_of_crates):
        crane_cargo_holder.append(stacks[stack_from].pop())

    for crate in reversed(crane_cargo_holder):
        stacks[stack_to].append(crate)

    return stacks


def get_top_crates(stacks):
    top_crates = ''

    for stack in stacks:
        if len(stack) > 1:
            crate = stack[-1]

            top_crates = f'{top_crates}{crate}'
    
    return top_crates


if __name__ == '__main__':
    stacks_str = []
    instructions_str = []

    lines = []
    with open('input.txt') as file:
        lines = file.read()

    # Get and process stacks section
    stacks_str = lines.split('\n\n')[0].split('\n')
    stacks_str = list(reversed(stacks_str))

    # Get and "process" instructions section
    instructions_str = lines.split('\n\n')[1].split('\n')
    if instructions_str[-1] == '':
        instructions_str.remove('')

    num_of_stacks = int((len(stacks_str[0]) + 1) / 4)
    stacks = [ [] for i in range(0, num_of_stacks) ]

    # Fill stacks list (stack-id included)
    for stack_line in stacks_str:
        for stack_index in range(0, num_of_stacks):
            if not stack_line[4 * stack_index + 1] == ' ':
                stacks[stack_index].append(stack_line[4 * stack_index + 1])

    # Prepare the stacks for the CrateMovers
    stacks_CrateMover_9000 = stacks
    stacks_CrateMover_9001 = deepcopy(stacks)

    for instruction in instructions_str:
        parameters = [ int(i) for i in instruction.split(' ') if i.isnumeric() ]
        
        stacks_CrateMover_9000 = operate_CrateMover_9000(stacks_CrateMover_9000,
                                 parameters[0], parameters[1], parameters[2])
        stacks_CrateMover_9001 = operate_CrateMover_9001(stacks_CrateMover_9001,
                                 parameters[0], parameters[1], parameters[2])

    print(f'Part one: The top crates will be {get_top_crates(stacks_CrateMover_9000)} '
          f'if using the CrateMover9000.')
    print(f'Part two: The top crates will be {get_top_crates(stacks_CrateMover_9001)} '
          f'if using the CrateMover9001.')