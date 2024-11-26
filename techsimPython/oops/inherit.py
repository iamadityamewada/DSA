class Phone:
    def __init__(self):
        print("Basic phone init")

    def calling(self):
        print("Calling")

    def text(self):
        print("texting")

class Smartphone(Phone):
    def __init__(self):
        print("SmartPhone init")

    def video_call(self):
        print("Video Calling")

class Samsung(Smartphone):
    def __init__(self):
        print("Samsung init")

    def biometrics(self):
        print("Add finger print")    


sm = Samsung()
sm.calling()
sm.video_call()
sm.biometrics()
# Sp = Smartphone()
# Sp.calling()
# # bp = Phone()

