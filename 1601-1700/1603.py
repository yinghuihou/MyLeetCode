# Definition for singly-linked list.

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bigNum = big
        self.midNum = medium
        self.smallNum = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.bigNum >= 1:
                self.bigNum -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.midNum >= 1:
                self.midNum -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.smallNum >= 1:
                self.smallNum -= 1
                return True
            else:
                return False
def main():
    object = ParkingSystem(1,1,1)
    print(object.addCar(1))
    print(object.addCar(1))



if __name__ == '__main__':
    main()
