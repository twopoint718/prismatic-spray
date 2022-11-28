LAST_PIXEL = None

class Pixel:
    def __init__(self):
        self.color = (0, 0, 0)

    def fill(self, color):
        self.color = color

    def write(self):
        global LAST_PIXEL
        LAST_PIXEL = self.color

class NeoPixel():
    def __init__(self, pin, num_leds):
        self.pin = pin
        self.num_leds = num_leds
        self.arr = [Pixel() for _i in range(num_leds)]

    def __getitem__(self, key):
        return self.arr[key]
