import pygame, sys
from pygame.locals import QUIT
import time
from time import sleep
import os 
import math
import random

pygame.init() #Initializes pygame.

#sprite variables
#cannons
doubleCannon = pygame.image.load('towers/doubleCannon.png')
singleCannon = pygame.image.load('towers/singleCannon.png')
#troops
armyMan = pygame.image.load('towers/armyMan.png')
bowman = pygame.image.load('towers/bowman.png')
robot = pygame.image.load('towers/robot.png')
#walls
wall = pygame.image.load('towers/wall.png')
strongWall = pygame.image.load('towers/strongWall.png')
#menu items
background = pygame.image.load('background.png')
sidebar = pygame.image.load('sidebar.png')
select = pygame.image.load('select.png')
play = pygame.image.load('play.png')

screen = pygame.display.set_mode((790, 640)) #This is a display object.



def initializeScreen() : #Sets up the screen.

  for a in range(0, 20) :
    for b in range(0, 20) :
      screen.blit(background,(a * 32,b * 32))
  grid = pygame.transform.scale(sidebar, (150,640))
  playButton = pygame.transform.scale(play,(150,100)) 
  screen.blit(grid,(640,0))
  screen.blit(playButton,(640,540))
  #units
  screen.blit(armyMan,(672,32))
  screen.blit(bowman,(736,32))
  screen.blit(robot,(672,96))
  #cannons
  screen.blit(singleCannon,(671,160))
  screen.blit(doubleCannon,(736,160))
  #wall
  screen.blit(wall,(672,224))
  screen.blit(strongWall,(736,224))


def remapGrid() : #Resets Menu Icons
  grid = pygame.transform.scale(sidebar, (150,640))
  playButton = pygame.transform.scale(play,(150,100)) 
  screen.blit(grid,(640,0))
  screen.blit(playButton,(640,540))
  #units
  screen.blit(armyMan,(672,32))
  screen.blit(bowman,(736,32))
  screen.blit(robot,(672,96))
  #cannons
  screen.blit(singleCannon,(671,160))
  screen.blit(doubleCannon,(736,160))
  #wall
  screen.blit(wall,(672,224))
  screen.blit(strongWall,(736,224))
  

initializeScreen()

pygame.display.set_caption('Winstons Penguin Troubles!') #This sets the title of the display.


#Global Game Variables
clock = pygame.time.Clock() #Regulates in-game time. Framerate, etc.

#Board Class - Creates a 20x20 Grid of Lines.
class Board(object):
  def __init__(self):
    for i in range(0, 640): #Creates a 20x20 grid. 
      if i % 32 == 0:
        pygame.draw.line(screen, (123, 152, 181), (i, 0), (i, 640)) 
        pygame.draw.line(screen, (123, 152, 181), (0, i), (640, i))

#Tower Class
class Tower: #General tower variables and methods.
  def __init__(self, x, y):
    self.hp = None
    self.damage = None
    self.x = x*32 #Pixel Position X
    self.y = y*32 #Pixel Position Y
    self.image = None
    self.attackLocations = [[None]]

  def attack(self): #Hit-Scan & Enemy Death
    for tile in self.attackLocations:
      for enemy in enemies:
        if(tile[0] == (enemy.x // 32) and tile[1] == (enemy.y // 32)):
          enemy.hp = enemy.hp - self.damage
          if(enemy.hp <= 0):
            screen.blit(background, (enemy.x, enemy.y))
            enemies.remove(enemy)

#Enemy Class
class Enemy: #General enemy variables and methods.
  def __init__(self, x, y):
    self.hp = None
    self.damage = None
    self.x = x*32 #Pixel Position X
    self.y = y*32 #Pixel Position Y
    self.xDistance = 10-(self.x//32)  #Grid Distance From Center X
    self.yDistance = 10-(self.y//32)  #Grid Distance From Center Y
    self.rightImage = None
    self.leftImage = None
    self.upImage = None
    self.downImage = None

  def moveLeft(self):
    screen.blit(background,(self.x,self.y))
    self.x = self.x - 32
    screen.blit(self.leftImage,(self.x,self.y))
    self.xDistance = 10-(self.x//32)  #Grid Distance From Center X
    self.yDistance = 10-(self.y//32)  #Grid Distance From Center Y
    
  def moveRight(self):
    screen.blit(background,(self.x,self.y))
    self.x = self.x + 32
    screen.blit(self.rightImage,(self.x,self.y))
    self.xDistance = 10-(self.x//32)  #Grid Distance From Center X
    self.yDistance = 10-(self.y//32)  #Grid Distance From Center Y
    
  def moveUp(self):
    screen.blit(background,(self.x,self.y))
    self.y = self.y - 32
    screen.blit(self.upImage,(self.x,self.y))
    self.xDistance = 10-(self.x//32)  #Grid Distance From Center X
    self.yDistance = 10-(self.y//32)  #Grid Distance From Center Y
    
  def moveDown(self):
    screen.blit(background,(self.x,self.y))
    self.y = self.y + 32
    screen.blit(self.downImage,(self.x,self.y))
    self.xDistance = 10-(self.x//32)  #Grid Distance From Center X
    self.yDistance = 10-(self.y//32)  #Grid Distance From Center Y

#Specific Towers
#Main Tower Class
class MainTower(Tower):
  def __init__(self, x, y): #Initializes to a grid position.
    super().__init__(x,y)
    self.hp = 5
    self.damage = 0
    self.x = self.x//32
    self.y = self.y//32
    self.attackLocations = [[0,0]]
    self.image = pygame.image.load('towers/penguins.png')
    screen.blit(self.image,(self.x, self.y))

#Wall Tower Class
class Wall(Tower):
  def __init__(self, x, y): #Initializes to a grid position.
    super().__init__(x,y)
    self.hp = 6
    self.damage = 0
    self.x = self.x//32
    self.y = self.y//32
    self.attackLocations = [[0,0]]
    self.image = pygame.image.load('towers/wall.png')
    self.x = self.x*32
    self.y = self.y*32
    screen.blit(self.image,(self.x, self.y))

#StrongWall Tower Class
class StrongWall(Tower):
  def __init__(self, x, y): #Initializes to a grid position.
    super().__init__(x,y)
    self.hp = 8
    self.damage = 0
    self.x = self.x//32
    self.y = self.y//32
    self.attackLocations = [[0,0]]
    self.image = pygame.image.load('towers/strongWall.png')
    self.x = self.x*32
    self.y = self.y*32
    screen.blit(self.image,(self.x, self.y))

#ArmyMan Tower Class
class ArmyMan(Tower):
  def __init__(self, x, y):
    super().__init__(x,y)
    self.hp = 5
    self.damage = 2
    self.x = self.x//32
    self.y = self.y//32
    self.image = pygame.image.load('towers/armyMan.png')
    self.attackLocations = [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1]]
    self.x = self.x*32
    self.y = self.y*32
    screen.blit(self.image,(self.x, self.y))

#BowMan Tower Class
class BowMan(Tower):
  def __init__(self, x, y):
    super().__init__(x,y)
    self.hp = 4
    self.damage = 1
    self.x = self.x//32
    self.y = self.y//32
    self.image = pygame.image.load('towers/bowman.png')
    self.attackLocations = [[self.x+1,self.y],[self.x-1,self.y],[self.x,self.y+1],[self.x,self.y-1],[self.x+2,self.y],[self.x-2,self.y],[self.x,self.y+2],[self.x,self.y-2]]
    self.x = self.x*32
    self.y = self.y*32
    screen.blit(self.image,(self.x, self.y))

#SingleCannon Tower Class
class SingleCannon(Tower):
  def __init__(self, x, y):
    super().__init__(x,y)
    self.hp = 5
    self.damage = 2
    self.x = self.x//32
    self.y = self.y//32
    self.image = pygame.image.load('towers/singleCannon.png')
    self.attackLocations = [[self.x+1,self.y+1],[self.x+1,self.y],[self.x+1,self.y-1],[self.x,self.y+1],[self.x,self.y],[self.x,self.y-1],[self.x-1,self.y+1],[self.x-1,self.y],[self.x-1,self.y-1],[self.x+2,self.y],[self.x+2,self.y+1],[self.x+2,self.y+2],[self.x+1,self.y+2],[self.x,self.y+2],[self.x-1,self.y+2],[self.x-2,self.y+2],[self.x-2,self.y+1],[self.x-2,self.y],[self.x-2,self.y-1],[self.x-2,self.y-2],[self.x-1,self.y-2],[self.x,self.y-2],[self.x+1,self.y-2],[self.x+2,self.y-2],[self.x+2,self.y-1]]
    self.x = self.x*32
    self.y = self.y*32
    screen.blit(self.image,(self.x, self.y))

#DoubleCannon Tower Class
class DoubleCannon(Tower):
  def __init__(self, x, y):
    super().__init__(x,y)
    self.hp = 7
    self.damage = 4
    self.x = self.x//32
    self.y = self.y//32
    self.image = pygame.image.load('towers/doubleCannon.png')
    self.attackLocations = [[self.x+1,self.y+1],[self.x+1,self.y],[self.x+1,self.y-1],[self.x,self.y+1],[self.x,self.y],[self.x,self.y-1],[self.x-1,self.y+1],[self.x-1,self.y],[self.x-1,self.y-1],[self.x+2,self.y],[self.x+2,self.y+1],[self.x+2,self.y+2],[self.x+1,self.y+2],[self.x,self.y+2],[self.x-1,self.y+2],[self.x-2,self.y+2],[self.x-2,self.y+1],[self.x-2,self.y],[self.x-2,self.y-1],[self.x-2,self.y-2],[self.x-1,self.y-2],[self.x,self.y-2],[self.x+1,self.y-2],[self.x+2,self.y-2],[self.x+2,self.y-1],[self.x+3,self.y+0],[self.x+3,self.y+1],[self.x+3,self.y+2],[self.x+3,self.y+3],[self.x+2,self.y+3],[self.x+1,self.y+3],[self.x,self.y+3],[self.x-1,self.y+3],[self.x-2,self.y+3],[self.x-3,self.y+3],[self.x-3,self.y-2],[self.x-3,self.y-1],[self.x-3,self.y],[self.x-3,self.y-1],[self.x-3,self.y-2],[self.x-3,self.y-3],[self.x-2,self.y-3],[self.x-1,self.y-3],[self.x,self.y-3],[self.x+1,self.y-3],[self.x+2,self.y-3],[self.x+3,self.y-3],[self.x+3,self.y-2],[self.x+3,self.y-1]]
    self.x = self.x*32
    self.y = self.y*32
    screen.blit(self.image,(self.x, self.y))

#Robot Tower Class
class Robot(Tower):
  def __init__(self, x, y):
    super().__init__(x,y)
    self.hp = 4
    self.damage = 1
    self.x = self.x//32
    self.y = self.y//32
    self.image = pygame.image.load('towers/robot.png')
    self.attackLocations = [[self.x+1,self.y+1],[self.x+1,self.y],[self.x+1,self.y-1],[self.x,self.y+1],[self.x,self.y],[self.x,self.y-1],[self.x-1,self.y+1],[self.x-1,self.y],[self.x-1,self.y-1]]
    self.x = self.x*32
    self.y = self.y*32
    screen.blit(self.image,(self.x, self.y))

#Specific Enemies
#Gobolin Class!!!!
class Goblin(Enemy): #Gobolin Class :} (In voice.) Creates Goblin Enemy
  def __init__(self, x, y):
    super().__init__(x, y)
    self.hp = 4
    self.damage = 2
    self.leftImage = pygame.image.load('enemies/goblinUp.png')
    self.rightImage = pygame.image.load('enemies/goblinRight.png')
    self.upImage = pygame.image.load('enemies/goblinUp.png')
    self.downImage = pygame.image.load('enemies/goblinDown.png')
    screen.blit(self.rightImage,(self.x,self.y))

#The Terminator
class KillerCyborg(Enemy):
  def __init__(self, x, y):
    super().__init__(x, y)
    self.hp = 6
    self.damage = 3
    self.leftImage = pygame.image.load('enemies/killerCyborgLeft.png')
    self.rightImage = pygame.image.load('enemies/killerCyborgRight.png')
    self.upImage = pygame.image.load('enemies/killerCyborgUp.png')
    self.downImage = pygame.image.load('enemies/killerCyborgDown.png')

#Function for enemy movement.
def moveEnemies():
  for enemy in enemies:
    canMove = True
    for tower in towers:
      if(abs((enemy.x)//32 - (tower.x)//32) == 0 and abs((enemy.y)//32 - (tower.y)//32) == 1 or abs((enemy.x)//32 - (tower.x)//32) == 1 and abs((enemy.y)//32 - (tower.y)//32) == 0):
        canMove = False
        tower.hp = tower.hp - enemy.damage
        if(tower.hp <= 0):
          screen.blit(background,(tower.x,tower.y))
          towers.remove(tower)
    if(canMove == True):
      if(abs(enemy.xDistance) > abs(enemy.yDistance)):
        if(enemy.xDistance > 0):
          enemy.moveRight()
        else:
          enemy.moveLeft()
      elif(enemy.yDistance > 0):
          enemy.moveDown()
      elif(enemy.yDistance < 0):
          enemy.moveUp()

#Attack functionality for towers.
def towerAttacks():
  for tower in towers:
    tower.attack()

mainTower = MainTower(10,10)
enemies = [Goblin(2,2),Goblin(3,3),Goblin(14,3),KillerCyborg(19,4)]
towers = [mainTower]


#UI Code
class UI:

  def __init__(self):
    self.unitSelect = None
    
  #Tower Selection
  def selectUnit(self, x, y): #Selects a unit type on click.
    #armyMan
    if (x//32 == 21 and y//32 == 1 and y//32 % 2 != 0):
      self.unitSelect = "armyMan"
      remapGrid()
      screen.blit(select, (x//32 * 32, y//32 * 32))
    #bowman
    elif (x//32 == 23 and y//32 == 1 and y//32 % 2 != 0):
      self.unitSelect = "bowman"
      remapGrid()
      screen.blit(select, (x//32 * 32, y//32 * 32))
    #robot
    elif (x//32 == 21 and y//32 == 3 and y//32 % 2 != 0):
      self.unitSelect = "Robot"
      remapGrid()
      screen.blit(select, (x//32 * 32, y//32 * 32))
    #singleCannon
    elif (x//32 == 21 and y//32 == 5 and y//32 % 2 != 0):
      self.unitSelect = "singleCannon"
      remapGrid()
      screen.blit(select, (x//32 * 32, y//32 * 32))
    #doubleCannoon
    elif (x//32 == 23 and y//32 == 5 and y//32 % 2 != 0):
      self.unitSelect = "doubleCannon"
      remapGrid()
      screen.blit(select, (x//32 * 32, y//32 * 32))
    #wall
    elif (x//32 == 21 and y//32 == 7 and y//32 % 2 != 0):
      self.unitSelect = "wall"
      remapGrid()
      screen.blit(select, (x//32 * 32, y//32 * 32))
    #strongWall
    elif (x//32 == 23 and y//32 == 7 and y//32 % 2 != 0):
      self.unitSelect = "strongWall"
      remapGrid()
      screen.blit(select, (x//32 * 32, y//32 * 32))

  #Tower Placement
  def unitPlace(self, x, y): #Adds a new tower to the list of towers on the board.
    
    print(self.unitSelect)
    
    if (self.unitSelect == "armyMan"): #Add armyMan
      towers.append(ArmyMan((x//32) * 32, (y//32) * 32))
      screen.blit(armyMan, ((x//32) * 32, (y//32) * 32))
      
    if (self.unitSelect == "bowman"): #Add bowMan
      towers.append(BowMan((x//32) * 32, (y//32) * 32))
      screen.blit(bowman, ((x//32) * 32, (y//32) * 32))
      
    if (self.unitSelect == "wall"): #Add wall
      towers.append(Wall((x//32) * 32, (y//32) * 32))
      screen.blit(wall, ((x//32) * 32, (y//32) * 32))
      
    if (self.unitSelect == "strongWall"): #Add strongWall
      towers.append(StrongWall((x//32) * 32, (y//32) * 32))
      screen.blit(strongWall, ((x//32) * 32, (y//32) * 32))
      
    if (self.unitSelect == "Robot"):
      towers.append(Robot((x//32) * 32, (y//32) * 32))
      screen.blit(robot, ((x//32) * 32, (y//32) * 32))
      
    if (self.unitSelect == "singleCannon"): #Add singleCannon
      towers.append(SingleCannon((x//32) * 32, (y//32) * 32))
      screen.blit(singleCannon, ((x//32) * 32, (y//32) * 32))
      
    if (self.unitSelect == "doubleCannon"): #Add doubleCannon
      towers.append(DoubleCannon((x//32) * 32, (y//32) * 32))
      screen.blit(doubleCannon, ((x//32) * 32, (y//32) * 32))
      
  #Event Checker
  def eventCheck(self): #Watches for user interaction.
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN: #Checks for mouse events.
        pos = pygame.mouse.get_pos()
        print(pos[0], pos[1])
        if (pos[0] > 640 and pos[1] > 540) :
          print("Button pressed")
          while (towers.count(mainTower) == 1 and len(enemies) != 0): #Checks to see if play button pressed.
            #seconds = 1
            #end_time = time.time() + seconds
            #while time.time() < end_time:
              moveEnemies()
              towerAttacks()
        elif (pos[0] > 640):
          self.selectUnit(pos[0], pos[1]) #Menu Actions
        elif (pos[0] < 640):
          self.unitPlace(pos[0], pos[1]) #Unit Placement

class WaveRunner:
  def __init__(self):
    pass
  
  def newWave(self):
    for enemy in enemies:
      pass
      
  
userInterface = UI()

#Game RUN!!!!
while True:
  
  userInterface.eventCheck()
  
  board = Board()
  pygame.display.update()

  clock.tick(1) #Display updates at 1 fps.

