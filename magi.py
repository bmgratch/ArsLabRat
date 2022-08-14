
# magi.py - this is a class designed to carry the important information about
# a magus for calculating their magical works

#TODO Get a record of all the data a magus needs
# 5 Techniques, 10 Forms
# Magic Theory, Stamina, Intelligence
# Aura? Not attached to magus, can be passed as part of calculation
# Verditius needs Philosophiae and Craft
# Ritual magic needs Philosophiae and Artes Liberales
# More advanced data can use Virtues and Flaws, lab and familiar

class Magus:
    """The numbers and mechanics of a Magus"""
    def __init__(self):

        # The magus name and House tradition
        self.name = "Generic Magus"
        self.house = "Ex Miscellanea"

        # Relevant Virtues and Flaws
        self.Virtues = ['Hermetic Magus']

        #TODO Should I make these a list instead of dict? Dict is clearer.
        # Arts comprised of Techniques and Forms
        self.tech = {'Cr':0, 'In':0, 'Mu':0, 'Pe':0, 'Re':0}
        self.form = {'An':0, 'Aq':0, 'Au':0, 'Co':0, 'He':0,
                     'Ig':0, 'Im':0, 'Me':0, 'Te':0, 'Vi':0}
        self.arts ={ **self.tech, **self.form}
        
        # The Characteristics of the Magus
        # Only Stamina and Intelligence matter for spellcasting or design
        self.char = {'Int':0, 'Sta':0}
        
        # The Abilities of the Magus
        # For most Lab Work, Magic Theory applies
        self.abilities = {
            'Magic Theory': 0,
            'Artes Liberales': 0,
            'Philosophiae': 0,
        }

# TODO Create string output for display
    def __str__(self):
        return  "%s, of House %s" % (self.name, self.house)
        