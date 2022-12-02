# Day 2 of the Advent of Code 2022: Rock Paper Scissors
#
# https://adventofcode.com/2022/day/2


def play_round_assumption(opponent, me):
    score = 0

    if me == 'X': # rock
        score = 1
    elif me == 'Y': # paper
        score = 2
    elif me == 'Z': # scissors
        score = 3
    
    if me == 'X': # rock
        if opponent == 'A': # rock: draw
            score = score + 3
        elif opponent == 'C': # scissors: win
            score = score + 6
    elif me == 'Y': # paper
        if opponent == 'A': # rock: win
            score = score + 6
        elif opponent == 'B': # paper: draw
            score = score + 3
    elif me == 'Z': # scissors
        if opponent == 'B': # paper: win
            score = score + 6
        elif opponent == 'C': # scissors: draw
            score = score + 3
    
    return score


def play_round_strategy(opponent, outcome):
    score = 0

    if opponent == 'A': # rock
        if outcome == 'X': # lose: scissors
            score = score + 0 + 3
        elif outcome == 'Y': # draw: rock
            score = score + 3 + 1
        elif outcome == 'Z': # win: paper
            score = score + 6 + 2
    elif opponent == 'B': # paper
        if outcome == 'X': # lose: rock
            score = score + 0 + 1
        elif outcome == 'Y': # draw: paper
            score = score + 3 + 2
        elif outcome == 'Z': # win: scissors
            score = score + 6 + 3
    elif opponent == 'C': # scissors
        if outcome == 'X': # lose: paper
            score = score + 0 + 2
        elif outcome == 'Y': # draw: scissors
            score = score + 3 + 3
        elif outcome == 'Z': # win: rock
            score = score + 6 + 1
    
    return score



with open('input.txt') as games_file:
    total_score_ass = 0 # Total score if my assumption was correct
    total_score_str = 0 # Total score if I play with the given strategy

    lines = games_file.readlines()
    for line in lines:
        opponent = line[0]
        column_2 = line[2] # my pick (assumption) or game outcome (strategy)

        total_score_ass = total_score_ass + play_round_assumption(opponent, column_2)
        total_score_str = total_score_str + play_round_strategy(opponent, column_2)

    print(f'My total score will be {total_score_ass} if my assumtion is correct.')
    print(f'My total score will be {total_score_str} for the new strategy.')