# States
IDLE = "IDLE"
LED_0_ON = "LED_0_ON"
LED_1_ON = "LED_1_ON"
LED_2_ON = "LED_2_ON"
LED_3_ON = "LED_3_ON"

HUE_ADJUST = "HUE_ADJUST"

class StateMachine:
    def __init__(self, bsp):
        self.state = "INIT"
        self.bsp

    def run(self):
        while True:
            if self.state == IDLE:
                # BSP() constructor handles init
                pass
            elif self.state == LED_0_ON:
                self.bsp.led_on(0)
            elif self.state == LED_1_ON:
                self.bsp.led_on(1)
            elif self.state == LED_2_ON:
                self.bsp.led_on(2)
            elif self.state == LED_3_ON:
                self.bsp.led_on(3)
            elif self.state == HUE_ADJUST:
                pass
            else:
                pass