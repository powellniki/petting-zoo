# import the python datetime module to help us create a timestamp
from datetime import date

class Copperhead:
    def __init__(self, name, species, category):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.category = category
        self.slithering = True


    def __str__(self):
        return f"name:\n{self.name}\n\nspecies:\n{self.species}\n\ndate added: {self.date_added}"