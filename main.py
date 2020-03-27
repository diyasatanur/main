# import packages
import pygame, random 
from pygame.locals import *
from sprite_loader import Spritesheet
from cat import Cat

# initialize game
pygame.init()

# initialize screen
screen_info = pygame.display.Info()
size = (width, height) = (800,600)
screen = pygame.display.set_mode(size)

#initialize clock 
clock = (0, 125, 0)

#initialize a background color 
color = (0, 125, 0)

cat_images = []

def get_cat_images(): 
  cat_sheet = SpriteSheet("cat.png")
  cat_sheet_width = cat_sheet.sprite_sheet.get_rect().width
  cat_sheet_height = cat_sheet.sprite.get_rect().height
  nrows = 4
  ncols = 2
  cat_width = cat_sheet_width / ncols 
  cat_height = cat_sheet_height / nrows
  #get cat images
  for row in range(nrows):
    for row in range(ncols): 
      cat_images.append(cat_sheet.get_image(
        col * cat_width, 
        row * cat_height, 
        cat_width, 
        cat_height
      ))
      scale = 0.5
      cat_images[-1] = pygame.transform.smoothscale(
        cat_images[-1], 
        (int(cat_width*scale), int(cat_height*scale))
      )


screen_info = pygame.display.Info()
size = (width, height) = (800, 600)
screen = pygame.display.set_mode(size)

# initialize clock 
clock = pygame.time.Clock()

# initialize a background color
color = (0, 125, 0)


def main():
  get_cat_images()
  cat = Cat((-90, random.randint(50, height-50)), cat_images)
  while True:
    clock.tick(60)
    cat.update()
    screen.fill(color)
    cat.draw(screen)
    pygame.display.flip() 

if __name__ == "__main__":
   main()