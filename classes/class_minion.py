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
    
    def __init__(self):
        pass



    # ------------------------------------------------------------------
    # The minion's heartbeat, evaluating its health and well being
    # ------------------------------------------------------------------
    def Pulse(self):
        pass