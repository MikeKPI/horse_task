class NodeIterator:
    def __init__(self, parent):
        self.parent = parent

    def __next__(self):
        tmp = self.parent
        if tmp is not None:
            self.parent = self.parent.parent
            return tmp
        else:
            raise StopIteration


class Node(NodeIterator):
    """
    Single step in BFS. It has x and y coordinate of object on the map
    and the ancestor object (must be the same class). Also class implements
    NodeIterator class for iteration and can be used by instruction 'in'.
    """
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent

    def __eq__(self, other):
        if self.x == other.x and \
                self.y == other.y:
            return True
        else:
            return False

    def __iter__(self):
        return NodeIterator(self)

    def __str__(self):
        return '[ x: {X:10} | y: {Y:10} |'.format(X=self.x, Y=self.y)

    def __len__(self):
        n = 0
        for _ in self:
            n += 1

        return n

    def check_steps(self, steps):
        """
        Node's checking operation for checking doubling.

        :param steps: tuple of Node objects
        :return: tuple of unique Nodes for this Node
        """
        tmp = [step for step in steps if step not in self]          # checks if step already used
        for step in tmp:
            step.parent = self
        return tuple(tmp)


if __name__ == '__main__':
    a = Node(3, 2, Node(4, 3, Node(5, 6)))

    print('True' if a.parent in a else 'False')