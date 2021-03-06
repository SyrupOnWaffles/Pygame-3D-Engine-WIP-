from pygame import *
from pygame import gfxdraw
import pygame, model6, model5, model4, model7
import numpy as np

xAngle = np.deg2rad(180)
yAngle = np.deg2rad(0)
zAngle = np.deg2rad(0)
screenSize = [256, 256]
class colours:
    black = (40,40,46)
    purple = (108,86,113)
    grey = (217,200,191)
    red = (249,130,132)
    light_purple = (176,169,228)
    blue = (172,204,228)
    teal = (179,227,218)
    pink = (254,170,228)
    dark_green = (135,168,137)
    green = (176,235,147)
    light_green = (233,245,157)
    tan = (255,230,198)
    brown = (222,163,139)
    orange = (255,195,132)
    yellow = (255,247,160)
    white = (255,247,228)
orthProjection = [[1, 0, 0], [0, 1, 0],[0,0,0]]

xRotation = [[1, 0, 0],
                [0, np.cos(xAngle), -np.sin(xAngle)],
                [0, np.sin(xAngle), np.cos(xAngle)]]

yRotation = [[np.cos(yAngle), 0, np.sin(yAngle)],
                [0, 1, 0],
                [-np.sin(yAngle), 0, np.cos(yAngle)]]

zRotation = [[np.cos(zAngle), -np.sin(zAngle), 0],
                [np.sin(zAngle), np.cos(zAngle), 0],
                [0, 0, 1]]    


background_colour = colours.black

screen = pygame.display.set_mode((screenSize[0], screenSize[1]), SCALED, 1)

texture = pygame.image.load("texture.png")
# Set the caption of the screen
pygame.display.set_caption('3D thing!')
  
screen.fill(background_colour)
def toProjected2D(coords, xAngle, yAngle, zAngle):
    xRotation = [[1, 0, 0],
                [0, np.cos(xAngle), -np.sin(xAngle)],
                [0, np.sin(xAngle), np.cos(xAngle)]]

    yRotation = [[np.cos(yAngle), 0, np.sin(yAngle)],
                [0, 1, 0],
                [-np.sin(yAngle), 0, np.cos(yAngle)]]

    zRotation = [[np.cos(zAngle), -np.sin(zAngle), 0],
                [np.sin(zAngle), np.cos(zAngle), 0],
                [0, 0, 1]]
    #All rotation object can make
    rotated = np.matmul(coords, xRotation)
    rotated = np.matmul(rotated, yRotation)
    rotated = np.matmul(rotated, zRotation)

    projected2D = np.matmul(rotated, orthProjection)
            
    return projected2D

def renderObject(model, xAngle, yAngle, zAngle, colour, thickness):      
    for x in range(len(model.faces)):        
            one = toProjected2D(model.vertices[(model.faces[x][0][0]) - 1], xAngle, yAngle, zAngle)
            two = toProjected2D(model.vertices[(model.faces[x][1][0]) - 1], xAngle, yAngle, zAngle)
            three = toProjected2D(model.vertices[(model.faces[x][2][0]) - 1], xAngle, yAngle, zAngle)
            pygame.gfxdraw.aapolygon(screen, [((one[0][0]) + (screenSize[0] / 2), (one[0][1]) + (screenSize[1] / 2)), ((two[0][0]) + (screenSize[0] / 2), (two[0][1]) + (screenSize[1] / 2)), ((three[0][0]) + (screenSize[0] / 2), (three[0][1]) + (screenSize[1] / 2))], colour)
    for y in range(len(model.normal)):
            pixel = toProjected2D(model.normal[y], xAngle, yAngle, zAngle)
            pygame.gfxdraw.pixel(screen, int(pixel[0][0]+ (screenSize[0] / 2)) , int(pixel[0][1] + (screenSize[1] / 2)), colours.green)
pygame.display.flip()

running = True
# game loop
while running:
    screen.fill(background_colour)
    yAngle += .05
    xAngle += .05

    for event in pygame.event.get():
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False
    renderObject(model5, xAngle, yAngle, zAngle, colours.grey, 0)
    
    pygame.display.update()