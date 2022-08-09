jumps = {
    0: (4, 6),
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (0, 3, 9),
    5: (),
    6: (0, 1, 7),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
}


class L:
    jump: int
    size: int

    def __init__(self, jump: int):
        self.jump = jump
        self.size = 0

    def start(self, position: int, path=None):
        if path is None:
            path = [position]
        if len(path) == self.jump:  # ok, jump quota is finished
            self.size += 1
            print(path)
            return
        for i in jumps[position]:  # next jumps
            self.start(i, path + [i])


if __name__ == "__main__":
    l = L(10)
    l.start(0)
    print(l.size)
