import random
import time
import math
import arcade

class SpaceCraft(arcade.Sprite):
    def __init__(self,w):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.width = 48
        self.height = 48
        self.speed = 4
        self.center_x = w // 2
        self.center_y = 38
        self.angle = 0
        self.change_angle = 0
        self.change_x = 0
        self.bullet_list = []
        self.score = 0
        self.counter = 1
        
    
    def rotate(self):
        self.angle += self.change_angle * self.speed

    def move(self):
        self.center_x += self.change_x * self.speed 

    def fire(self):
        self.bullet_list.append(Bullet(self))
##################################################################################
class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed = 8
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.angle = host.angle

    def move(self):
        self.center_x -= self.speed * math.sin(math.radians(self.angle))
        self.center_y += self.speed * math.cos(math.radians(self.angle))
###################################################################################
class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip3_orange.png")
        self.width = 48
        self.height = 48
        self.center_x = random.randint(1,w)
        self.center_y = h
        self.speed = 2 
        self.angle = 180
        
    def move(self):
        self.center_y -= self.speed 
#################################################################



#################################################################################
class Game(arcade.Window):
    def __init__(self):
        self.wid = 600
        self.hei = 500
        self.health = 3
        super().__init__(self.wid,self.hei,"Silver SpaceCraft")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.background_black = arcade.load_texture("black.png")
        self.explosion_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.fire_sound = arcade.load_sound(":resources:sounds/laser2.wav")
        self.space = SpaceCraft(self.wid)
        self.enemy_list = []
        self.start = time.time()
        

    def on_draw(self):
        arcade.start_render()
        self.space.draw()
        arcade.draw_lrwh_rectangle_textured(0,0,self.wid,self.hei,self.background)
        for i in self.space.bullet_list:
            i.draw()
        for j in self.enemy_list:
            j.draw()
        arcade.draw_text(f"Score: {self.space.score}",480,18,arcade.color.GREEN,bold=True,font_size=17)
          
        arcade.draw_text('❤' * self.health,25,13,arcade.color.RED,bold=True,font_size=22)
        if self.health ==0:
            arcade.draw_lrwh_rectangle_textured(0,0,self.wid,self.hei,self.background_black)
            arcade.draw_text("GameOver",140,240,arcade.color.RED,50)
            time.sleep(1)
            arcade.exit()
    
                

    def on_update(self, delta_time: float):
        self.end = time.time()
        if self.end - self.start > random.randint(3,15):
            self.enemy_list.append(Enemy(self.wid,self.hei))
            self.start =  time.time()
        self.space.move()
        self.space.rotate()
        for i in self.space.bullet_list:
            i.move()
        
        for j in self.enemy_list:
            j.move()
           
        for j in self.enemy_list:
            if j.center_y < -20:
                self.health -=1 
                self.enemy_list.remove(j)

        for i in self.space.bullet_list:
            if i.center_x <-10 or i.center_x > self.wid or i.center_y < -10 or i.center_y > self.hei:
                self.space.bullet_list.remove(i)

        for i in self.space.bullet_list:
            for j in self.enemy_list:
                if arcade.check_for_collision(i,j):
                    self.enemy_list.remove(j)
                    self.space.bullet_list.remove(i)
                    self.space.score +=1
                    arcade.play_sound(self.explosion_sound)
    
        
    def on_key_press(self,key,modifiers):
        if key== arcade.key.RIGHT:
            self.space.change_angle = -1
        elif key== arcade.key.LEFT:
            self.space.change_angle = 1
        elif key== arcade.key.A:
            self.space.change_x = -1
        elif key== arcade.key.D:
            self.space.change_x = 1
        elif key== arcade.key.SPACE:
            self.space.fire()
            arcade.play_sound(self.fire_sound)


    def on_key_release(self,key,modifiers):
        self.space.change_x = 0
        self.space.change_angle = 0

game =Game()
arcade.run()

