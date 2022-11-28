class Pin:
    IN = 'IN'
    OUT = 'OUT'
    PULL_DOWN = 'PULL_DOWN'

    def __init__(self, num, direction = OUT, up_down = None) -> None:
        self.num = num
        self.direction = direction
        self.up_down = up_down