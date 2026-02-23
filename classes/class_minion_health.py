# -*- coding: utf-8 -*-
import random
from classes.class_minion_health_illness import Illness

class Health:

    
    
    def __init__(self):
        self.illness = Illness()

        self.age = 0
        self.aging_tick = 0.3
        self.age_expectancy = 0
        self.dead = False    
        self.setAgeExpectancy()


    # ------------------------------------------------------------------
    # Let the minion age and stay healthy (or not)
    # ------------------------------------------------------------------
    def growOlder(self):
        self.setAging()
        self.illness.checkSickness(self.age)
        






    # ------------------------------------------------------------------
    # Check if minion is dead (true or false)
    # ------------------------------------------------------------------
    def isDead(self):
        return self.dead



    # ------------------------------------------------------------------
    # Get minion's age
    # ------------------------------------------------------------------
    def getAge(self):
        return int(self.age)
    


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
    # Let the minion grow old
    # ------------------------------------------------------------------
    def setAging(self):
        if self.getAge() <= self.age_expectancy:
            self.age = self.age +self.aging_tick
        else:
            print('Died of old age.')
            print('-' * 79)
            print()
            self.dead = True


