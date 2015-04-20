import queue


class NoPathsFound(Exception):
    pass


class GameLogic:
    def __init__(self, chess_map, start, finish, figure):
        self.visited = [start]
        self.queue = queue.Queue()
        self.queue.put(start)
        self.finish = finish
        self.map = chess_map
        self.figure = figure

    def __iter__(self):
        return self

    def play(self):
        while True:
            try:
                node = self.queue.get()
                # print("size: {sz:100} element: {element:100}".format(sz=str(self.queue.qsize()),
                #                                                      element=str(node)))

                if node == self.finish:
                    return node
                else:
                    # possible_moves gets filtered by map and node figure moves
                    possible_moves = self.map.check_steps(node.check_steps(self.figure.get_moves(node)))
                    for move in possible_moves:
                        if move not in self.visited:
                            self.queue.put(move)
                            self.visited.append(move)
            except queue.Empty:
                raise NoPathsFound()
