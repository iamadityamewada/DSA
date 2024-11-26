class Phone:
    def __init__(self):
        self.name = "nokia"
        print("Basic phone init")

    def calling(self):
        print("Calling")

    def text(self):
        print("texting")


class Smartphone(Phone):
    def __init__(self):
        print("SmartPhone init")
        # super().__init__()

    def video_call(self):
        print("Video Calling")

class Samsung(Smartphone):
    def __init__(self):
        print("Samsung init")
        super().__init__()
        Phone.__init__(self)

    def biometrics(self):
        print("Add finger print")    


sm = Samsung()


# sm.calling()
# sm.video_call()
# sm.biometrics()


# Sp = Smartphone()
# Sp.calling()
# # bp = Phone()

