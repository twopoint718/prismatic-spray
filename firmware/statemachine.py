# Signals to be handled
from enum import Enum

class Signal(Enum):
    AdjustBrightness = 1
    ButtonDown = 2
    ButtonUp = 3
    IncrementHue = 4
    DecrementHue = 5

class StateMachine:
    def __init__(self, bsp):
        self.state = None
        self.bsp = bsp

    def transition(self, newState):
        self.state = newState

    # States are methods
    def initial_state(self):
        self.curr_hue = 0
        self.curr_brightness = 1.0
        self.transition(self.idle_state)

    def idle_state(self):
        pass

    def led_on_state(self):
        pass