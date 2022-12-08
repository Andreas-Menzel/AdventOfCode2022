# Day 8 of the Advent of Code 2022: Treetop Treehouse
#
# https://adventofcode.com/2022/day/8


# x: row - starting from 0
# y: column - starting from 0
def is_visible(forest, x, y):
    if x == 0 or x == len(forest)-1 or y == 0 or y == len(forest[0])-1:
        return True
    else:
        tree_height = forest[x][y]

        visible = True
        # check up
        for row in list(range(0, x)):
            if forest[row][y] >= tree_height:
                visible = False
        
        if visible:
            return True
        
        visible = True
        # check down
        for row in list(range(x+1, len(forest))):
            if forest[row][y] >= tree_height:
                visible = False
        
        if visible:
            return True

        visible = True
        # check left
        for col in list(range(0, y)):
            if forest[x][col] >= tree_height:
                visible = False
        
        if visible:
            return True
        
        visible = True
        # check right
        for col in list(range(y+1, len(forest[x]))):
            if forest[x][col] >= tree_height:
                visible = False

        return visible


def trees_visible_from_outside(forest):
    visible_counter = 0

    for row in range(len(forest)):
        for col in range(len(forest[row])):
            if is_visible(forest, row, col):
                visible_counter = visible_counter + 1
    
    return visible_counter


# dir must be in ['left', 'right', 'up', 'down']
def trees_visible_from_inside(forest, x, y, dir):
    trees = 0
    
    match dir:
        case 'left':
            for col in range(y-1, -1, -1):
                trees = trees + 1
                if forest[x][col] >= forest[x][y]:
                    break
        case 'right':
            for col in range(y+1, len(forest[x])):
                trees = trees + 1
                if forest[x][col] >= forest[x][y]:
                    break
        case 'up':
            for row in range(x-1, -1, -1):
                trees = trees + 1
                if forest[row][y] >= forest[x][y]:
                    break
        case 'down':
            for row in range(x+1, len(forest)):
                trees = trees + 1
                if forest[row][y] >= forest[x][y]:
                    break
        case _:
            return 0

    return trees


def highest_scenic_score(forest):
    highest_score = 0

    for row in range(0, len(forest)):
        for col in range(0, len(forest[row])):
            visible_left = trees_visible_from_inside(forest, row, col, 'left')
            visible_right = trees_visible_from_inside(forest, row, col, 'right')
            visible_up = trees_visible_from_inside(forest, row, col, 'up')
            visible_down = trees_visible_from_inside(forest, row, col, 'down')

            scenic_score = visible_left * visible_right * visible_up * visible_down

            if scenic_score > highest_score:
                highest_score = scenic_score

    return highest_score


def main():
    # Read forest map
    forest = []
    with open('input.txt') as forest_map_file:
        forest_str = forest_map_file.readlines()
    
    # Convert str map to int map
    for row in range(len(forest_str)):
        forest.append([])
        for col in range(len(forest_str[row])-1):
            forest[-1].append(int(forest_str[row][col]))
    
    print(f'Part one: {trees_visible_from_outside(forest)} trees are visible '\
          f'from the outside.')
    print(f'Part two: The highest scenic score is {highest_scenic_score(forest)}')


if __name__ == '__main__':
    main()