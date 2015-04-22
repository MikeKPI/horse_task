from game.game_logic import GameLogic, NoPathsFound
from game.models import Map, HorseFigure, Node


def generate_map(map_matrix):
    """
    Generating object of Map class.

    :param map_matrix: boolean initialization matrix
    :return: object of Map class
    """
    restricted = []

    for y, row in enumerate(map_matrix):
        for x, node in enumerate(row):
            if not node:
                # restricted.append(tuple(x, y))
                restricted.append(Node(x=x, y=y))

    return Map(restricted_positions=restricted,
               max_x=len(map_matrix[0])-1,          # X, Y starts with 0 and ends with len - 1
               max_y=len(map_matrix)-1)


def get_position(x, y):
    return Node(x=x, y=y)   # models.Node(x=x, y=y)


if __name__ == '__main__':
    from time import time

    chess_map = [[True for _ in range(10)] for _ in range(10)]
    gl = game_logic.GameLogic(chess_map=generate_map(chess_map),
                              start=get_position(9, 0),
                              finish=get_position(0, 9),
                              figure=HorseFigure())

    start = time()
    try:
        a = gl.play()
    except game_logic.NoPathsFound as e:
        print(e)
    print('Execution time {}'.format(str(time()-start)))
    print(a)
    print(len(gl.queue))
