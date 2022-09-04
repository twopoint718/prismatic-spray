from machine import ADC, Pin
import micropython
import neopixel

micropython.alloc_emergency_exception_buf(100)

# 24 precomputed hues as RGB. Each value is 15 degrees (360/24) separated in
# degrees of hue. These values can be passed directly to the neopixel fill func. 
HUES = [
    (255, 0, 0),   (255, 63, 0),  (255, 127, 0), (255, 191, 0),
    (255, 255, 0), (191, 255, 0), (127, 255, 0), (63, 255, 0),
    (0, 255, 0),   (0, 255, 63),  (0, 255, 127), (0, 255, 191),
    (0, 255, 255), (0, 191, 255), (0, 127, 255), (0, 63, 255),
    (0, 0, 255),   (63, 0, 255),  (127, 0, 255), (191, 0, 255),
    (255, 0, 255), (255, 0, 191), (255, 0, 127), (255, 0, 63)
]
NUM_HUES = 24

class BSP:
    def __init__(self):
        # Buttons
        self.button0 = Pin(14, Pin.IN, Pin.PULL_DOWN)
        # self.button1 = Pin(??, Pin.IN, Pin.PULL_DOWN) 
        # self.button2 = Pin(??, Pin.IN, Pin.PULL_DOWN) 
        # self.button3 = Pin(??, Pin.IN, Pin.PULL_DOWN) 

        # Pin: 32, ADC1, GP27
        self.hueInput = ADC(Pin(27))

        # Pin: 25, on-board LED
        self.onboard_led = Pin(25, Pin.OUT)

        # NeoPixel (WS2812)
        self.num_pixels = 4
        # Pin: 21, GP16
        Pin(16, Pin.OUT)
        self.pixel = neopixel.NeoPixel(Pin(16), self.num_pixels)

    def increment_hue(self):
        self.curr_hue += 1
        if self.curr_hue >= NUM_HUES:
            self.curr_hue = 0

    def decrement_hue(self):
        self.curr_hue -= 1
        if self.curr_hue < 0:
            self.curr_hue = NUM_HUES-1
        
    def led_on(self, n, hue, brightness=1):
        self.pixel[n].fill(HUES[hue])
        self.pixel[n].write()

    def led_off(self, n):
        self.pixel[n].fill((0,0,0))
        self.pixel[n].write()