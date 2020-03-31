"""im just tryna come up with some remotely christmas-related stuff in these titles"""
from copy import deepcopy

bossHealth = 71
bossDamage = 10
spellList = {'Missile': 53, 'Drain': 73, 'Shield': 113, 'Recharge': 229, 'Poison': 173}
effects = {'Shield', 'Poison', 'Recharge'}

class Player:
    def __init__(self):
        self.effects = []
        self.health = 50
        self.mana = 500
        self.manaSpent = 0
        self.bossHealth = bossHealth
        self.castedSpells = []

    def cast(self, spell):
        if spell == 'Missile':
            self.bossHealth -= 4

        elif spell == 'Drain':
            self.bossHealth -= 2
            self.health += 2

        elif spell == 'Shield':
            self.effects.append(['Shield', 6])

        elif spell == 'Recharge':
            self.effects.append(['Recharge', 5])

        elif spell == 'Poison':
            self.effects.append(['Poison', 6])

        self.manaSpent += spellList[spell]
        self.mana -= spellList[spell]
        self.castedSpells.append(spell)

    def applyEffects(self):
        for e in self.effects:
            if e[0] == 'Poison':
                self.bossHealth -= 3
            elif e[0] == 'Recharge':
                self.mana += 101
            e[1] -= 1
        self.effects = [e for e in filter(lambda ef: ef[1] > 0, self.effects)]

    def bossAttack(self):
        damage = bossDamage if 'Shield' not in [ef[0] for ef in self.effects] else bossDamage - 7
        if damage >= 1:
            self.health -= damage
        else:
            self.health -= 1

    def checkDead(self):
        if self.health <= 0:
            return 'oh noes'
        elif self.bossHealth <= 0:
            return 'we did it yay', self.manaSpent
        return 'what'

def simulate(hardCore):  # takes in a game and returns all possible outcomes
    loScore = float('inf')
    allGames = [Player()]
    while allGames:
        newGames = []
        for g in allGames:
            g.applyEffects()
            if g.checkDead() == 'what':
                if hardCore:
                    g.health -= 1
                for s in spellList:
                    newG = deepcopy(g)
                    if s in [x[0] for x in newG.effects] and s in effects or spellList[s] > g.mana:
                        continue
                    newG.cast(s)
                    results = newG.checkDead()
                    if results == 'what':  # check if the player won or smth
                        if newG.manaSpent > loScore:
                            continue  # it's hopeless... well never get lower mana than this
                    elif results == 'oh noes':
                        continue
                    elif results[0] == 'we did it yay' and results[1] < loScore:
                        loScore = results[1]

                    newG.applyEffects()  # maybe the effects will kill the boss
                    if newG.checkDead()[0] == 'we did it yay' and newG.checkDead()[1] < loScore:
                        loScore = newG.checkDead()[1]
                        continue

                    newG.bossAttack()  # well, boss's turn this time
                    results = newG.checkDead()
                    if results == 'what':
                        newGames.append(newG)  # onto the next round!
                    elif results == 'oh noes':
                        continue  # there's no way the player can win right after boss's turn right

            elif g.checkDead() == 'oh noes':  # probably will never come into effect but eh
                continue

            elif g.checkDead()[0] == 'we did it yay' and g.checkDead()[1] < loScore:  # if boss gets killed by effects
                loScore = g.checkDead()[1]  # by a casted effect
        allGames = newGames
    return loScore

print('FINALLY THIS TOOK ME SO FRICKIN LONG: %i' % simulate(False))
print('but at least part two wasnt that hard to implement: %i' % simulate(True))
print('and its slow but whatever')
