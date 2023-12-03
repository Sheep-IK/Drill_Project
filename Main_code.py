from pico2d import *
import random

P_speed = 6
P_max = 150

class bird:
    bird_image = None

    def __init__(self, x, y, cnt, flying_type=random.randint(1, 2), P_down=random.randint(55, 70)):
        if bird.bird_image == None:
            bird.bird_image = load_image('bird_long.png')
        print('새한마리 슈우웅')
        self.flying_type = flying_type
        self.x, self.y = x, y
        self.head = 0
        self.P_down = P_down

    def flying(self):
        if self.flying_type == 1:
            self.x, self.y = 0, 500  #캔버스
            self.y = random.randint(480, 550)
        else:
            self.x, self.y = 800, 500 #캔버스
            self.y = random.randint(480, 550)

    def draw(self):
        self.bird_image.draw(self.x, self.y)

    def plate_type(self):  # 왼쪽에서 오른쪽으로 이동
        if self.flying_type == 1:
            self.x += P_speed
        elif self.flying_type == 2:
            self.x -= P_speed


    def __del__(self):
        print("새 소멸")  # test

class plate:
    #__cnt = 0   #멤버 변수
    flying_image = None
    def __init__(self, x, y, cnt, flying_type = random.randint(1, 2),P_down = random.randint(55, 70)):
        if plate.flying_image == None:
            plate.flying_image = load_image('Made_Plate.png')
        print('비행접시 슈우웅')
        self.flying_type = flying_type
        self.x, self.y = x, y
        self.head = 0
        self.P_down = P_down


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
            if self.head <= self.P_down:
                self.x += P_speed
                self.y += 2
            elif self.head > self.P_down:
                self.x += P_speed
                self.y -= 2
        elif self.flying_type == 2:
            if self.head <= self.P_down:
                self.x -= P_speed
                self.y += 2
            elif self.head > self.P_down:
                self.x -= P_speed
                self.y -= 2

        self.head += 1





    def __del__(self):
        print("객체 소멸")  #test


#화면 크기 설정

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

start_base = load_image('Start Base.PNG')
grass_base = load_image('Base Grass.png')
close_up = load_image('Close Up Start.png')

shotgun_targeting_s = load_image('shotgun_targeting_s.png')
shotgun_targeting_m = load_image('aim_m.png')


#총기 이미지
#hand_gun = load_image('300HandGun_sheet.png')
hand_gun = load_image('BGHandGun_sheet.png')

#폰트
level_font = load_font('Ephesis-Regular.ttf', 60)
font = load_font('ENCR10B.TTF', 20)
score_font = load_font('ENCR10B.TTF', 40)

sign = load_image('sign.png') #표지판


#각종 사운드
click_sound = load_wav('click_sound.wav')
click_sound.set_volume(30)
Gun1_sound = load_wav('Gun1.wav')
Gun2_sound = load_wav('Gun2.wav')
Gun3_sound = load_wav('Gun3.wav')
Gun1_sound.set_volume(20)
Gun2_sound.set_volume(20)
Gun3_sound.set_volume(20)

start_sound = load_wav('classic.wav')
main_sound = load_wav('spring.wav')

low_score = load_wav('low_score.wav')
middle_score = load_wav('middle_score.wav')
high_score = load_wav('high_score.wav')

low_score.set_volume(50)
middle_score.set_volume(150)
high_score.set_volume(50)


mx, my = 0, 0
mx2, my2 = 0, 0

score = 0 #점수 계산
Move_Count_Timer = 0 #브레이킹 계산

cycle = True
maincheck = False
startpage = True
mainpage = False
endpage = False
Pck = False

Fbird = True
Bck = False
Plate_click = False
Shooting = False
Hand_Motion = False
targeting_move = False
Checking_mode = False
First_shoot = True

Easy_mode = True
Normal_mode = False
Hard_mode = False

Gun_mode1 = True
Gun_mode2 = False
Gun_mode3 = False

start_music = True
middle_music = False
end_sound = True

moveingP_point = 10
point = 15

start_timer = 0
TimeLimit = 60

BirdMotion = 0
MotionCount = 0
MotionDelay = 0

Count = 0


def handle_event():
    global mx,my,mx2,my2
    global startpage, mainpage, endpage
    global Easy_mode, Normal_mode, Hard_mode
    global Shooting
    global targeting_move
    global Move_Count_Timer
    global Checking_mode
    global Hand_Motion
    global start_timer
    global TimeLimit
    global score
    global Pck, Bck
    global Gun_mode1, Gun_mode2, Gun_mode3
    global First_shoot
    global end_sound
    global point
    global moveingP_point
    global P_speed
    global P_down
    global P_max

    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, CANVAS_HEIGHT - event.y
            if startpage == True and mx >= 200 and mx <= 610 and my >= 125 and my <= 400:
                click_sound.play()
                startpage = False
                mainpage = True
                start_timer = get_time()
            if mainpage == True:
                if First_shoot:
                    First_shoot = False
                else:
                    Shooting = True
                    Hand_Motion = True
                    Gun_sound()

            if startpage == True and mx >= 40 and mx <= 200 and my >= 30 and my <= 90:
                click_sound.play()
                Easy_mode = True
                Normal_mode = False
                Hard_mode = False
                moveingP_point = 10
                point = 15
                P_speed = 6
                P_max = 150
                print('Easy_mode')
            elif startpage == True and mx >= 300 and mx <= 480 and my >= 30 and my <= 90:
                click_sound.play()
                Easy_mode = False
                Normal_mode = True
                Hard_mode = False
                moveingP_point = 7
                point = 20
                P_speed = 8
                P_max = 120
                print('Normal_mode')
            elif startpage == True and mx >= 590 and mx <= 750 and my >= 30 and my <= 90:
                click_sound.play()
                Easy_mode = False
                Normal_mode = False
                Hard_mode = True
                moveingP_point = 5
                point = 30
                P_speed = 10
                P_max = 100

                print('Hard_mode')


        elif event.type == SDL_MOUSEMOTION:
            if mx != 0 and my != 0:
                mx2, my2 = mx, my

            mx, my = event.x, CANVAS_HEIGHT - event.y

        elif event.type == SDL_MOUSEBUTTONUP:
            Shooting = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            print('keydown')
            if not Checking_mode:
                Checking_mode = True
            elif Checking_mode:
                Checking_mode = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_q:
            if startpage == True or endpage == True:
                quit()
            else:
                mainpage = False
                endpage = True

        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            startpage = True
            mainpage = False
            endpage = False

            Pck = False
            Bck = False
            TimeLimit = 60
            score = 0
            First_shoot = True
            end_sound = True


        elif event.type == SDL_KEYDOWN and event.key == SDLK_g:
            if Gun_mode1:
                Gun_mode1 = False
                Gun_mode2 = True
                Gun2_sound.play()
            elif Gun_mode2:
                Gun_mode2 = False
                Gun_mode3 = True
                Gun3_sound.play()
            elif Gun_mode3:
                Gun_mode3 = False
                Gun_mode1 = True
                Gun1_sound.play()

def Gun_sound():
    if Gun_mode1:
        Gun1_sound.play()
    elif Gun_mode2:
        Gun2_sound.play()
    elif Gun_mode3:
        Gun3_sound.play()



start_sound.repeat_play()
main_sound.repeat_play()

while cycle:
    while startpage:
        start_sound.set_volume(32)
        main_sound.set_volume(0)
        clear_canvas()
        start_base.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        level_font.draw(50, 60, f'Easy!', (0, 0, 0))
        level_font.draw(CANVAS_WIDTH // 2 - 100, 60, f'Normal!', (0, 0, 0))
        level_font.draw(CANVAS_WIDTH - 200, 60, f'Hard!', (0, 0, 0))

        handle_event()
        if mx >= 200 and mx <= 610 and my >= 125 and my <= 400:
              if maincheck == False:
                close_up.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
                level_font.draw(50, 60, f'Easy!', (0, 0, 0))
                level_font.draw(CANVAS_WIDTH // 2 - 100, 60, f'Normal!', (0, 0, 0))
                level_font.draw(CANVAS_WIDTH - 200, 60, f'Hard!', (0, 0, 0))
                #print('maincheck') #test

        if Easy_mode:
            draw_rectangle(40, 30, 200, 90)
        elif Normal_mode:
            draw_rectangle(300, 30, 480, 90)
        elif Hard_mode:
            draw_rectangle(590, 30, 750, 90)



        update_canvas()
        delay(0.1)


    while mainpage:
        start_sound.set_volume(0)
        main_sound.set_volume(36)
        #print(middle_music)


        global plate_gather
        global flying_type
        # print('running') #test
        clear_canvas()
        grass_base.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)


        #타이머 생성
        leftTime = TimeLimit - get_time() + start_timer
        if leftTime < 0:
            mainpage = False
            endpage = True

        font.draw(10, CANVAS_HEIGHT - 10, f'(Time: {leftTime:.2f})', (0, 0, 0))

        #점수판 생성
        font.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT - 10, f'(Score : {score})', (0, 0, 0))


        if Fbird:
            Bird = bird(0, 500, 1, random.randint(1, 2))
            Fbird = False

        if Count >= 2 and Bck == False:
            Bird = bird(0, 500, 1, random.randint(1, 2))
            Bird.plate_type()
            Bird.flying()
            Count = 0
            Bck = True
            print('Bird 생성완료')


        if Bird.head >= 3 * P_max:
            Bck = False


        if Bck:
            if BirdMotion == 13:
                BirdMotion = 0
            else:
                BirdMotion += 1
            Bird.head += 1

            if Bird.flying_type == 1:
                Bird.bird_image.clip_draw(BirdMotion*145, 0, 145, 125, Bird.x, Bird.y, 70, 70)
                Bird.x += 4
            else:
                Bird.bird_image.clip_composite_draw(BirdMotion * 145, 0, 145, 125, 0, 'h', Bird.x, Bird.y, 70, 70)
                Bird.x -= 4

        #원판 날아오기
        if Pck == False:
            Count += 1
            Plate = plate(0, 400, 1, random.randint(1, 2))
            Plate.flying()
            print('원판 생성완료')
            Pck = True
            Plate_click = False
            Plate.P_down -= random.randint(-10, 10)

            if Easy_mode:
                pass
            elif Normal_mode:
                Plate.P_down -= 10
            elif Hard_mode:
                Plate.P_down -= 20

        Plate.plate_type()


        #print(Plate.head) #test
        if Plate.head == P_max:
            plate.__del__(Plate)
            Pck = False

        plate.draw(Plate)

        #사격 코드
        handle_event()

        if Hand_Motion: #사격 모션 코드
            hand_gun.clip_draw(MotionCount*115, 0, 115, 185, CANVAS_WIDTH // 2 + 100, 100, 255, 300)
            if MotionDelay < 1:
                MotionDelay += 1
            else:
                MotionDelay = 0
                MotionCount += 1

            if MotionCount == 14:
                MotionCount = 0
                Hand_Motion = False
        else:
            hand_gun.clip_draw(0, 0, 115, 185, CANVAS_WIDTH // 2 + 100, 100, 255, 300)

        if mx - 15 < mx2 and mx + 15 > mx2 and my - 15 < my2 and my + 15 > my2:
            Move_Count_Timer += 1
            if Move_Count_Timer == 10:  # 브레이킹이 걸리는데까지 소요시간
                targeting_move = False
                shotgun_targeting_s.draw(mx, my)
                Move_Count_Timer = 0

        else:
            shotgun_targeting_m.draw(mx, my)
            targeting_move = True
            Move_Count_Timer = 0

        # print(targeting_move) #test
        # print(mx, mx2, my, my2) #test
        # print(Move_Count_Timer)  # test
        if targeting_move == True:
            shotgun_targeting_m.draw(mx, my)
        else:
            shotgun_targeting_s.draw(mx, my)

        #사격 충돌 체크

        if targeting_move == True:
            if Plate.x - 10 < mx and Plate.x + 10 > mx and Plate.y - 5 < my and Plate.y + 5 > my and Plate_click == False and Shooting == True:
                print('원판 사격 명중!')
                score += moveingP_point
                print(score)
                Plate_click = True
                Pck = False
                Shooting = False
        elif targeting_move == False:
            if Plate.x - 50 < mx and Plate.x + 50 > mx and Plate.y -27 < my and Plate.y + 27 > my and Plate_click == False and Shooting == True:
                # draw_rectangle(Plate.x - 50 , Plate.y - 27, Plate.x+ 50, Plate.y + 27) #test
                print('원판 사격 명중!')
                score += point
                print(score)
                Plate_click = True
                Pck = False
                Shooting = False

        #print(Checking_mode) #test
        #Test Box
        if Checking_mode == True:
            if targeting_move == True:
                draw_rectangle(Plate.x - 10, Plate.y - 5, Plate.x + 10, Plate.y + 5)  # test
            else:
                draw_rectangle(Plate.x - 50, Plate.y - 27, Plate.x + 50, Plate.y + 27)  # test

        update_canvas()
        delay(0.02)


    while endpage:
        grass_base.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
        if end_sound == True:
            end_sound = False
            if score >= 300:
                high_score.play()
            elif score < 300 and score >= 100:
                middle_score.play()
            elif score < 100:
                low_score.play()



        sign.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2 - 100, CANVAS_WIDTH, CANVAS_HEIGHT)
        if score >= 300:
            score_font.draw(CANVAS_WIDTH // 2 - 120, CANVAS_HEIGHT // 2, f'Excellent!!', (255, 0, 0))
            score_font.draw(CANVAS_WIDTH // 2 - 120, CANVAS_HEIGHT // 2 - 40, f'"{score}"point!', (0, 0, 255))
        elif score < 300 and score >= 100:
            score_font.draw(CANVAS_WIDTH // 2 - 50, CANVAS_HEIGHT // 2, f'Great!!', (255, 0, 0))
            score_font.draw(CANVAS_WIDTH // 2 - 100, CANVAS_HEIGHT // 2 - 40, f'"{score}"point!', (0, 0, 255))
        elif score < 100:
            score_font.draw(CANVAS_WIDTH // 2 - 180, CANVAS_HEIGHT // 2, f'Are you a human..?? ', (255, 0, 0))
            score_font.draw(CANVAS_WIDTH // 2 - 120, CANVAS_HEIGHT // 2 - 40, f'"{score}"point!', (0, 0, 255))
        handle_event()
        update_canvas()
        delay(0.02)



