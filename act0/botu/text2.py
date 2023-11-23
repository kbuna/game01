import pygame as pg
from pygame.locals import *
import sys

tmr = 0 

def main():
  global tmr
  pg.init()
  pg.display.set_caption("ゲーム")
  screen = pg.display.set_mode((800,600))
  clock = pg.time.Clock()

  while True:
    tmr += 1
    for e in pg.event.get():
      if e.type ==QUIT:
        pg.quit()
        sys.exit()
      elif e.type == KEYDOWN:
        if e.key == K_F1:
          screen = pg.display.set_mode((800,600),FULLSCREEN)
        if e.key == K_F2 or e.key == K_ESCAPE:
          screen = pg.display.set_mode((800,600))
    pg.display.update()
    clock.tick(15)

if __name__ == "__main__":
  main()