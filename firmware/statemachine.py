# Events to be handled
class Event:
    def __init__(self, value):
        self.value = value

class AdjustBrightness(Event): pass
class ButtonDown(Event): pass
class ButtonUp(Event): pass
class IncrementHue(Event): pass
class DecrementHue(Event): pass

class StateMachine:
    def __init__(self, bsp):
        # Extended state variables
        self.curr_pixel = 0
        self.curr_brightness = 1.0
        self.pixels = [0, 0, 0, 0]

        # State machine internal variables
        self.__state = None
        self.__bsp = bsp

        self.transition(self.idle_state)

    def get_state(self):
        return self.__state

    def get_focus(self):
        return self.pixels[self.curr_pixel]

    def set_focus(self, n):
        self.pixels[self.curr_pixel] = n

    def inc_focus(self):
        n = self.get_focus() + 1
        if n > 23:
            self.set_focus(0)
        else:
            self.set_focus(n)

    def dec_focus(self):
        n = self.get_focus() - 1
        if n < 0:
            self.set_focus(23)
        else:
            self.set_focus(n)

    def dispatch(self, event: Event):
        """Send the incoming event to the current state. The event subclass will
        have any arguments expected by that handler."""
        self.__state(event)

    def transition(self, newState):
        self.__state = newState

################################################################################
## STATES

    def idle_state(self, event: Event):
        if type(event) == IncrementHue:
            self.curr_pixel = event.value
            self.inc_focus()
        elif type(event) == DecrementHue:
            self.curr_pixel = event.value
            self.dec_focus() 
        elif type(event) == ButtonDown:
            self.curr_pixel = event.value
            self.__bsp.led_on(self.curr_pixel, self.pixels[self.curr_pixel])
            self.transition(self.led_on_state)
        else:
            # TODO: testing only?
            raise NotImplementedError()

    def led_on_state(self, event: Event):
        if type(event) == ButtonUp:
            self.curr_pixel = event.value
            self.__bsp.led_off(self.curr_pixel)
            self.transition(self.idle_state)
