# class Block:
#     def __init__(self, start_position):
#         self.pos1 = start_position
#         self.pos2 = start_position

#     def display(self):
#         print("Position 1:", self.pos1)
#         print("Position 2:", self.pos2)

#     def get_orientation(self):

#         if self.pos1 == self.pos2:
#             return "standing"

#         elif self.pos1[0] == self.pos2[0]:
#             return "horizontal"

#         elif self.pos1[1] == self.pos2[1]:
#             return "vertical"

#     def move_right(self):

#         orientation = self.get_orientation()

#         r1, c1 = self.pos1
#         r2, c2 = self.pos2

#         if orientation == "standing":

#             self.pos1 = (r1, c1 + 1)
#             self.pos2 = (r1, c1 + 2)

#         elif orientation == "horizontal":

#             self.pos1 = (r1, c2 + 1)
#             self.pos2 = (r1, c2 + 1)

#         elif orientation == "vertical":

#             self.pos1 = (r1, c1 + 1)
#             self.pos2 = (r2, c2 + 1)


#     def move_left(self):

#         orientation = self.get_orientation()

#         r1, c1 = self.pos1
#         r2, c2 = self.pos2

#         if orientation == "standing":

#             self.pos1 = (r1, c1 - 2)
#             self.pos2 = (r1, c1 - 1)

#         elif orientation == "horizontal":

#             self.pos1 = (r1, c1 - 1)
#             self.pos2 = (r1, c1 - 1)

#         elif orientation == "vertical":

#             self.pos1 = (r1, c1 - 1)
#             self.pos2 = (r2, c2 - 1)


#     def move_up(self):

#         orientation = self.get_orientation()

#         r1, c1 = self.pos1
#         r2, c2 = self.pos2

#         if orientation == "standing":

#             self.pos1 = (r1 - 2, c1)
#             self.pos2 = (r1 - 1, c1)

#         elif orientation == "horizontal":

#             self.pos1 = (r1 - 1, c1)
#             self.pos2 = (r2 - 1, c2)

#         elif orientation == "vertical":

#             self.pos1 = (r1 - 1, c1)
#             self.pos2 = (r1 - 1, c1)


#     def move_down(self):

#         orientation = self.get_orientation()

#         r1, c1 = self.pos1
#         r2, c2 = self.pos2

#         if orientation == "standing":

#             self.pos1 = (r1 + 1, c1)
#             self.pos2 = (r1 + 2, c1)

#         elif orientation == "horizontal":

#             self.pos1 = (r1 + 1, c1)
#             self.pos2 = (r2 + 1, c2)

#         elif orientation == "vertical":

#             self.pos1 = (r2 + 1, c1)
#             self.pos2 = (r2 + 1, c1)


#     def get_state(self):

#         return (self.pos1, self.pos2)




class Block:
    def __init__(self, start_position):
        self.pos1 = start_position
        self.pos2 = start_position

    def display(self):
        print(f"Position 1: {self.pos1} | Position 2: {self.pos2} | Orientation: {self.get_orientation()}")

    def get_orientation(self):
        # Standing (Upright) = Both row and column of both blocks are in same coordinates / Both blocks coordinates are same
        if self.pos1 == self.pos2:
            return "standing"
        # Horizontal = the row of both block are same position but their column's coordinates are different
        elif self.pos1[0] == self.pos2[0]:
            return "horizontal"
        #Vertical = Column of both block are same position but their row's coordinates are different
        elif self.pos1[1] == self.pos2[1]:
            return "vertical"

    def _update_positions(self, new_pos1, new_pos2):
        """Helper method to safely update and sort positions."""
        # Sorting guarantees pos1 is always left and pos2 is right
        positions = sorted([new_pos1, new_pos2])
        self.pos1 = positions[0]
        self.pos2 = positions[1]

    def move_right(self):
        r1, c1 = self.pos1
        r2, c2 = self.pos2
        orientation = self.get_orientation()
        if orientation == "standing":
            self._update_positions((r1, c1 + 1), (r1, c1 + 2))
        elif orientation == "horizontal":
            self._update_positions((r1, c2 + 1), (r1, c2 + 1))
        elif orientation == "vertical":
            self._update_positions((r1, c1 + 1), (r2, c2 + 1))

    def move_left(self):
        r1, c1 = self.pos1
        r2, c2 = self.pos2
        orientation = self.get_orientation()
        if orientation == "standing":
            self._update_positions((r1, c1 - 2), (r1, c1 - 1))
        elif orientation == "horizontal":
            self._update_positions((r1, c1 - 1), (r1, c1 - 1))
        elif orientation == "vertical":
            self._update_positions((r1, c1 - 1), (r2, c2 - 1))

    def move_up(self):
        r1, c1 = self.pos1
        r2, c2 = self.pos2
        orientation = self.get_orientation()
        if orientation == "standing":
            self._update_positions((r1 - 2, c1), (r1 - 1, c1))
        elif orientation == "horizontal":
            self._update_positions((r1 - 1, c1), (r2 - 1, c2))
        elif orientation == "vertical":
            self._update_positions((r1 - 1, c1), (r1 - 1, c1))

    def move_down(self):
        r1, c1 = self.pos1
        r2, c2 = self.pos2
        orientation = self.get_orientation()
        if orientation == "standing":
            self._update_positions((r1 + 1, c1), (r1 + 2, c1))
        elif orientation == "horizontal":
            self._update_positions((r1 + 1, c1), (r2 + 1, c2))
        elif orientation == "vertical":
            self._update_positions((r2 + 1, c1), (r2 + 1, c1))

    def copy(self):
        """Returns a completely independent copy of the block for the AI to use."""
        new_block = Block(self.pos1)  # Initialize with pos1
        new_block.pos2 = self.pos2  # Explicitly set pos2
        return new_block

    def __eq__(self, other):
        """Allows Python to compare two blocks: block1 == block2"""
        if not isinstance(other, Block):
            return False

        # Sort to ensure (A, B) is treated the same as (B, A), in case pos1 and pos2 ever get flipped accidentally.
        self_positions = sorted([self.pos1, self.pos2])
        other_positions = sorted([other.pos1, other.pos2])
        return self_positions == other_positions

    def __hash__(self):
        """Allows the block to be stored in a set() for the AI's 'visited' list."""
        # We hash a sorted tuple of the positions so the hash is always consistent
        positions = sorted([self.pos1, self.pos2])
        return hash((positions[0], positions[1]))

    def get_state(self):
        positions = sorted([self.pos1, self.pos2])
        return (positions[0], positions[1])

  