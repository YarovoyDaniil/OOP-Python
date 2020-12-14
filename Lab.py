class Fuel:
    def __init__(self, vol):
        self.__volume = vol

    def get_volume(self):
        return self.__volume

    def set_volume(self, v:int):
        self.__volume = v

class Wheels:
    __wheel_type = 'Classic steel wheel'

    def get_wheels_type(self):
        return self.__wheel_type

    def set_wheels_type(self,w:str):
        self.__wheel_type = w

def test(x):
    a = Fuel(x)
    print(a.get_volume())
    a.set_volume(67)
    print(a.get_volume())
    b = Wheels()
    print(b.get_wheels_type())
    b.set_wheels_type('Light alloy wheels')
    print(b.get_wheels_type())

test(25)