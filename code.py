import micropython
from statemachine import StateMachine
micropython.alloc_emergency_exception_buf(100)

# Create new BSP instance, initialize all peripherals
bsp = BSP()
fsm = StateMachine(bsp)
fsm.run()