# Day 10 of the Advent of Code 2022: Cathode-Ray Tube
#
# https://adventofcode.com/2022/day/10


def get_register_history(cpu_signal_log):
    register_history = [1]

    register_value = register_history[-1]

    for cmd in cpu_signal_log:
        if cmd == 'noop':
            register_history.append(register_value)
        elif cmd[0:5] == 'addx ':
            # Assume that the input is well formed
            value = int(cmd.split(' ')[1])
            register_history.append(register_value)
            register_history.append(register_value)
            register_value = register_value + value
    
    return register_history


def signal_strength(register_history, cpu_cycle):
    return register_history[cpu_cycle] * cpu_cycle


def main():
    # Read CPU signal log
    cpu_signal_log = []
    with open('input.txt') as cpu_signal_log_file:
        cpu_signal_log = [ line.rstrip() for line in cpu_signal_log_file.readlines() ]

    register_history = get_register_history(cpu_signal_log)

    # Part one: Calculate the combined signal strength at cpu cycles 20, 60,
    # 100, 140, 180 and 220
    combined_signal_strength = 0
    for cpu_cycle in range(20, 220+1, 40):
        sig_strength = signal_strength(register_history, cpu_cycle)
        combined_signal_strength = combined_signal_strength + sig_strength

    print(f'Part one: The combined signal strength is {combined_signal_strength}.')



if __name__ == '__main__':
    main()