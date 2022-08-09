jumps = {
    0: (4, 6),
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (9, 3),
    5: (),
    6: (0, 1, 7),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
}


class L:
    jump: int

    def __init__(self, jump: int):
        self.jump = jump

    def start(self, position: int):
        pass


if __name__ == "__main__":
    l = L(10)
    l.start(0)
