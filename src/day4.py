import os, re, copy
from advent_helpers import BingoBoard
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.abspath(os.path.join(SCRIPT_PATH, '..', 'data'))

def process_data(text: str) -> list[BingoBoard]:
    '''Process file and return list of bingo boards'''
    text_boards = re.split(r"\n{2,}", text.strip())
    boards = []
    for text_board in text_boards:
        text_board = text_board.splitlines()
        board = BingoBoard(text_board)
        boards.append(board)
    return boards
    
def main():
    with open(os.path.join(DATA_PATH, 'day4.txt')) as file:
        number_list = file.readline()
        number_list = list(map(int, number_list.split(',')))
        text_boards = file.read()
        boards = process_data(text_boards)
        first_board = False
        unfinished_boards = list(range(len(boards)))
        for number in number_list:
            for i, board in enumerate(boards):
                if board.check_board():
                    continue
                elif board.mark(number):
                    unfinished_boards.remove(i)
                    score = board.score(number)
                    if not first_board:
                        print("Part 1: Score = {}".format(score))
                        first_board = True
                    if len(unfinished_boards) == 0:
                        print("Part 2: Score = {}".format(score))

if __name__ == '__main__':
    main()
