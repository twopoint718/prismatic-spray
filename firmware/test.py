import unittest
# from statemachine import StateMachine, IncrementHue, DecrementHue, ButtonDown
import statemachine as sm

class MockBSP():
    def __init__(self):
        self.hues = [(i,i,i) for i in range(0,23)] # pseudo-"colors"
        self.pixel = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
    
    def led_on(self, n, hue, brightness=1):
        print("LED_ON")
        self.pixel[n] = self.hues[hue]

    def led_off(self, n):
        self.pixel[n] = (0,0,0)

class TestState(unittest.TestCase):
    def test_transitions_to_idle_state(self):
        bsp = MockBSP()
        sut = sm.StateMachine(bsp)
        
        self.assertEqual(sut.idle_state, sut.get_state())

    def test_initial_focused_pixel(self):
        bsp = MockBSP()
        sut = sm.StateMachine(bsp)

        self.assertEqual(0, sut.curr_pixel)

    def test_turn_on_led(self):
        bsp = MockBSP()
        sut = sm.StateMachine(bsp)

        sut.dispatch(sm.IncrementHue(0))
        sut.dispatch(sm.ButtonDown(0))
        
        self.assertEqual(sut.led_on_state, sut.get_state())
        self.assertEqual((1,1,1), bsp.pixel[0])

    def test_decrement_wraparound(self):
        bsp = MockBSP()
        sut = sm.StateMachine(bsp)

        sut.dispatch(sm.DecrementHue(0))
        
        self.assertEqual(23, sut.get_focus())

if __name__ == '__main__':
    unittest.main()