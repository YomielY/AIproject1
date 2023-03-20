# COMP30024 Artificial Intelligence, Semester 1 2023
# Project Part A: Single Player Infexion

from .utils import render_board

board = {(6, 3): ("b", 5), (5, 3): ("b", 1), (4, 3): ("r", 1), (3, 3): ("r", 6), (6, 4): ("b", 1),
          (6, 5): ("b", 1), (6, 2): ("r", 1)}
tuple1 = (6, 3, "b", 5)
tuple2 = (0, 1)

# 得到行动方向之后spread结果
def spread(tup1: tuple, tup2: tuple, board: dict[tuple, tuple]):
    power = tup1[3]    # power of the original cell
    coordinates_list = []   # list to store coordinates after spread

    i = 1
    while i <= power:
        # find the coordinates after spread
        coordinates_list.append(((tup1[0]+i*tup2[0]) % 7, (tup1[1]+i*tup2[1]) % 7))
        i += 1

    spread_lists = []
    # find the power of each cell after spread
    for coordinate in coordinates_list:
        if coordinate in board:
            color, power = board[coordinate]
            if power < 6:
                new_power = power + 1

            # if the original power is 6, the cell become empty
            else:
                new_power = 0
        # when the spread position is empty
        else:
            new_power = 1
        if new_power != 0:
            spread_lists.append((coordinate[0], coordinate[1], tup1[2], new_power))

    return spread_lists

# 查找cost最合适的spread action -> 6 选 1
def find_action():
    return



def search(input: dict[tuple, tuple]) -> list[tuple]:
    """
    This is the entry point for your submission. The input is a dictionary
    of board cell states, where the keys are tuples of (r, q) coordinates, and
    the values are tuples of (p, k) cell states. The output should be a list of 
    actions, where each action is a tuple of (r, q, dr, dq) coordinates.

    See the specification document for more details.
    """

    # The render_board function is useful for debugging -- it will print out a 
    # board state in a human-readable format. Try changing the ansi argument 
    # to True to see a colour-coded version (if your terminal supports it).
    print(render_board(input, ansi=False))
    print(spread(tuple1, tuple2, board))

    # Here we're returning "hardcoded" actions for the given test.csv file.
    # Of course, you'll need to replace this with an actual solution...
    return [
        (5, 6, -1, 1),
        (3, 1, 0, 1),
        (3, 2, -1, 1),
        (1, 4, 0, -1),
        (1, 3, 0, -1)
    ]
