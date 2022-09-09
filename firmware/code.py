from bsp import BSP
from statemachine import StateMachine
import micropython

micropython.alloc_emergency_exception_buf(100)

# Create new BSP instance, initialize all peripherals
bsp = BSP()
fsm = StateMachine(bsp)
# TODO: run state machine