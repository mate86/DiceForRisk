import random

# ========== Functions ==========

def Dice(member):
    member = int(member)
    DiceValue = []
    for i in range(member):
        DiceValue.append(random.randrange(1,7))
    return DiceValue

def AttackResult(diceattacker):
    if len(diceattacker) == 1:
        print("  Attacker: " + str(diceattacker[0]))
    if len(diceattacker) == 2:
        print("  Attacker: " + str(diceattacker[0]) + "-" + str(diceattacker[1]))
    if len(diceattacker) == 3:
        print("  Attacker: " + str(diceattacker[0]) + "-" + str(diceattacker[1]) + "-" + str(diceattacker[2]))

def DefendResult(dicedefender):
    if len(dicedefender) == 1:
        print("  Defender: " + str(dicedefender[0]))
    if len(dicedefender) == 2:
        print("  Defender: " + str(dicedefender[0]) + "-" + str(dicedefender[1]))
    if len(dicedefender) == 3:
        print("  Defender: " + str(dicedefender[0]) + "-" + str(dicedefender[1]) + "-" + str(dicedefender[2]))

def Outcome(diceattacker, dicedefender):
    AttackerUnitLost = 0
    DefenderUnitLost = 0
    if len(diceattacker) <= len(dicedefender):
        for i in range(len(diceattacker)):
            if diceattacker[i] <= dicedefender[i]:
                AttackerUnitLost += 1
            else:
                DefenderUnitLost += 1
    if len(diceattacker) > len(dicedefender):
        for i in range(len(dicedefender)):
            if diceattacker[i] <= dicedefender[i]:
                AttackerUnitLost += 1
            else:
                DefenderUnitLost += 1

    print("\nOutcome:")
    print("  Attacker: Lost " + str(AttackerUnitLost) + " units")
    print("  Defender: Lost " + str(DefenderUnitLost) + " units")


# ========== Main ==========

Attackers = 0
while int(Attackers) < 1 or int(Attackers) > 3:
    Attackers = input("How many units attack: ")
DiceAttacker = Dice(Attackers)
    
Defenders = 0
while int(Defenders) < 1 or int(Defenders) > 3:
    Defenders = input("How many units defend: ")
DiceDefender = Dice(Defenders)

print("\nDice:")
AttackResult(DiceAttacker)
DefendResult(DiceDefender)
Outcome(DiceAttacker, DiceDefender)