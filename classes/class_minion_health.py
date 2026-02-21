# -*- coding: utf-8 -*-
import random

class Health:
    age_expectancy = 0



    def __init__(self):
        self.setAgeExpectancy()
    


    # ------------------------------------------------------------------
    # Give age expectancy
    # ------------------------------------------------------------------
    def getAgeExpectancy(self):
        return str(self.age_expectancy)



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