# -*- coding: utf-8 -*-
import random
from classes.minion.class_minion_health_illness import Illness

class Health:

    
    
    # ------------------------------------------------------------------
    # Let the minion age and stay healthy (or not)
    # ------------------------------------------------------------------
    def __init__(self, emitter):
        self.emitter = emitter

        self.illness = Illness(self.emitter)

        self.age = 0.0
        self.aging_tick = 0.3
        self.age_expectancy = 0
        self.dead = False    
        self.setAgeExpectancy()


    # ------------------------------------------------------------------
    # Let the minion age and stay healthy (or not)
    # ------------------------------------------------------------------
    def growOlder(self):
        self.setDead(self.illness.checkSickness(int(self.getAge())))
        
        if not self.isDead():
            return self.setAging()
        
        return self.isDead()




    # ------------------------------------------------------------------
    # Check if minion is dead (return true or false)
    # ------------------------------------------------------------------
    def isDead(self):
        return self.dead



    # ------------------------------------------------------------------
    # Get minion's age (default = float or integer)
    # ------------------------------------------------------------------
    def getAge(self, tp = "float"):
        if tp == 'int':
            return int(self.age)
        return self.age
    


    # ------------------------------------------------------------------
    # Get aging-tick which ages the minion
    # ------------------------------------------------------------------
    def getAgingTick(self):
        return self.aging_tick



    # ------------------------------------------------------------------
    # Give age expectancy
    # ------------------------------------------------------------------
    def getAgeExpectancy(self):
        return self.age_expectancy



    # ------------------------------------------------------------------
    # Determine the probable age
    # It's rare that someone gets older than 90 and even
    # more rare to die before 19 yo
    # ------------------------------------------------------------------
    def setAgeExpectancy(self):
        
        x = random.randint(70, 90)
        
        if random.randint(1,100) < 50:
            x = random.randint(50,69)
            
            if random.randint(1,100) < 45:
                x = random.randint(20,49)
                
                if random.randint(1,100) < 40:
                    x = random.randint(91,110)
    
                    if random.randint(1,100) < 35:
                        x = random.randint(1,19)
                
        self.age_expectancy = x
        


    # ------------------------------------------------------------------
    # Set the age
    # ------------------------------------------------------------------
    def setAge(self, age):
        self.age = age
        

        
    # ------------------------------------------------------------------
    # Let the minion grow old
    # ------------------------------------------------------------------
    def setAging(self):
        if self.getAge() <= self.getAgeExpectancy():
            self.setAge(self.getAge() + self.getAgingTick())
            return False
        else:
            print('Died of old age.')
            print('-' * 79)
            print()
            return True
                    


    # ------------------------------------------------------------------
    # Kill the minion
    # ------------------------------------------------------------------
    def setDead(self, dead_status):
        self.dead = dead_status


