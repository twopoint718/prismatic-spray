import unittest
import statemachine
import bsp
import mock_neopixel
import mock_machine

class MockBSP():
    def __init__(self):
        self.hues = [(i,i,i) for i in range(0,23)] # pseudo-"colors"
        self.pixel = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
    
    def led_on(self, n, hue, brightness=1):
        self.pixel[n] = self.hues[hue]

    def led_off(self, n):
        self.pixel[n] = (0,0,0)

class TestState(unittest.TestCase):
    def test_transitions_to_idle_state(self):
        bsp = MockBSP()
        sut = statemachine.StateMachine(bsp)
        
        self.assertEqual(sut.idle_state, sut.get_state())

    def test_initial_focused_pixel(self):
        bsp = MockBSP()
        sut = statemachine.StateMachine(bsp)

        self.assertEqual(0, sut.curr_pixel)

    def test_turn_on_led(self):
        bsp = MockBSP()
        sut = statemachine.StateMachine(bsp)

        sut.dispatch(statemachine.IncrementHue(0))
        sut.dispatch(statemachine.ButtonDown(0))
        
        self.assertEqual(sut.led_on_state, sut.get_state())
        self.assertEqual((1,1,1), bsp.pixel[0])

    def test_decrement_wraparound(self):
        bsp = MockBSP()
        sut = statemachine.StateMachine(bsp)

        sut.dispatch(statemachine.DecrementHue(0))
        
        self.assertEqual(23, sut.get_focus())

    def test_increment_wraparound(self):
        bsp = MockBSP()
        sut = statemachine.StateMachine(bsp)
        for i in range(23):
            sut.dispatch(statemachine.IncrementHue(0))
        
        self.assertEqual(23, sut.get_focus())
        sut.dispatch(statemachine.IncrementHue(0))
        self.assertEqual(0, sut.get_focus())

class TestBSP(unittest.TestCase):
    def test_dummy(self):
        sut = bsp.BSP(mock_neopixel, mock_machine)

        sut.led_on(0, 0)

        self.assertEqual((255, 0, 0), mock_neopixel.LAST_PIXEL)
        
if __name__ == '__main__':
    unittest.main()