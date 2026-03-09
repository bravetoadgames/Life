"""
+----------------------------------------------------------------------+
| Class Brain                                                          |
+----------------------------------------------------------------------+
"""
import random

class Brain:
    

    def __init__(self, emitter):
        self.emitter = emitter

        self.dopamine = 100
        self.serotonin = 100
        
        self.setDopamine()
        self.setSerotonin()
        


    # ------------------------------------------------------------------
    # Single lifepulse in the brain's lifecycle
    # ------------------------------------------------------------------
    def lifePulseBrain(self):
        self.checkEmitters()


    # ------------------------------------------------------------------
    # Check for depression and execute any consequence that follows out of that
    # ------------------------------------------------------------------
    def checkEmitters(self):
        if self.getSerotonin() < 80:
            self.emitter.emit("BRAIN_DEPRESSION_WARNING", self.getSerotonin())

        if self.getDopamine() < 80:
            self.emitter.emit("BRAIN_SADNESS_WARNING", self.getDopamine())


        
    # ------------------------------------------------------------------
    # Get dopamine level
    # ------------------------------------------------------------------
    def getDopamine(self):
        return self.dopamine


    # ------------------------------------------------------------------
    # Get serotonin level
    # ------------------------------------------------------------------
    def getSerotonin(self):
        return self.serotonin


    # ------------------------------------------------------------------
    # Set dopamine level
    # ------------------------------------------------------------------
    def setDopamine(self):
        dopamine_level = 100

        a = random.randint(0,100)

        if a < 20:
            dopamine_level = random.randint(80,100)
        
        self.dopamine = dopamine_level


    # ------------------------------------------------------------------
    # Set serotonin level
    # ------------------------------------------------------------------
    def setSerotonin(self):
        serotonin_level = random.randint(85,95)

        a = random.randint(0,100)

        if a < 30:
            serotonin_level = random.randint(96,100)
            
            b = random.randint(0,100)
            
            if b < 30:
                serotonin_level = random.randint(30,84)
                
        self.serotonin = serotonin_level

