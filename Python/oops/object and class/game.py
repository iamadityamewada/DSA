class Game:
    def __init__(self,):
        print("Welcome to the game")
        self.life = 5
        p_name = input("Enter Player Name: ")
        self.name = p_name

    def attack(self, enemy):
        enemy.life -= 1
        if enemy.life>0:
         print(f"{self.name} attack on {enemy.name}")
        #  self.show_life()
        else:
           print("Game Over")
           print("DEAD" , enemy.name) 
    def show_life(self):
        if self.life <= 0:
           print("Game Over")
        else:     
          print("Life: " , self.life , self.name)

    def add_life(self):
        if self.life>0 and self.life < 5:
           self.life += 1
           print("life increase by 1")
        elif self.life == 0:
            print( f"{self.name} is already dead")   
        elif self.life == 5:
           print(f"{self.name} have enough life")      

p1 = Game()
p2 = Game()

p1.attack(p2)
p1.attack(p2)
p2.attack(p1)
p1.show_life()
p2.show_life()
