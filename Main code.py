from pico2d import *

#화면 크기 설정

CANVAS_WIDTH, CANVAS_HEIGHT = 800, 600
open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

start_base = load_image('Start Base.PNG')
grass_base = load_image('Base Grass.png')
close_up = load_image('Close Up Start.png')

mx, my = 0, 0
click = False
start = True
running = False
def handle_event():
    global mx,my
    global start, running
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            mx, my = event.x, CANVAS_HEIGHT - event.y
            start = False
            running = True
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, CANVAS_HEIGHT - event.y




while start:
    clear_canvas()
    start_base.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    handle_event()
    if mx >= 200 and mx <= 610 and my >= 125 and my <= 400:
          if click == False:
            close_up.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
            print(click)


    update_canvas()
    delay(0.1)

while running:
    print('running')
    clear_canvas()
    grass_base.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)


    update_canvas()
    delay(0.05)

