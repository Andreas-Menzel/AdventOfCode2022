# Day 11 of the Advent of Code 2022: Monkey in the Middle
#
# https://adventofcode.com/2022/day/11
#
# Either my implementation is way to inefficient, or my laptop has not enough
# processing power to calculate the result for part two. I rather blame it on
# my laptop ^^


class Monkey:
    all_monkeys = []

    def __init__(self, _items, _operation, _test_divisable_by, _monkey_true, _monkey_false, _me_in_panic_mode):
        self.items = _items
        self.operation = _operation
        self.test_divisable_by = _test_divisable_by
        self.monkey_true = _monkey_true
        self.monkey_false = _monkey_false
        self.me_in_panic_mode = _me_in_panic_mode

        self.inspections = 0
    
    def operate(self, _item):
        item = 0
        
        val = 0
        if self.operation[1] == 'old':
            val = _item
        else:
            val = int(self.operation[1])

        match self.operation[0]:
            case '+':
                item = _item + val
            case '-':
                item = _item - val
            case '*':
                item = _item * val
            case '/':
                item = _item / val
        
        return item
    
    def perform_test(self, item):
        return item % self.test_divisable_by == 0
    
    def play_routine_one_item(self):
        self.inspections = self.inspections + 1

        item = self.items.pop(0)  # Inspect
        item = self.operate(item) # Operate
        if not self.me_in_panic_mode:
            item = item // 3      # Monkey gets bored

        other_monkey = None
        if self.perform_test(item):
            other_monkey = self.monkey_true
        else:
            other_monkey = self.monkey_false

        self.all_monkeys[other_monkey].items.append(item)
    
    def play_routine(self):
        while self.items != []:
            self.play_routine_one_item()


def process_monkey_observations(_me_in_panic_mode = False):
    monkey_objects = []

    notes = []
    with open('input.txt') as notes_file:
        notes = notes_file.read()

    monkeys = notes.split('\n\n')

    for monkey in monkeys:
        monkey = monkey.split('\n')

        items = [ int(item) for item in monkey[1][18:].split(', ') ]
        operation = [ monkey[2][23:24], monkey[2][25:] ]
        test_divisable_by = int(monkey[3][21:])
        monkey_true = int(monkey[4][29:])
        monkey_false = int(monkey[5][30:])

        new_monkey = Monkey(items, operation, test_divisable_by, monkey_true, monkey_false, _me_in_panic_mode)
        monkey_objects.append(new_monkey)

    Monkey.all_monkeys = monkey_objects
    return monkey_objects


def play_round(monkeys):
    for i in range(len(monkeys)):
        monkeys[i].play_routine()


def play_rounds(monkeys, rounds):
    for i in range(rounds):
        play_round(monkeys)


def calculate_monkey_business(monkeys):
    level = 0

    inspections = [ monkey.inspections for monkey in monkeys ]
    inspections.sort()

    level = inspections[-1] * inspections[-2]

    return level


def part_one():
    # Read file and prepare data
    monkeys = process_monkey_observations(_me_in_panic_mode = False)

    play_rounds(monkeys, 20)

    print(f'Part one: The level of monkey business after 20 rounds is '\
          f'{calculate_monkey_business(monkeys)} if I stay calm and rational.')


def part_two():
    # Read file and prepare data
    monkeys = process_monkey_observations(_me_in_panic_mode = True)

    play_rounds(monkeys, 10000)

    print(f'Part one: The level of monkey business after 10000 (!) rounds is '\
          f'{calculate_monkey_business(monkeys)} if I activate panic mode.')


def main():
    part_one()
    part_two()


if __name__ == '__main__':
    main()