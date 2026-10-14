from pico2d import *
import random

# Game object class here

speed = random.randint(5, 20)
size = random.randint(100, 400)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass

class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.r = self.image.w // 2          
        self.x, self.y = random.randint(100, 700), 50 + self.r
        self.vx, self.vy = 0.0, 0.0
    def draw(self):
            self.image.draw(self.x, self.y)
        
    def update(self): 
         self.y += speed
         if self.y>= 400:
             self.y=390
                               
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.image = load_image('run_animation.png')
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def reset_world():
    global running
    global world
    running = True
    world = []
    grass = Grass()

    world.append(grass)
    team = [Boy() for i in range(11)]
    team2 = [Ball() for i in range(20)]
    world += team, team2


def update_world():
    for o in world: o.update()

def render_world():
 clear_canvas()
 for o in world:
  o.draw()
 update_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

reset_world()
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
