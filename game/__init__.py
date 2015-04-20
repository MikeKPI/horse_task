import game_logic
import models


def generate_map(map_matrix):
    restricted = []

    for y, row in enumerate(map_matrix):
        for x, node in enumerate(row):
            if not node:
                restricted.append(models.Node(x=x, y=y))

    return models.Map(restricted_positions=restricted,
                      max_x=len(map_matrix[0])-1,          # X, Y starts with 0 and ends with len - 1
                      max_y=len(map_matrix)-1)


def get_position(x, y):
    return models.Node(x=x, y=y)


if __name__ == '__main__':
    from time import time

    chess_map = [[True for _ in range(1000)] for _ in range(1000)]
    gl = game_logic.GameLogic(chess_map=generate_map(chess_map),
                              start=get_position(999, 0),
                              finish=get_position(0, 999),
                              figure=models.HorseFigure())

    start = time()
    try:
        a = gl.play()
    except game_logic.NoPathsFound as e:
        print(e)
    print('Execution time {}'.format(str(time()-start)))
    print(len(a)-1)
    print(a)