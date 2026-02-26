# -*- coding: utf-8 -*-
import random

class Eyes:
    colors = [
        "green",
        "brown",
        "dark blue",
        "light blue",
        ]
    def __init__(self):
        
        self.color = ""
        self.sight_eye_left = 0.0
        self.sight_eye_right = 0.0

        self.setColor()
        self.setEyeSight()
        


    # ------------------------------------------------------------------
    # Get the eye color
    # ------------------------------------------------------------------
    def getColor(self):
        return self.color



    # ------------------------------------------------------------------
    # Get eyesight
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


    def setEyeSight(self):
        self.sight_eye_left = 100
        self.sight_eye_right = 100

        a = random.randint(0,100)

        if a < 10:                      # minion has eye issues
            b = random.randint(30,95)
            
            self.sight_eye_left = b
            self.sight_eye_right = b

            if b < 35:                  # eyes differ in sight
                while self.sight_eye_left == self.sight_eye_right:
                    c = random.randint(30,95)
                    self.sight_eye_left = c
        
                    