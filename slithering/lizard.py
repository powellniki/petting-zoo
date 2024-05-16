# import the python datetime module to help us create a timestamp
from datetime import date

class Lizard:
    def __init__(self, name, species, category, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.category = category
        self.slithering = True
        self.food = food

    def __str__(self):
        return f"name:\n{self.name}\n\nspecies:\n{self.species}\n\ndate added: {self.date_added}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')