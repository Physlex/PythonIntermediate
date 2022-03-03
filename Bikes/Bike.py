
class Bike :
    def __init__(self, colour:str, frameMat:str) :
        self.colour = colour
        self.frameMat = frameMat
        return

    def drive(self) -> None :
        print("Vrroooooom")
        print("Wow! Was that a %s bike made of %s material??" % (self.colour, self.frameMat))
        return

bike = Bike("Red", "Rubber")
bike.drive()