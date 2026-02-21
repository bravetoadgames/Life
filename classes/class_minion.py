# -*- coding: utf-8 -*-
from classes.class_minion_appetite import Appetite
from classes.class_minion_brain import Brain
from classes.class_minion_eyes import Eyes
from classes.class_minion_health import Health
from classes.class_minion_hearing import Hearing
from classes.class_minion_sex import Sex

class Minion:

    brain = Brain()
    health = Health()
    appetite = Appetite()
    eyes = Eyes()
    hearing = Hearing()
    sex = Sex()
    
    thirst = 0
    
    life_tick = 0.01
    age = 0
    
    def __init__(self):
        pass



    # ------------------------------------------------------------------
    # Get minion's age
    # ------------------------------------------------------------------
    def getAge(self):
        return str(int(self.age))


    
    # ------------------------------------------------------------------
    # Let the minion grow old
    # ------------------------------------------------------------------
    def setAging(self):
        self.age = self.age +self.life_tick
        