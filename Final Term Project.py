# Sachi Nagada
# Term Project

from pykinect2 import PyKinectV2, PyKinectRuntime
from pykinect2.PyKinectV2 import *
import pygame
import sys
import math
import random


red = (255, 102, 102)
blue = (178, 102 , 255)
orange = (255, 165, 0)
green = (76, 153, 0)
peach = (255, 204, 152)

class Start(pygame.sprite.Sprite):
    def __init__(self,location):
        super(Start,self).__init__()
        # play button image from 
        #http://www.freevideogamesonline.org/core-images/play-game-dark-blue.png
        self.image = pygame.image.load("playbutton.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = location

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        self.r = random.randint(20,40)
        self.color = random.choice([red, blue, orange, green])
        self.cx = random.randint(40, 900)
        self.cy = random.randint(400, 600)
        self.drop = 4
        self.xdrop = random.choice([-2,2])
        self.touchXWalls = False
        self.touchYWalls = False
        self.rect = pygame.Rect(self.cx - self.r, self.cy - self.r,
                                2*self.r, 2*self.r)
        self.image = pygame.Surface((2 * self.r, 2 * self.r),
                                    pygame.SRCALPHA)  # make it transparent
        self.image = self.image.convert_alpha()

    def update(self,score):
        if self.cx < 10 or self.cx > 980:
            self.touchXWalls = True
        elif self.cy < 10:
            self.touchYWalls = True
         # make fruit change direction once it hits a wall
        if self.touchXWalls == False:
            self.cx += self.xdrop
        else:
            self.cx -= self.xdrop
      
        if self.touchYWalls == False:
            self.cy -= self.drop
        else:
            self.cy += self.drop
        if score > 10:
            self.drop = (score//10)*4

        # updates the position and draws the object
        self.rect = pygame.Rect(self.cx-self.r, self.cy - self.r,
                                2*self.r, 2*self.r)
        pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r)



class CutFruit(pygame.sprite.Sprite):
    def __init__(self,r, x, y, color):
        super(CutFruit, self).__init__()
        self.r = r
        self.x = x
        self.y = y
        self.color = color
        self.drop = 2
        self.rect = pygame.Rect(self.x-self.r, self.y - self.r,
                                2*self.r, 2*self.r)
        self.image = pygame.Surface((2 * self.r, 2 * self.r),
                                    pygame.SRCALPHA)  # make it transparent
        self.image = self.image.convert_alpha()

    def update(self):
        self.y += self.drop
        self.rect = pygame.Rect(self.x-self.r, self.y - self.r,
                                2*self.r, 2*self.r)
        pygame.draw.polygon(self.image, self.color, [(0,self.r),
            (self.r/4, self.r/2),( self.r-3, 0),(self.r-3, 2*self.r),
            (self.r/4, 3*self.r/2)])
        pygame.draw.polygon(self.image, self.color, [(self.r+3,0),
            (3*self.r/2, self.r/4),(2*self.r, self.r),(7*self.r/4, 3*self.r/2),
            (self.r+3, 2*self.r)]) 

class LeftHand(pygame.sprite.Sprite):
    def __init__(self, fruit, leftX, leftY):
        super(LeftHand,self).__init__()
        self.fruit = fruit
        self.kinect = PyKinectRuntime.PyKinectRuntime(
            PyKinectV2.FrameSourceTypes_Color|PyKinectV2.FrameSourceTypes_Body)       
        self.bodies = None  
        self.leftX = leftX
        self.leftY = leftY
        self.leftCurrX = 0
        self.leftCurrY = 0
        self.elbowX = 0
        self.color = peach
        self.r = 20
        self.image = pygame.image.load('lefthand.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.leftX, self.leftY)

    def update(self):
        # determines the position of the hand in kinect
        if self.kinect.has_new_body_frame():
            self.bodies = self.kinect.get_last_body_frame()
            if self.bodies is not None:
                for i in range (0, self.kinect.max_body_count):
                    body = self.bodies.bodies[i]
                    if not body.is_tracked:
                        continue 
                    joints = body.joints 

                    #tracking states: tracked, inferred, and not tracked  
                    if (joints[PyKinectRuntime.JointType_ElbowLeft]
                        .TrackingState != PyKinectV2.TrackingState_NotTracked):
                        self.elbowX = (joints[PyKinectV2.JointType_ElbowLeft].
                            Position.x)
                    if (joints[PyKinectV2.JointType_HandLeft].
                        TrackingState != PyKinectV2.TrackingState_NotTracked):
                        self.leftCurrX = (joints[PyKinectV2.JointType_HandLeft]
                            .Position.x)
                        self.leftCurrY = (joints[PyKinectV2.JointType_HandLeft]
                            .Position.y)
                        self.leftX = (450/0.5)*self.leftCurrX + 225
                        self.leftY = (-600/0.45)*self.leftCurrY + 300

        # update the position of the hand
        self.image = pygame.image.load('lefthand.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.leftX, self.leftY)

class RightHand(pygame.sprite.Sprite):
    def __init__(self, fruit, rightX, rightY):
        super(RightHand,self).__init__()
        self.fruit = fruit
        self.kinect = (PyKinectRuntime.PyKinectRuntime(PyKinectV2
            .FrameSourceTypes_Color|PyKinectV2.FrameSourceTypes_Body))       
        self.bodies = None  
        self.rightX = rightX
        self.rightY = rightY
        self.rightCurrX = 0
        self.rightCurrY = 0
        self.elbowX = 0
        self.color = peach 
        self.r = 20
        self.image = pygame.image.load('righthand.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.rightX, self.rightY)

    def update(self):
        if self.kinect.has_new_body_frame():
            self.bodies = self.kinect.get_last_body_frame()
            if self.bodies is not None:
                for i in range (0, self.kinect.max_body_count):
                    body = self.bodies.bodies[i]
                    if not body.is_tracked:
                        continue 
                        #tracking states: tracked, inferred, and not tracked
                    joints = body.joints   
                    if (joints[PyKinectV2.JointType_HandRight].TrackingState 
                        != PyKinectV2.TrackingState_NotTracked):
                        # updates the hand position in the Right/Left hand Class
                        self.rightCurrX = (joints[PyKinectV2.
                              JointType_HandRight].Position.x)
                        self.rightCurrY = (joints[PyKinectV2.
                              JointType_HandRight].Position.y)
                        self.rightX = (900)*self.rightCurrX + 450
                        self.rightY = (-600/0.45)*self.rightCurrY + 300
                    if (joints[PyKinectRuntime.JointType_ElbowRight]
                        .TrackingState != PyKinectV2.TrackingState_NotTracked):
                        self.elbowX = (joints[PyKinectV2.JointType_ElbowRight]
                            .Position.x)

        # updates the position of the right hand
        self.image = pygame.image.load('righthand.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.rightX, self.rightY)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.r = 30
        self.color = (0,0,0)#(255, 255, 255)
        self.cx = random.randint(100, 700)
        self.cy = 400

        # image from 
        #http://www.abeka.com/BookImages/ClipArt/237744/46x46y50fx50fh/237744
        #-Soccer-Ball-black-and-white-line-png.png
        self.image = pygame.image.load('soccerball.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.cx, self.cy)
        self.dropX = 0
        self.dropY = 0
        self.a = self.r
    def update(self):
         self.cx += self.dropX
         self.cy += self.dropY 
         self.image = pygame.image.load('soccerball.png').convert_alpha()
         self.rect = self.image.get_rect()
         self.rect.center = (self.cx, self.cy)


class Goal(pygame.sprite.Sprite):
    # image from 
    #http://cdn4.kozzi.com/b1/11/248/photo-24727257-illustration-of-
    #soccer-goal.jpg
    def __init__(self, ball):
        super(Goal, self).__init__()
        self.ball = ball
        self.cx = random.randint(20,700)
        self.cy = 20
        self.image = pygame.image.load("goal.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.cx, self.cy)

    def update(self):
        self.image = pygame.image.load("goal.png").convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.cx, self.cy)

class LeftFoot(pygame.sprite.Sprite):
    def __init__(self, ball, leftX, leftY):
        super(LeftFoot, self).__init__()
        self.currX = leftX
        self.currY = leftY
        self.kinect = (PyKinectRuntime.PyKinectRuntime(PyKinectV2.
            FrameSourceTypes_Color|PyKinectV2.FrameSourceTypes_Body))       
        self.bodies = None  
        self.prevX = 0
        self.prevY = 0
        self.color = peach 
        self.r = 20
        self.rect = pygame.Rect(self.currX-self.r, self.currY - self.r,
                              2*self.r, 2*self.r)
        self.image = pygame.Surface((2 * self.r, 2 * self.r),
                                    pygame.SRCALPHA) 
        self.image = self.image.convert_alpha()

    def update(self):
        if self.kinect.has_new_body_frame():
            self.bodies = self.kinect.get_last_body_frame()
            if self.bodies is not None:
                for i in range (0, self.kinect.max_body_count):
                    body = self.bodies.bodies[i]
                    if not body.is_tracked:
                        continue 
                        #tracking states: tracked, inferred, and not tracked
                    joints = body.joints   
                    if (joints[PyKinectV2.JointType_FootLeft].TrackingState 
                        != PyKinectV2.TrackingState_NotTracked):
                        self.currX = (450/0.5)*(joints[PyKinectV2.
                             JointType_FootLeft].Position.x) + 225
                        self.currY = (-200/0.3)*(joints[PyKinectV2.
                              JointType_FootLeft].Position.y) + 25

        # updates the position and displays the object
        self.prevX = self.currX
        self.prevY = self.currY
        self.rect = pygame.Rect(self.currX-self.r, self.currY - self.r,
                              2*self.r, 2*self.r)
        pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r)

class RightFoot(pygame.sprite.Sprite):
    def __init__(self, ball, rightX, rightY):
        super(RightFoot,self).__init__()
        self.ball = ball
        self.currX = rightX
        self.currY = rightY
        self.kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.
            FrameSourceTypes_Color|PyKinectV2.FrameSourceTypes_Body)       
        self.bodies = None  
        self.prevX = 0
        self.prevY = 0
        self.color = peach 
        self.r = 20
        self.rect = pygame.Rect(self.currX-self.r, self.currY - self.r,
                              2*self.r, 2*self.r)
        self.image = pygame.Surface((2 * self.r, 2 * self.r),
                                    pygame.SRCALPHA) 
        self.image = self.image.convert_alpha()

    def update(self):
        if self.kinect.has_new_body_frame():
            self.bodies = self.kinect.get_last_body_frame()
            if self.bodies is not None:
                for i in range (0, self.kinect.max_body_count):
                    body = self.bodies.bodies[i]
                    if not body.is_tracked:
                        continue 
                        #tracking states: tracked, inferred, and not tracked
                    joints = body.joints   
                    if ((joints[PyKinectV2.JointType_FootRight].TrackingState 
                        != PyKinectV2.TrackingState_NotTracked)):
                        # updates the hand position in the Right/Left feet Class
                        self.currX = (900)*(joints[PyKinectV2
                            .JointType_FootRight].Position.x) + 450
                        self.currY = (-200/0.3)*(joints[PyKinectV2.
                            JointType_FootRight].Position.y) + 25
                               
        # updates the position of the foot and displays the object
        self.prevX = self.currX
        self.prevY = self.currY
        self.rect = pygame.Rect(self.currX-self.r, self.currY - self.r,
                              2*self.r, 2*self.r)
        pygame.draw.circle(self.image, self.color, (self.r, self.r), self.r)

class BoxingGlove(pygame.sprite.Sprite):
    def __init__(self):
        super(BoxingGlove, self).__init__()

        self.cx = random.randint(150,650)
        self.cy = random.randint(100,300)
        self.move = random.choice([-7,7])
        self.color = (255,0,0)
        self.r = 30
        # image from 
        #http://png-4.vector.me/files/images/4/4/449313/boxing_glove
        #_vector_image_thumb.gif
        self.image = pygame.image.load('glove.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (self.cx, self.cy)
    
    def update(self):
        self.cx += self.move
        self.rect = self.image.get_rect()
        self.rect.center = (self.cx, self.cy)
        self.image = pygame.image.load('glove.png').convert_alpha()

class Head(pygame.sprite.Sprite):
    def __init__(self, glove):
        super(Head,self).__init__()
        self.glove = glove
        self.kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.
            FrameSourceTypes_Color|PyKinectV2.FrameSourceTypes_Body)       
        self.bodies = None
        self.cx = 0
        self.cy = 0
        # image from 
        #http://www.clker.com/cliparts/8/7/Z/L/N/M/white-stick-figure-md.png
        self.image = pygame.image.load('stickfigure.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midtop = (self.cx, self.cy)

    def update(self):
         if self.kinect.has_new_body_frame():
            self.bodies = self.kinect.get_last_body_frame()
            if self.bodies is not None:
                for i in range (0, self.kinect.max_body_count):
                    body = self.bodies.bodies[i]
                    if not body.is_tracked:
                        continue 
                        #tracking states: tracked, inferred, and not tracked
                    joints = body.joints   
                    if (joints[PyKinectV2.JointType_Head].TrackingState 
                        != PyKinectV2.TrackingState_NotTracked):
                        # updates the hand position in the Head Class
                        self.cx = ((900/1.21)*(joints[PyKinectV2
                            .JointType_Head].Position.x) + 268)
                        self.cy = ((-300/0.56)*(joints[PyKinectV2
                            .JointType_Head].Position.y) + 654)

        # updates the position and displays the object
         self.image = pygame.image.load('stickfigure.png').convert_alpha()
         self.rect = self.image.get_rect()
         self.rect.center = (self.cx, self.cy)
       
# the general outline from Lukas' blog:
# https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py
class PygameGame(object):
    def init(self):
        pygame.init()     
        self.screen = (pygame.display.set_mode((960, 540), pygame.HWSURFACE
            |pygame.DOUBLEBUF, 32))
        self.counter = 0
        self.GameOver = False
        self.score=0
        self.tempScore = 0
        self.misses = 0 
      
        self.startScreen = True # start with True
        
        self.fruitNinjadir = True # start with True
        self.FruitNinjaOver = True
        self.FruitNinjaExercise = False
        self.FruitExerciseMessage = False
        
        self.soccerOver = True
        self.soccerMessage = True # start with True
       
        self.boxingOver = True
        self.boxingMessage = True # start with True
       
        self.start = Start([350,250])
        self.starts = pygame.sprite.Group(self.start)

        self.fruit = pygame.sprite.Group()
        self.cutFruit = pygame.sprite.Group() 

        self.lefthand = LeftHand(self.fruit, 0, 0)
        self.lefts = pygame.sprite.Group(self.lefthand)

        self.righthand = RightHand(self.fruit, 0, 0)
        self.rights = pygame.sprite.Group(self.righthand)

        self.ball = Ball()
        self.balls = pygame.sprite.Group()

        self.goal = Goal(self.ball)
        self.goals = pygame.sprite.Group(self.goal)

        self.rightFoot = RightFoot(self.ball, 0, 0)
        self.rightFeet = pygame.sprite.Group(self.rightFoot)

        self.leftFoot = LeftFoot(self.ball, 0, 0)
        self.leftFeet = pygame.sprite.Group(self.leftFoot)

        self.glove = BoxingGlove()
        self.gloves = pygame.sprite.Group(self.glove)

        self.head = Head(self.glove)
        self.heads = pygame.sprite.Group(self.head)

    def timerFired(self, dt):
        if self.GameOver == False:
            
            # if hand collides with play button, delete the play button 
            #and start game
            if self.startScreen == True:
                if (pygame.sprite.groupcollide(self.rights, self.starts, 
                    False, True, pygame.sprite.collide_rect) or 
                    pygame.sprite.groupcollide(self.lefts, self.starts,
                            False, True, pygame.sprite.collide_rect)):
                    self.FruitNinjaOver = False
                    self.startScreen = False
                self.rights.update()
                self.lefts.update()
                        
            if self.FruitNinjaOver == False:
                self.counter += 0.1
                #display the instructions for 10 seconds
                if self.counter > 10:
                    self.fruitNinjadir = False

                    # adds fruit when less than one on the screen
                if len(self.fruit) < 1 and self.fruitNinjadir == False:
                    self.f = Fruit()
                    self.fruit.add(self.f)
                
                    # if score of 25 is achieved, move to soccer
                if self.score > 25: 
                    self.boxingOver = False
                    self.counter = 0 # resets the counter
                    self.misses = 0 # resets the misses
                    self.FruitNinjaOver = True

                    # if the number of misses is more than 5, exercise is needed
                if self.misses > 5:
                    self.FruitNinjaExercise = True  
                    self.counter = 0 
                    self.FruitNinjaOver = True 

                    # checks for collision between the hand and the fruit 
                    #and gets rid of the fruit
                    # and adds a cutFruit that falls down
                if (pygame.sprite.groupcollide(self.rights, self.fruit, False, 
                    False, pygame.sprite.collide_rect) or 
                    pygame.sprite.groupcollide(self.lefts, self.fruit,
                        False, False, pygame.sprite.collide_rect)):
                    self.score +=1
                    for fruit in self.fruit:
                        self.cutFruit.add(CutFruit(fruit.r,fruit.cx,
                            fruit.cy,fruit.color))
                        self.fruit.remove(fruit)

                #gets rid of the fruit if at the bottom of the screen 
                #and increases the number of misses
                for fruit in self.fruit:
                    if fruit.cy > 500 and (fruit.touchXWalls==True or 
                        fruit.touchYWalls == True):
                        self.fruit.remove(fruit)
                        self.misses +=1
  
                self.fruit.update(self.score)
                self.rights.update()
                self.lefts.update()
                self.cutFruit.update()

            if self.FruitNinjaExercise == True:
                # this number because it's the closest to counting down seconds
                self.counter += 0.01 

                self.rights.update()
                self.lefts.update()

                # elbow and hand of opposite hands should be on top of each other 
                # leaving a 10 cm margin for kinect buffer
                for right in self.rights:
                    for left in self.lefts:
                        if ((abs(right.rightCurrX - right.elbowX) > 0.1 
                            and abs(left.leftCurrX - left.elbowX) < 0.1) or 
                        (abs(right.rightCurrX - left.elbowX) < 0.1 
                            and abs(left.leftCurrX - left.elbowX) > 0.1)):
                            self.FruitExerciseMessage = False

                        else:
                            self.FruitExerciseMessage = True
               
                # enough stretching, time to move to next game
                if self.counter > 15: 
                    self.boxingOver = False
                    self.misses = 0
                    self.FruitExerciseMessage = False
                    self.counter = 0
                    self.FruitNinjaExercise = False


            #soccer game is ons
            if self.soccerOver == False:
                self.counter +=0.1
            
               # explains the rules in the first ten seconds
                if self.counter > 3:
                    self.soccerMessage = False
            
                # always have at least one ball on screen
                if len(self.balls) < 1 and self.soccerMessage == False:
                    newBall = Ball()
                    self.balls.add(newBall)

                # always have at least one goal on screen
                if len(self.goals)<1 and self.soccerMessage == False:
                    for ball in self.balls:
                        newGoal = Goal(ball)
                        self.goals.add(newGoal)

                    # if ball is at the 100 pixel mark, it hasn't hit the goal
                    # and will be removed from the sprite
                for ball in self.balls:
                    if (ball.cy < 100 or ball.cy> 600 or
                     ball.cx < 0 or ball.cx > 800):
                        self.balls.remove(ball)
                        self.misses +=1

            #if the ball goes in the goal, score increases and new challenge
                if (pygame.sprite.groupcollide(self.balls, self.goals, 
                    True, True, pygame.sprite.collide_rect)):
                    self.score+=1
                    self.tempScore +=1

                if pygame.sprite.groupcollide(self.rightFeet, self.balls, 
                    False, False, pygame.sprite.collide_rect):
                    for ball in self.balls:
                        for goal in self.goals:
                            for foot in self.rightFeet:
                                ball.dropX = (goal.cx + random.randint(0,250)
                                    - ball.cx)/ (0.05*abs(foot.currY
                                     - foot.prevX))
                                ball.dropY = (goal.cy + random.randint(0,135)
                                    - ball.cy)/ (0.05*abs(foot.currY 
                                        - foot.prevX))


                # need to look at both feet because player can kick the ball
                # with both feet
                if pygame.sprite.groupcollide(self.leftFeet, self.balls, 
                    False, False, pygame.sprite.collide_rect):
                    for ball in self.balls:
                        for goal in self.goals:
                            for foot in self.leftFeet:
                                ball.dropX = (goal.cx + random.randint(0,250)- 
                                    ball.cx)/ (0.05*abs(foot.currY 
                                    - foot.prevX))
                                ball.dropY = (goal.cy + random.randint(0,135)- 
                                    ball.cy)/ (0.05*abs(foot.currY 
                                        - foot.prevX))

                if self.tempScore> 5:
                    self.GameOver = True

                self.goals.update()
                self.balls.update()
                self.rightFeet.update()
                self.leftFeet.update()

                # have done well in this game and time to move on to a 
                # different game
            if self.boxingOver == False:
                self.counter +=0.1
               
            # displays the instructions for this game for the first 10 seconds
                if self.counter > 10:
                    self.boxingMessage = False
                   
                    # one glove on screen at all times
                if len(self.gloves)<1 and self.boxingMessage == False:
                    newGlove = BoxingGlove()
                    self.gloves.add(newGlove)
                   
                    # make the gloves dissappear when they are at the edges
                for glove in self.gloves:
                    if glove.cx < 100 or glove.cx > 900:
                        self.score += 1
                        self.tempScore +=1
                        self.gloves.remove(glove)
                   
                        # switch from boxing to soccer
                if self.tempScore > 20 or self.misses > 5:
                    self.soccerOver = False
                    self.tempScore = 0
                    self.misses = 0
                    self.counter = 0
                    self.boxingOver = True

                if pygame.sprite.groupcollide(self.heads, self.gloves,
                            False, True, pygame.sprite.collide_rect):
                    self.misses +=1

                self.gloves.update()
                self.heads.update()
                  
    def redrawAll(self, screen):

        if self.GameOver == False:
            if self.startScreen == True:
                
                # rectangle to give a background color
                rectangle = pygame.draw.rect(screen, (204, 255, 153),
                    (0,0,1000,1000))
               
                # idea for displaying this sprite from 
                #http://floppsie.comp.glam.ac.uk/Glamorgan/gaius/games/8.html
                for start in self.starts:
                    screen.blit(start.image, start.rect)
                
                #text on the screen
                myfont = pygame.font.SysFont("comicsansms",20)
                label1 = (myfont.render(
                    "Please stand 1-2 meters away from the kinect", 1,blue))
                label3 = myfont.render(
                    "Please move your hand over 'Play'", 1, blue)
                label4 = myfont.render("to begin Fruit Ninja", 1, blue)                
                screen.blit(label1,(280,20))
                screen.blit(label3,(340, 140))
                screen.blit(label4,(400, 180))
                self.lefts.draw(screen)
                self.rights.draw(screen)

            if self.FruitNinjaOver == False:
               
                #background image from 
                #http://img3.wikia.nocookie.net/__cb39/fruitninja/images/5/
                #50/Wiki-background
                background = pygame.image.load("FruitNinjaBackground.png")
                screen.blit(background, (0,0))
                if self.fruitNinjadir == True:
                    myfont = pygame.font.SysFont("comicsansms", 40)
                    label1 = myfont.render("Move your hands to slice the fruit",
                     1, (245, 221, 186))
                    screen.blit(label1,(150,200))
                else:
                    self.fruit.draw(screen)
                    self.cutFruit.draw(screen)
                    self.lefts.draw(screen)
                    self.rights.draw(screen)
                
                #all the text on the screen:
                myfont = pygame.font.SysFont("comicsansms",20)
                label = myfont.render("Score: " + str(self.score), 1,
                    (245, 221, 186))
                screen.blit(label,(450,20))

            if self.FruitNinjaExercise == True:
                
                #background image from 
                #http://blog.hottubthings.com/wp-content/uploads/2014/06/
                #6277148.jpg
                background = pygame.image.load("FruitNinjaExercise.png")
                screen.blit(background,(400,40))
                
                # text
                myfont = pygame.font.SysFont("arial", 30)
                label1 = myfont.render("Please do this stretch", 1, blue)
                label2 = myfont.render("for 15 seconds with each arm", 1, blue)
                screen.blit(label1, (350,325))
                screen.blit(label2, (275,375))
                if self.FruitExerciseMessage == True:
                    myfont = pygame.font.SysFont("arial", 40)
                    label3 = myfont.render("Please continue stretching", 1, red)
                    screen.blit(label3, (250, 450))
            
            if self.soccerOver == False:
               
                # background image from http://www.imgmob.net/soccer-field.html
                background = pygame.image.load("soccerfield.png")
                screen.blit(background,(0,0))
                if self.soccerMessage:
                    myfont = pygame.font.SysFont("comicsansms",40)
                    label = myfont.render(
                        "Kick the soccer ball and aim for the goal", 1,
                        (0,0,153)) 
                    screen.blit(label,(100,200))
                else:
                    for goal in self.goals:
                        screen.blit(goal.image, goal.rect)
                    self.goals.draw(screen)
                    self.balls.draw(screen)
                    self.rightFeet.draw(screen)
                    self.leftFeet.draw(screen)
                myfont = pygame.font.SysFont("comicsansms",20)
                label = myfont.render("Score: " + str(self.score), 1,(0,0,153))
                screen.blit(label,(5,5))

            if self.boxingOver == False:
               
                # background image from 
                #http://www.localwom.com/i/boxing-ring-widescreen-wallpapers.jpg
                background = pygame.image.load("boxingring.png")
                screen.blit(background,(0,0))
                myfont = pygame.font.SysFont("comicsansms",20)
                label = myfont.render("Score: " + str(self.score), 1,
                    (255,255,255))
                screen.blit(label,(5,5))
                if self.boxingMessage:
                    myfont = pygame.font.SysFont("comicsansms",30)
                    label = myfont.render(
                        "Duck and move to avoid the boxing gloves", 1,
                        (255,255,255)) 
                    screen.blit(label,(200,200))
                else:
                    self.gloves.draw(screen)
                    self.heads.draw(screen)

        else:
            #shows a black background with "Game Over" and the score
            pygame.draw.rect(screen, (0,0,0),(0, 0, 1000, 800))
            myfont = pygame.font.SysFont("comicsansms",20)
            label = myfont.render("Score: " + str(self.score), 1,red)
            screen.blit(label,(20,20))
            myfont1 = pygame.font.SysFont("comicsansms", 50)
            label1 = myfont1.render("Game Over", 1, red)
            label2 = myfont1.render("Nice Job!", 1, red)
            screen.blit(label1, (350, 250))
            screen.blit(label2, (370, 150))


    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=800, height=800, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        while True:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.GameOver = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()
       
        self.kinect.close()
        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()