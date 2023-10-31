from pico2d import *
import random

class plate:
    #__cnt = 0   #멤버 변수
    flying_image = None
    def __init__(self, x, y, cnt):
        if plate.flying_image == None:
            plate.flying_image = load_image('Flying Disk.png')
        print('비행접시 슈우웅')
        self.flying_type = random.randint(1,2)

    def flying(self, x, y):
        if self.flying_type == 1:
            self.x, self.y = 0, 300  #캔버스
        else
            self.x, self.y = 800, 300 #캔버스

    def draw(self):
        self.flying_image.draw(self.x, self.y)

    def __del__(self):
        print("객체 소멸")


Plate_Number = 20
Plate_count = 1


while Plate_count < Plate_Number:
    plate(__cnt=Plate_count)
    Plate_count += 1


