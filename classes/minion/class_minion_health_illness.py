import random


class Illness:
    sickness_part_1 = [
        "stupifying", "blasphemic", "retarding", "painful", "blinding",
        "deafening", "back-curling",
        "grating", "hair-raising", "stuttering", "paralyzing", "sickening",
        "nauseating", "heart-stopping", "dehydrating", "gut-wrenching",
        "back-curling", "shocking", "perplexing", "stunning", "hurtful",
        ]

    sickness_part_2 = [
        "Wizard’s Hands", "Fellfrost Fever", "Mage’s Flu", "Shadelung",
        "Ooze-Sniffles", "Rust Lung", "Somatic Madness", "Dancing Mania",
        "Soul Rot", "Planar Gout", "Green Fever", "Ranger’s Ear",
        "Gold-Heart", "Violent Shakes", "Contagious Nightmares",
        "Polypox", "Gravesight", "Deep Shambles", "Whispering Tongue",
        "Mummy Rot", "Burning Fungi",
        ]



    def __init__(self, emitter):
        self.emitter = emitter

        self.sickness = ""
        
        pass
        


    # ------------------------------------------------------------------
    # Check if minion is sick
    # ------------------------------------------------------------------
    def isSick(self):
        if self.sickness != "":
            return True
        return False



    # ------------------------------------------------------------------
    # Determine if minion becomes lethally ill
    # ------------------------------------------------------------------
    def checkSickness(self, age = 0):
        x = random.randint(0,10000)
        
        if x <= age:
            # With aging, chance increases to become ill
            print('Got sick at age ' + str(age) + ' because of ' + self.getSickness() + ' and died!')
            print('-' * 79)
            print()
            return True
        
        return False



    # ------------------------------------------------------------------
    # Generate an illness
    # ------------------------------------------------------------------
    def getSickness(self):
        a = random.randint(0,len(self.sickness_part_1)-1)
        b = random.randint(0,len(self.sickness_part_2)-1)
        return self.sickness_part_1[a] + " " + self.sickness_part_2[b]


    
    