# -*- coding: utf-8 -*-
import random

class Health:
    age = 0
    aging_tick = 0.15
    age_expectancy = 0
    dead = False    


    def __init__(self):
        self.setAgeExpectancy()



    # ------------------------------------------------------------------
    # Determine if minion becomes lethally ill
    # ------------------------------------------------------------------
    def checkSickness(self):
        x = random.randint(0,30000)
        
        if x <= self.age:
            # With aging, chance increases to become ill
            print('Got sick at age ' + str(self.getAge()) + ' and died!')
            self.dead = True



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
        
        if self.age <= self.age_expectancy:
            self.age = self.age +self.aging_tick
        else:
            print('Died at the age of ' + str(self.getAge()) + '.') 
            self.dead = True
