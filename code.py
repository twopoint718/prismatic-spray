from machine import ADC, Pin
import math
import neopixel
import time

button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Pin: 32, ADC1, GP27
hueInput = ADC(Pin(27))

# NeoPixel (WS2812)
num_pixels = 1
# Pin: 21, GP16
pixel = neopixel.NeoPixel(Pin(16), num_pixels)
pixel.brightness = 0.3

def getHue(pin):
    return pin.read_u16() / 65535 * 360

def hToRGB(H, S=1, L=0.5):
    C = 1
    X = 1 - math.fabs((H / 60.0) % 2 - 1)
    m = L - C/2.0
    r = 0
    g = 0
    b = 0
    if H >= 0 and H < 60:
        r, g, b = (C, X, 0)
    elif H >= 60 and H < 120:
        r, g, b = (X, C, 0)
    elif H >= 120 and H < 180:
        r, g, b = (0, C, X)
    elif H >= 180 and H < 240:
        r, g, b = (0, X, C)
    elif H >= 240 and H < 300:
        r, g, b = (X, 0, C)
    else:
        r, g, b = (C, 0, X)
    return (int(r * 255), int(g * 255), int(b * 255))

h = 0
while True:
    h = getHue(hueInput)
    if button.value() == 1:
        rgb = hToRGB(h)
        pixel.fill(rgb)
    else:
        pixel.fill((0,0,0))
    pixel.write()
    time.sleep(0.1)
