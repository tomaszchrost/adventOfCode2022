import utils


def main():
    rps_list = utils.get_matchups()
    scores = (utils.RockPaperScissors.get_score_part_one(move[0], move[1]) for move in rps_list)
    print(sum(scores))


if __name__ == '__main__':
    main()
