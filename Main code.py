from pico2d import *
import random

class plate:
    #__cnt = 0   #멤버 변수
    flying_image = None
    def __init__(self, x, y, cnt, flying_type = random.randint(1, 2)):
        if plate.flying_image == None:
            plate.flying_image = load_image('Made_Plate.png')
        print('비행접시 슈우웅')
        self.flying_type = flying_type
        self.x, self.y = x, y
        self.head = 0

    def flying(self):
        if self.flying_type == 1:
            #self.x, self.y = 0, 300  #캔버스
            self.x, self.y = 0, random.randint(270, 400)  #test
        else:
            #self.x, self.y = 800, 300 #캔버스
            self.x, self.y = 800, random.randint(270, 400)  # test

    def draw(self):
        self.flying_image.draw(self.x, self.y)

    def plate_type(self):  # 왼쪽에서 오른쪽으로 이동

        if self.flying_type == 1:
            if self.head <= 60:
                self.x += 8
                self.y += 2
            elif self.head > 60:
                self.x += 8
                self.y -= 2
        elif self.flying_type == 2:
            if self.head <= 60:
                self.x -= 8
                self.y += 2
            elif self.head > 60:
                self.x -= 8
                self.y -= 2

        self.head += 1





    def __del__(self):
        print("객체 소멸")  #test




# def plate_type2(x, y):  # 오른쪽에서 왼쪽으로 이동
#     global head
#
#     while head <= 160:
#         if head <= 80:
#             x -= 5
#             y += 2
#         elif head > 80:
#             x -= 5
#             y -= 2
#
#         plate.draw(Plate)
#         head += 1


#화면 크기 설정

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

start_base = load_image('Start Base.PNG')
grass_base = load_image('Base Grass.png')
close_up = load_image('Close Up Start.png')

shotgun_targeting_s = load_image('shotgun_targeting_s.png')

#shotgun_targeting_m = load_image('shotgun_targeting_m.png')
shotgun_targeting_m = load_image('aim_m.png')


#총기 이미지


mx, my = 0, 0
mx2, my2 = 0, 0

score = 0 #점수 계산
Move_Count_Timer = 0 #브레이킹 계산

maincheck = False
start = True
mainpage = False
Pck = False
Plate_click = False
Shooting = False
targeting_move = False

def handle_event():
    global mx,my,mx2,my2
    global start, mainpage
    global Shooting
    global targeting_move
    global Move_Count_Timer

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, CANVAS_HEIGHT - event.y
            if start == True:
                start = False
                mainpage = True
            Shooting = True

        elif event.type == SDL_MOUSEMOTION:
            if mx != 0 and my != 0:
                mx2, my2 = mx, my

            mx, my = event.x, CANVAS_HEIGHT - event.y

        elif event.type == SDL_MOUSEBUTTONUP:
            Shooting = False


while start:
    clear_canvas()
    start_base.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    handle_event()
    if mx >= 200 and mx <= 610 and my >= 125 and my <= 400:
          if maincheck == False:
            close_up.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            print(maincheck)


    update_canvas()
    delay(0.1)

#Plate = plate(0, 400, 1, random.randint(1, 2))
#Plate.flying()
while mainpage:

    global plate_gather
    global flying_type
    # print('running') #test
    clear_canvas()
    grass_base.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)

    #원판 날아오기
    if Pck == False:
        Plate = plate(0, 400, 1, random.randint(1, 2))
        Plate.flying()
        print('원판 생성완료')
        Pck = True
        Plate_click = False

    Plate.plate_type()


    #print(Plate.head) #test
    if Plate.head == 120:
        plate.__del__(Plate)
        Pck = False

    plate.draw(Plate)
    # plate_gather = [plate() for i in range(10)]

    #사격 코드
    handle_event()
    if mx - 15 < mx2 and mx + 15 > mx2 and my - 15 < my2 and my + 15 > my2:
        Move_Count_Timer += 1
        if Move_Count_Timer == 7:  # 브레이킹이 걸리는데까지 소요시간
            targeting_move = False
            shotgun_targeting_s.draw(mx, my)
            Move_Count_Timer = 0

    else:
        shotgun_targeting_m.draw(mx, my)
        targeting_move = True
        Move_Count_Timer = 0

    # print(targeting_move) #test
    # print(mx, mx2, my, my2) #test
    print(Move_Count_Timer)  # test
    if targeting_move == True:
        shotgun_targeting_m.draw(mx, my)
    else:
        shotgun_targeting_s.draw(mx, my)

    #사격 충돌 체크


    if Plate.x - 50 < mx and Plate.x + 50 > mx and Plate.y -27 < my and Plate.y + 27 > my and Plate_click == False and Shooting == True:
        # draw_rectangle(Plate.x - 50 , Plate.y - 27, Plate.x+ 50, Plate.y + 27) #test
        print('원판 사격 명중!')
        score += 10
        print(score)
        Plate_click = True
        Pck = False
        Shooting = False



    update_canvas()
    delay(0.02)




