class NoPathsFound(Exception):
    pass


class GameLogic:
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