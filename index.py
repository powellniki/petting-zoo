from slithering import Copperhead, Gecko, Lizard, RatSnake, Salamander
from swimming import Frog, Goldfish, Goose, Mallard, Turtle
from walking import Donkey, Goat, Horse, Llama, Pig


spot = Copperhead("Spot", "copperhead", "tank", "mice")
charlie = RatSnake("Charlie", "rat snake", "tank", "mice")
cookie = Lizard("Cookie", "lizard", "tank", "crickets")
bubbles = Gecko("Bubbles", "gecko", "tank", "bugs")
viper = Salamander("Viper", "salamander", "tank", "salamander chow")

alien = Mallard("Alien", "mallard", "pond", "bread chunks")
funky = Goldfish("Funky", "goldfish", "pond", "fish flakes")
jonathan = Turtle("Jonathan", "turtle", "pond", "turtle bites")
sniper = Goose("Sniper", "goose", "pond", "goose flakes")
legs = Frog("Legs", "frog", "pond", "bugs")

frank = Llama("Frank the Tank", "llama", "petting area", "midday", "llama chow")
tina = Goat("Tina", "goat", "petting area", "morning", "goat pellets")
nancy = Pig("Nancy", "pig", "petting area", "afternoon", "chilled mud")
alfred = Donkey("Alfred", "donkey", "petting area", "morning", "hay")
susan = Horse("Susan", "horse", "petting area", "afternoon", "hay")


# print(f"{frank.name} the {frank.species} is available to pet during the {frank.shift} shift")

# print(jonathan.feed())