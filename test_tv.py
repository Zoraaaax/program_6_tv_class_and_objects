#  Import the TV class from the tv module
from tv import TV


#  Define class TestTV
class TestTV:

    #  Define method 'test_tv' in 'TestTV' class
    def test_tv(self):
        # Create an Object
        tv1 = TV()
        tv2 = TV()

        # Use the 'turn_on' method on 'tv1' and 'tv2
        tv1.turn_on()
        tv2.turn_on()

        # Use the 'set_channel' method on 'tv1' and 'tv2
