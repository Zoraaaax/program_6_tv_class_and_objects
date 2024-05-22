#  Constructor
class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    #  Method to turn on the TV
    def turn_on(self):
        self.on = True

    #  Method to turn off the TV
    def turn_off(self):
        self.on = False

    #  Method to set the channel in TV
    def set_channel(self, channel_no):
        if self.on and 1 <= channel_no <= 120:
            self.channel = channel_no

    #  Method to get the channel in TV
    def get_channel(self):
        return self.channel

    def set_volume_level(self, volume_no):
        if self.on and 1 <= volume_no <= 7:
            self.volume_level = volume_no

    def get_volume_level(self):
        return self.volume_level

    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1

    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    def volume_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1
