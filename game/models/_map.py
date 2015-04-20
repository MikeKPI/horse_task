class Map:
    """
    Represent chess board with all restricted areas and borders.
    Also it uses less memory than simple matrix that represents whole chess board.
    """
    def __init__(self, restricted_positions, max_x, max_y):
        self.restricted_positions = restricted_positions
        self.max_x = max_x
        self.max_y = max_y

    def check_steps(self, steps):
        """
        Method takes tuple of steps and filters it by rules. Step must be on the chess board
        and do not equal to restricted positions.

        :param steps: Tuple of Node objects.
        :return: Tuple of filtered Node objects.
        """
        return tuple([step for step in steps
                      if step not in self.restricted_positions and
                      step.x >= 0 and
                      step.y >= 0 and
                      step.x <= self.max_x and
                      step.y <= self.max_y])