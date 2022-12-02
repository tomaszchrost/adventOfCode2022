import os
import enum

RESOURCES = os.path.abspath('resources/')
ROCK_PAPER_SCISSORS_FILE_PATH = os.path.join(RESOURCES, 'rock_paper_scissors.dat')


class RockPaperScissors:

    class Moves(enum.Enum):
        ROCK = 1
        SCISSORS = 2
        PAPER = 3

    class Outcomes(enum.Enum):
        LOSE = 1
        DRAW = 2
        WIN = 3

    RPS_SCORE_VALUES = {Moves.ROCK: 1, Moves.PAPER: 2, Moves.SCISSORS: 3}
    THEIR_MOVE_MAP = {'A': Moves.ROCK, 'B': Moves.PAPER, 'C': Moves.SCISSORS}
    MY_MOVE_MAP = {'X': Moves.ROCK, 'Y': Moves.PAPER, 'Z': Moves.SCISSORS}
    MY_OUTCOME_MAP = {'X': Outcomes.LOSE, 'Y': Outcomes.DRAW, 'Z': Outcomes.WIN}

    @classmethod
    def did_i_draw(cls, i_played, they_played):
        my_move = cls.MY_MOVE_MAP[i_played]
        their_move = cls.THEIR_MOVE_MAP[they_played]

        return my_move == their_move

    @classmethod
    def did_i_win(cls, i_played, they_played):
        moves = cls.Moves

        my_move = cls.MY_MOVE_MAP[i_played]
        their_move = cls.THEIR_MOVE_MAP[they_played]

        return ((my_move == moves.ROCK and their_move == moves.SCISSORS)
                or (my_move == moves.SCISSORS and their_move == moves.PAPER)
                or (my_move == moves.PAPER and their_move == moves.ROCK))

    @classmethod
    def get_score_part_one(cls, they_played, i_played):
        my_move = cls.MY_MOVE_MAP[i_played]
        score = cls.RPS_SCORE_VALUES[my_move]

        if cls.did_i_draw(i_played, they_played):
            score += 3
        elif cls.did_i_win(i_played, they_played):
            score += 6

        return score

    @classmethod
    def get_score_part_two(cls, they_played, i_need_to):
        my_outcome = cls.MY_OUTCOME_MAP[i_need_to]

        score = 0
        opponent_rps_score_value = cls.RPS_SCORE_VALUES[cls.THEIR_MOVE_MAP[they_played]]
        if my_outcome == cls.Outcomes.DRAW:
            score = 3 + opponent_rps_score_value
        elif my_outcome == cls.Outcomes.WIN:
            score = 6 + (1 if opponent_rps_score_value + 1 == 4 else opponent_rps_score_value + 1)
        elif my_outcome == cls.Outcomes.LOSE:
            score = 3 if opponent_rps_score_value - 1 == 0 else opponent_rps_score_value - 1

        return score


def get_matchups():
    with open(ROCK_PAPER_SCISSORS_FILE_PATH, 'r') as f:
        rps_list = f.readlines()

    formatted_rps_list = [item.strip().split() for item in rps_list]
    return formatted_rps_list
