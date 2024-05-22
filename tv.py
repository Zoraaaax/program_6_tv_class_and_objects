#  Constructor
class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    #  Method to turn on the TV
    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def set_channel(self, channel_no):
        if self.on and 1 <= channel_no <= 120:
            self.channel = channel_no

    def get_channel(self):
        return self.channel

    def set_volume_level(self, volume_no):
        if self.on and 1 <= volume_no <= 7:
            self.volume_level = volume_no
