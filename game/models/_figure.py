from game.models import Node


class ChessFigure:
    def get_moves(self, position):
        """
        Method get figure position and returns all possible positions without
        exceptions (Node(x=-1, y=20) possible too). You need to filtrate output of it.

        :param position: Node object that describe position where figure located now.
        :return: Tuple of all possible positions. Every single position is a Node object.
        """
        return tuple([Node(x=position.x+xi,
                           y=position.y+yi,
                           parent=position)
                      for xi, yi in self._moves_coefficients])


class HorseFigure(ChessFigure):
    """
    Implementation of single chess figure.
    """

    def __init__(self):
        self._moves_coefficients = tuple([[-1, -2],
                                          [1, -2],
                                          [2, -1],
                                          [2, 1],
                                          [1, 2],
                                          [-1, 2],
                                          [-2, 1],
                                          [-2, -1],
                                          ])
