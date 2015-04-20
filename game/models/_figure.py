from game.models import Node


class HorseFigure:
    """
    Implementation of single chess figure.
    """
    @staticmethod
    def get_moves(position):
        """
        Method get figure position and returns all possible positions without
        exceptions (Node(x=-1, y=20) possible too). You need to filtrate output of it.

        :param position: Node object that describe position where figure located now.
        :return: Tuple of all possible positions. Every single position is a Node object.
        """
        return (
            Node(x=position.x-1,    # left 1
                 y=position.y-2),   # top 2
            Node(x=position.x+1,    # right 1
                 y=position.y-2),   # top 2

            Node(x=position.x+2,    # right 2
                 y=position.y-1),   # top 1
            Node(x=position.x+2,    # right 2
                 y=position.y+1),   # bottom 1

            Node(x=position.x+1,    # right 1
                 y=position.y+2),   # bottom 2
            Node(x=position.x-1,    # left 1
                 y=position.y+2),   # bottom 2

            Node(x=position.x-2,    # left 2
                 y=position.y+1),   # bottom 1
            Node(x=position.x-2,    # left 2
                 y=position.y-1),   # top 1
        )