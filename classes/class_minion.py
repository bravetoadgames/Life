# -*- coding: utf-8 -*-
from classes.class_minion_appetite import Appetite
from classes.class_minion_brain import Brain
from classes.class_minion_eyes import Eyes
from classes.class_minion_health import Health
from classes.class_minion_hearing import Hearing
from classes.class_minion_sex import Sex

class Minion:

    sex = Sex()
    brain = Brain()
    health = Health()
    appetite = Appetite()
    eyes = Eyes()
    hearing = Hearing()
    
    thirst = 0
    
    def __init__(self):
        pass


    def lifePulse(self):
        # Do all health related stuff
        if not self.health.getDead():
            self.health.setAging()
        

        