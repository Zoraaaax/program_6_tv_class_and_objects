#  Constructor
class TV:
    def __int__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

    #  Method to turn on the TV
    def turn_on(self):
        self.on = True
        
