from machine import ADC, Pin
import math
import micropython
import neopixel
import time
import utime
micropython.alloc_emergency_exception_buf(100)

################################################################################
# States

class State():
    IDLE = 0
    BUTTON_UP = 1
    BUTTON_DOWN = 2
    FAILURE = 3

# initial global state
state = State.IDLE

################################################################################
# Configure I/O Pins & Globals

# Pin: 19, GP14
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Pin: 32, ADC1, GP27
hueInput = ADC(Pin(27))

# Pin: 25, on-board LED
onboard_led = Pin(25, Pin.OUT)

# NeoPixel (WS2812)
num_pixels = 1
# Pin: 21, GP16
pin = Pin(16, Pin.OUT)
pixel = neopixel.NeoPixel(Pin(16), num_pixels)
pixel.fill((0, 0, 0))
pixel.write()

################################################################################
# Function defs

def getHue(p):
    return p.read_u16() / 65535 * 360

def hsl2rgb(H, S=1, L=0.5):
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

def toggleLed():
    pass

toggle = True
def onButtonPress(pin):
    global state
    if state == State.IDLE:
        state = State.BUTTON_DOWN
        return
    if state == State.BUTTON_DOWN:
        state = State.BUTTON_UP
        return

################################################################################
# Main

# Setup
button.irq(handler=onButtonPress, trigger=(Pin.IRQ_RISING or Pin.IRQ_FALLING))

while True:
    if state == State.IDLE:
        # Enter lower-power mode when there's nothing to do 
        machine.idle()
    elif state == State.BUTTON_DOWN:
        rgb = hsl2rgb(getHue(hueInput))
        pixel.fill(rgb)
        pixel.write()
        utime.sleep(0.1)
    elif state == State.BUTTON_UP:
        pixel.fill((0, 0, 0))
        pixel.write()
        state = State.IDLE
    else:
        # Turn on LED to signal possible problem
        onboard_led.value(1)

