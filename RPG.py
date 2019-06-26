from time import sleep

class Character():

    def __init__(self, hp, ac, speed, xp):
        self.hp = hp
        self.ac = ac
        self.speed = speed
        self.xp = xp
        self.max_hp = hp
        self.level = 1
        self.is_alive = True
        self.is_conscious = True
    
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
            if self.xp >= 300 and self.xp < 900 and self.level == 1:
                self.level_up()
            if self.xp >= 900 and self.level == 2:
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
        self.max_hp = self.max_hp + 5
        self.speed = self.speed + 5
        self.level = self.level + 1

    def __str__(self):
        if self.is_alive:
            return 'HP: ' + str(self.hp) + ' AC: ' + str(self.ac) + ' Speed: ' + str(self.speed) + ' XP: ' + str(self.xp)
        else:
            return "You have died. "

def main():
    character1 = Character(20, 14, 30, 250)
    character1.take_damage(30)
    character1.xp_gain(50)
    character1.long_rest(5)
    print(character1)

main()