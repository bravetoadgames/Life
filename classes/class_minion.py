# -*- coding: utf-8 -*-
from classes.class_minion_brain import Brain
from classes.class_minion_digestion import Digestion
from classes.class_minion_eyes import Eyes
from classes.class_minion_health import Health
from classes.class_minion_hearing import Hearing
from classes.class_minion_sex import Sex
from classes.class_event_emitter import EventEmitter
class Minion:

    
    def __init__(self):
        self.events = EventEmitter()

        self.sex = Sex(self.events)
        self.brain = Brain(self.events)
        self.health = Health(self.events)
        self.digestion = Digestion(self.events)
        self.eyes = Eyes(self.events)
        self.hearing = Hearing(self.events)
        
        self.thirst = 0

        self.setEmitters()

        self.summarize()


    def test(self):
        pass

    # ------------------------------------------------------------------
    # The heartbeat of a minion
    # ------------------------------------------------------------------
    def lifePulse(self):
        # Do all health related stuff
        if not self.health.isDead():
            self.health.setDead(self.health.growOlder())
        



    def setEmitters(self):
        self.events.subscribe("DEPRESSION_WARNING", self.test)



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
        