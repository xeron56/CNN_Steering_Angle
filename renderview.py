import numpy as np
import pandas as pd
import pygame
import glob
from config import VisualizeConfig


#-------------------------------
#defining colour
#---------------------------------
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

config = VisualizeConfig()

preds = pd.read_csv(config.pred_path)

filenames = glob.glob(config.img_path)


pygame.init()
size = (840, 520)
pygame.display.set_caption("steering angle prediction")
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
myfont = pygame.font.SysFont("monospace", 20)

for i in range(1000):

    angle = preds["steering_angle"].iloc[i] # radians
  
    
    # add image to screen
    img = pygame.image.load(filenames[i])
    screen.blit(img, (0, 0))
    
    sidetext1=myfont.render("Steer left",1,(0,255,0))
    sidetext2=myfont.render("Steer right",1,(0,255,0))
    sidetext3=myfont.render("Steer forward",1,(0,255,0))

    if angle* 57.2958 > 0 :
        screen.blit(sidetext1,(13,270))

    if angle* 57.2958 < 0 :
       screen.blit(sidetext1,(15,260))  
      
    if angle* 57.2958 == 0:
       screen.blit(sidetext1,(18,250))

    # add text
    pred_txt = myfont.render("Prediction: " + str(round(angle* 57.2958, 3)), 1, (255,255,0)) # angle in degrees
    
      

    screen.blit(pred_txt, (10, 280))

   

    # draw steering wheel
    radius = 50
    pygame.draw.circle(screen, WHITE, [320, 300], radius, 2)
    pygame.draw.circle(screen, WHITE, [320, 300], radius, 3)  

    
    
    # draw cricle for predicted angle
    x = radius * np.cos(np.pi/2 + angle)
    y = radius * np.sin(np.pi/2 + angle)
    pygame.draw.circle(screen, GREEN, [320 + int(x), 300 - int(y)], 5) 
    
    pygame.display.update()
    pygame.display.flip()
    pygame.time.delay(23)
    