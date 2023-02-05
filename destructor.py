import time

class Destructor:
    def __init__(self):
        print("Object Initialiation...")

    def __del__(self):
        print("Object Destruction...")

d1 = Destructor()

di = None

time.sleep(5)


print("Creating object...")