# -*- coding: utf-8 -*-
import random

class Eyes:
    colors = [
        "green",
        "brown",
        "dark blue",
        "light blue",
        ]
    def __init__(self, emitter):
        
        self.emitter = emitter

        self.color = ""
        self.cross_eyed = False
        self.sight_eye_left = 0.0
        self.sight_eye_right = 0.0
        
        self.setColor()
        self.setCrossEyed()
        self.setEyeSight()
            


    # ------------------------------------------------------------------
    # Get the eye color
    # ------------------------------------------------------------------
    def getColor(self):
        return self.color



    # ------------------------------------------------------------------
    # Get cross-eyedness of minion
    # ------------------------------------------------------------------
    def getCrossEyed(self):
        if self.cross_eyed == True:
            return "Minion has cross-eyed vision"
        return ""



    # ------------------------------------------------------------------
    # Get eyesight text
    # ------------------------------------------------------------------
    def getEyeSight(self):
        
        if self.getSightEyeLeft() == self.getSightEyeRight():
            if self.getSightEyeLeft() == 0:
                return "Blind"
            else:
                return str(self.getSightEyeLeft()) + "%"
        
        return "Left eye: " + str(self.getSightEyeLeft()) + "% - Right eye: " + str(self.getSightEyeRight()) + "%"



    # ------------------------------------------------------------------
    # Get left eye's sight
    # ------------------------------------------------------------------
    def getSightEyeLeft(self):
        return self.sight_eye_left



    # ------------------------------------------------------------------
    # Get right eye's sight
    # ------------------------------------------------------------------
    def getSightEyeRight(self):
        return self.sight_eye_right



    # ------------------------------------------------------------------
    # Set the eye color
    # ------------------------------------------------------------------
    def setColor(self):
        a = random.randint(0,len(self.colors)-1)
        self.color = self.colors[a]


    
    # ------------------------------------------------------------------
    # Determine if minion is cross eyed
    # ------------------------------------------------------------------
    def setCrossEyed(self):

        self.cross_eyed = False
        
        if random.randint(0,100) < 10:
            self.cross_eyed = True
                
            
            
    # ------------------------------------------------------------------
    # Set the eyesight of the minion
    # ------------------------------------------------------------------
    def setEyeSight(self):
        self.sight_eye_left = 100                   # default 100% vision
        self.sight_eye_right = 100

        a = random.randint(0,100)

        if a < 8:                                   # minion has eye issues
            b = random.randint(30,95)
            
            self.sight_eye_left = b
            self.sight_eye_right = b

            if b < 40:                              # eyes differ in sight quality
                while self.sight_eye_left == self.sight_eye_right:
                    c = random.randint(30,95)
                    self.sight_eye_left = c
        
            
