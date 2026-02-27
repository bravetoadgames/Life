# -*- coding: utf-8 -*-
from classes.class_minion_brain import Brain
from classes.class_minion_digestion import Digestion
from classes.class_minion_eyes import Eyes
from classes.class_minion_health import Health
from classes.class_minion_hearing import Hearing
from classes.class_minion_sex import Sex

class Minion:

    
    def __init__(self):
        self.sex = Sex()
        self.brain = Brain()
        self.health = Health()
        self.digestion = Digestion()
        self.eyes = Eyes()
        self.hearing = Hearing()
        
        self.thirst = 0

        self.summarize()



    # ------------------------------------------------------------------
    # The heartbeat of a minion
    # ------------------------------------------------------------------
    def lifePulse(self):
        # Do all health related stuff
        if not self.health.isDead():
            self.health.setDead(self.health.growOlder())
        

    # ------------------------------------------------------------------
    # Summary of basic minion information
    # ------------------------------------------------------------------
    def summarize(self):
        print("Name: " + self.sex.getFullName())
        print("Gender: " + self.sex.getGender())
        print("Age expectancy: " + str(self.health.getAgeExpectancy()))
        print("Eye color: " + self.eyes.getColor())
        print("Eyesight: " + self.eyes.getEyeSight())

        if self.eyes.getCrossEyed() != "":
            print(self.eyes.getCrossEyed())

        print("Serotonin level: " + str(self.brain.getSerotonin()))
        print("Dopamine level: " + str(self.brain.getDopamine()))
        print()
        