from pico2d import *
import random

class grass:
    def _init_(self):
     self.image = load_image('grass.png')
    def draw(self):
       self.image.draw(400,30)
    def update(self): pass


class Boy:
   def _init_(self):
      self.x, self.y = random.randiant(100, 700), 90
      self.image = load
