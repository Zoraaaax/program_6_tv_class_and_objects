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

        # Use the 'set_channel' and 'set_volume_level' method on 'tv1'
        tv1.set_channel(3)
        tv1.set_volume_level(4)

        # Use the 'set_channel' and 'set_volume_level' method on 'tv2'
        tv2.set_channel(2)
        tv2.set_volume_level(5)

        #  Print the channel and volume level of 'tv1' and 'tv2'
        print(f"tv1's channel is {tv1.get_channel()} and volume level is {tv1.get_volume_level()}")
        print(f"tv2's channel is {tv2.get_channel()} and volume level is {tv2.get_volume_level()}")


#  Run Test
TestTV().test_tv()
