class NoPathsFound(Exception):
    pass


class GameLogic:
    """
    Class that implement all logic for problem solving. It implement
    BFS algorithm for solving in play() method.
    """
    def __init__(self, chess_map, start, finish, figure):
        self.queue = [start]
        self.visited = dict({start: start})
        self.finish = finish
        self.map = chess_map
        self.figure = figure
        self.path = []

    def __iter__(self):
        return self

    def play(self):
        """
        This method implement BFS for horse task.
        :return: finish node (Node object that contain all path to start node)
        :raises: NoPathFound exception if path couldn't be found
        """
        for node in self.queue:
            # print(node, self.finish)
            if node == self.finish:
                return node
            else:
                # possible_moves gets filtered by map and node figure moves
                possible_moves = self.map.check_steps(self.figure.get_moves(node))
                tmp = [move for move in possible_moves if move not in self.visited]
                self.queue.extend(tmp)
                for i in tmp:
                    self.visited[i] = i

        raise NoPathsFound