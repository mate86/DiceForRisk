import random

def Dice():
    DiceValue = random.randrange(1,7)
    return DiceValue

print("Dice:")
print("  Attacker: " + str(Dice()) + "-" + str(Dice())+ "-" + str(Dice()))
print("  Defender: " + str(Dice()) + "-" + str(Dice()))