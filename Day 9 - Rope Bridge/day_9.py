# Day 9 of the Advent of Code 2022: Rope Bridge
#
# https://adventofcode.com/2022/day/9


def move_head(_head, _tail, _direction):
    head = _head

    match _direction:
        case 'U':
            head[0] = head[0] + 1
        case 'D':
            head[0] = head[0] - 1
        case 'L':
            head[1] = head[1] - 1
        case 'R':
            head[1] = head[1] + 1

    tail = move_tail(head, _tail)

    return head, tail


def move_tail(_head, _tail):
    tail = _tail

    if _head[0] == _tail[0]:
        # same row
        if _head[1] > _tail[1] + 1:
            # T . H
            tail[1] = tail[1] + (_head[1] - _tail[1] - 1)
        elif _tail[1] > _head[1] + 1:
            # H . T
            tail[1] = tail[1] + (_head[1] - _tail[1] + 1)
    elif _head[1] == _tail[1]:
        # same column
        if _head[0] > _tail[0] + 1:
            # H
            # .
            # T
            tail[0] = tail[0] + (_head[0] - _tail[0] - 1)
        elif _tail[0] > _head[0] + 1:
            # T
            # .
            # H
            tail[0] = tail[0] + (_head[0] - _tail[0] + 1)
    else:
        if _head[0] > _tail[0] + 1:
            # e.g.   H .
            #        . .
            #        . T
            tail[0] = tail[0] + (_head[0] - _tail[0] - 1)
            tail[1] = _head[1]
        elif _tail[0] > _head[0] + 1:
            # e.g.   T .
            #        . .
            #        . H
            tail[0] = tail[0] + (_head[0] - _tail[0] + 1)
            tail[1] = _head[1]
        
        elif _head[1] > _tail[1] + 1:
            # e.g.   . . H
            #        T . .
            tail[1] = tail[1] + (_head[1] - _tail[1] - 1)
            tail[0] = _head[0]
        elif _tail[1] > _head[1] + 1:
            # e.g.   . . T
            #        H . .
            tail[1] = tail[1] + (_head[1] - _tail[1] + 1)
            tail[0] = _head[0]
    
    return tail


def positions_visited_short_rope(_moves):
    positions = set()

    head = [0, 0]
    tail = [0, 0]

    for move in _moves:
        movement = move.split(' ')
        direction = movement[0]
        multiplier = int(movement[1])

        for i in range(0, multiplier):
            head, tail = move_head(head, tail, direction)
            positions.add(tuple(tail))
    
    return len(positions)


def main():
    moves = []
    with open('input.txt') as moves_file:
        moves = moves_file.readlines()

    print(f'Part one: The tail visits a total of {positions_visited_short_rope(moves)} '\
          f'different positions.')


if __name__ == '__main__':
    main()