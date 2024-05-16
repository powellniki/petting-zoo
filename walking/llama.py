# import the python datetime module to help us create a timestamp
from datetime import date

class Llama():
    def __init__(self, name, species, category, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.category = category
        self.walking = True
        self.shift = shift
        self.food = food

    def __str___(self):
        return f"{self.name} the {self.species} is available to pet during the {self.shift} shift"
    
    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%y")}')