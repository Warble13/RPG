from time import sleep
from random import randint


class Character():

    def __init__(self, hp, ac, speed, xp, mana):
        self.hp = hp
        self.ac = ac
        self.speed = speed
        self.xp = xp
        self.max_hp = hp
        self.level = 1
        self.is_alive = True
        self.is_conscious = True
        self.mana = mana
        self.max_mana = mana
    
    def take_damage(self, damage_amount):
        if self.is_alive:
            self.hp = self.hp - damage_amount
            if self.hp <= self.max_hp * (-1):
                self.hp = 0
                self.is_alive = False
            
            elif self.hp <= 0:
                self.is_conscious = False
                while self.hp < 0 :
                    self.long_rest(1)


    def xp_gain(self, xp_amount):
        if self.is_alive:
            self.xp = self.xp + xp_amount
            if self.xp >= 300 and self.level == 1:
                self.level_up()
            if self.xp >= 900 and self.level == 2:
                self.level_up()
            if self.xp >= 1800 and self.level == 3:
                self.level_up()
            

    def long_rest(self, rest_length):
        if self.is_alive:
            sleep(rest_length)
            self.hp = self.hp + (rest_length * 5)
            print("You're resting. ")
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            if self.hp >= 0:
                self.is_conscious = True

    def level_up(self):
        print("You've leveled up! ")
        self.max_hp = self.max_hp + 5
        self.speed = self.speed + 5
        self.level = self.level + 1

    def heal(self, heal_amount):
        if self.is_alive:
            self.hp = self.hp + heal_amount
            print("You're healing. ")
            if self.hp > self.max_hp:
                self.hp = self.max_hp
            if self.hp >= 0:
                self.is_conscious = True
            self.heal_amount = 0
        
    def armor_increase(self, temp_ac):
        if self.is_alive:
            self.ac = temp_ac

    def __str__(self):
        if self.is_alive:
            return 'HP: ' + str(self.hp) + ' AC: ' + str(self.ac) + ' Speed: ' + str(self.speed) + ' XP: ' + str(self.xp)
        else:
            return "You have died. "


class Wizard(Character):
    def __init__(self):
        hp = randint(9, 16)
        ac = randint(9, 13)
        speed = 30
        xp = 0
        mana = 100
        super().__init__(hp, ac, speed, xp, mana)
    
    def spells(self):
        damage_given = None
        spell_choice = None
        spell_list = {1:'Mana Bolt', 2:'Cure wounds', 3:'Mage Armor'}
        spell_info = {1: 'You shoot a bolt of mana that deals damage. ', 2: 'You heal your wounds. ', 3:'You make armor out of mana, increasing your defense. '}
        print('Your spells: ')
        for num in spell_list:
            print(str(num) + '. ' + spell_list[num])
        init_choice = str(input("Which spell will you use? "))
        init_choice = init_choice.lower()
        if init_choice == 'mana bolt' or init_choice == '1' and self.mana >= 20:
            spell_choice = 1
            damage_given = randint(8, 12)
            if damage_given == 12:
                damage_given = 50
            self.mana = self.mana - 20
        elif init_choice == 'cure wounds' or init_choice == '2' and self.mana >= 20:
            spell_choice = 2
            self.heal(10)
            self.mana = self.mana - 20
        elif init_choice == 'mage armor' or init_choice == '3' and self.mana >= 20:
            spell_choice = 3
            self.armor_increase(16)
            self.mana = self.mana - 20
        else:
            print('Choose a valid spell. ')
            self.spells()
        if spell_choice != None:
            print(spell_info.get(spell_choice))
        if self.mana == 0:
            battle_rest = int(input('You need to rest. How long would you like to rest? '))
            self.long_rest(battle_rest)
        print('You now have ' + str(self.mana) + ' mana left. ')
        return damage_given

    def level_up(self):
        Character.level_up(self)
        self.mana = self.mana + 50

    def long_rest(self, rest_length):
        Character.long_rest(self, rest_length)
        self.mana = self.mana + (rest_length * 20)
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        super().long_rest(rest_length)
    
    def __str__(self):
        if self.is_alive:
            return 'Wizard - HP: ' + str(self.hp) + ' AC: ' + str(self.ac) + ' Speed: ' + str(self.speed) + ' XP: ' + str(self.xp)
        else:
            return "You have died, Wizard. "

class Monk(Character):
    def __init__(self):
        hp = randint(17, 22)
        ac = randint(13, 17)
        speed = 45
        xp = 0
        ki = 5
        super().__init__(hp, ac, speed, xp, ki)
    
    def monk_attacks(self):
        damage_given = None
        attack_choice = None
        attack_list = {1:'Flurry of Blows', 2:'Calm Emotions', 3:'Mental Fortitude'}
        attack_info = {1: 'You attack with your fists rapidly. ', 2: 'You calm your emotions, relaxing and slightly healing yourself. ', 3:'You turn your mental resolve into defense. '}
        print('Your attacks: ')
        for num in attack_list:
            print(str(num) + '. ' + attack_list[num])
        init_choice = str(input("Which attack will you use? "))
        init_choice = init_choice.lower()
        if init_choice == 'flurry of blows' or init_choice == '1' and self.mana >= 1:
            attack_choice = 1
            damage_given = randint(6, 15)
            if damage_given == 15:
                damage_given = 50
            self.mana = self.mana - 1
        elif init_choice == 'cure wounds' or init_choice == '2' and self.mana >= 1:
            attack_choice = 2
            self.heal(5)
            self.mana = self.mana - 1
        elif init_choice == 'mental fortitude' or init_choice == '3' and self.mana >= 1:
            attack_choice = 3
            self.armor_increase(18)
            self.mana = self.mana - 1
        else:
            print('Choose a valid attack. ')
            self.monk_attacks()
        if attack_choice:
            print(attack_info.get(attack_choice))
            print('You now have ' + str(self.mana) + ' ki left. ')
        if self.mana == 0:
            battle_rest = int(input('You need to rest. How long would you like to rest? '))
            self.long_rest(battle_rest)
        return damage_given

    def level_up(self):
        Character.level_up(self)
        self.mana = self.mana + 1

    def long_rest(self, rest_length):
        Character.long_rest(self, rest_length)
        self.mana = self.mana + (rest_length)
        if self.mana > self.max_mana:
            self.mana = self.max_mana
        super().long_rest(rest_length)

    def __str__(self):
        if self.is_alive:
            return 'Monk - HP: ' + str(self.hp) + ' AC: ' + str(self.ac) + ' Speed: ' + str(self.speed) + ' XP: ' + str(self.xp)
        else:
            return "You have died, Monk. "


def main():
    wizard1 = Wizard()
    monk1 = Monk()
    print(wizard1)
    print(monk1)
    while wizard1.is_alive and monk1.is_alive:
        if wizard1.is_alive and wizard1.is_conscious:
            damage = wizard1.spells()
            if damage:
                monk1.take_damage(damage)
        if monk1.is_alive and monk1.is_conscious:
            damage = monk1.monk_attacks()
            if damage:
                wizard1.take_damage(damage)
        if not wizard1.is_alive:
            print('Monk wins! ')
            print(monk1)
            monk1.xp_gain(100)
        if not monk1.is_alive:
            print('Wizard wins! ')
            print(wizard1)
            wizard1.xp_gain(100)
        print(wizard1)
        print(monk1)


main() 
