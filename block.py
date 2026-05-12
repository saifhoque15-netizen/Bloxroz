class Block:
    def __init__(self, start_position):
        self.pos1 = start_position
        self.pos2 = start_position

    def display(self):
        print("Position 1:", self.pos1)
        print("Position 2:", self.pos2)

    def get_orientation(self):

        if self.pos1 == self.pos2:
            return "standing"

        elif self.pos1[0] == self.pos2[0]:
            return "horizontal"

        elif self.pos1[1] == self.pos2[1]:
            return "vertical"

    def move_right(self):

        orientation = self.get_orientation()

        r1, c1 = self.pos1
        r2, c2 = self.pos2

        if orientation == "standing":

            self.pos1 = (r1, c1 + 1)
            self.pos2 = (r1, c1 + 2)

        elif orientation == "horizontal":

            self.pos1 = (r1, c2 + 1)
            self.pos2 = (r1, c2 + 1)

        elif orientation == "vertical":

            self.pos1 = (r1, c1 + 1)
            self.pos2 = (r2, c2 + 1)


    def move_left(self):

        orientation = self.get_orientation()

        r1, c1 = self.pos1
        r2, c2 = self.pos2

        if orientation == "standing":

            self.pos1 = (r1, c1 - 2)
            self.pos2 = (r1, c1 - 1)

        elif orientation == "horizontal":

            self.pos1 = (r1, c1 - 1)
            self.pos2 = (r1, c1 - 1)

        elif orientation == "vertical":

            self.pos1 = (r1, c1 - 1)
            self.pos2 = (r2, c2 - 1)


    def move_up(self):

        orientation = self.get_orientation()

        r1, c1 = self.pos1
        r2, c2 = self.pos2

        if orientation == "standing":

            self.pos1 = (r1 - 2, c1)
            self.pos2 = (r1 - 1, c1)

        elif orientation == "horizontal":

            self.pos1 = (r1 - 1, c1)
            self.pos2 = (r2 - 1, c2)

        elif orientation == "vertical":

            self.pos1 = (r1 - 1, c1)
            self.pos2 = (r1 - 1, c1)


    def move_down(self):

        orientation = self.get_orientation()

        r1, c1 = self.pos1
        r2, c2 = self.pos2

        if orientation == "standing":

            self.pos1 = (r1 + 1, c1)
            self.pos2 = (r1 + 2, c1)

        elif orientation == "horizontal":

            self.pos1 = (r1 + 1, c1)
            self.pos2 = (r2 + 1, c2)

        elif orientation == "vertical":

            self.pos1 = (r2 + 1, c1)
            self.pos2 = (r2 + 1, c1)


    def get_state(self):

        return (self.pos1, self.pos2)