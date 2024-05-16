from slithering import Copperhead, Gecko, Lizard, RatSnake, Salamander
from swimming import Frog, Goldfish, Goose, Mallard, Turtle
from walking import Donkey, Goat, Horse, Llama, Pig


spot = Copperhead("Spot", "copperhead", "tank")
charlie = RatSnake("Charlie", "rat snake", "tank")
cookie = Lizard("Cookie", "lizard", "tank")
bubbles = Gecko("Bubbles", "gecko", "tank")
viper = Salamander("Viper", "salamander", "tank")

alien = Mallard("Alien", "mallard", "pond")
funky = Goldfish("Funky", "goldfish", "pond")
jonathan = Turtle("Jonathan", "turtle", "pond")
sniper = Goose("Sniper", "goose", "pond")
legs = Frog("Legs", "frog", "pond")

frank = Llama("Frank the Tank", "llama", "petting area", "midday")
tina = Goat("Tina", "goat", "petting area", "morning")
nancy = Pig("Nancy", "pig", "petting area", "afternoon")
alfred = Donkey("Alfred", "donkey", "petting area", "morning")
susan = Horse("Susan", "horse", "petting area", "afternoon")


print(f"{frank.name} the {frank.species} is available to pet during the {frank.shift} shift")