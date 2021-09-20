from enemy import Enemy
from boy import Boy
from land import Box1, Box2, Land,Box
import time
import random
import arcade

class Game(arcade.Window):
    def __init__(self):
        self.wid = 800
        self.hei = 700
        super().__init__(self.wid,self.hei,"Platform Game")
        self.background =  arcade.load_texture("image.png")
        self.keys = arcade.Sprite(":resources:images/items/keyYellow.png")
        self.background_win = arcade.load_texture("smoke.jpg")
        self.background_lost = arcade.load_texture("black.jpg")
        self.keys.center_x = 40
        self.keys.center_y = 570
        self.keys.width = 50
        self.keys.height = 50

        self.lock = arcade.Sprite(":resources:images/tiles/lockYellow.png")
        self.lock.center_x = 770
        self.lock.center_y = 440
        self.lock.width = 50
        self.lock.height = 50
        self.land_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.boy = Boy()
        for land in range(0,810,80):
            self.land_list.append(Land(land,5))

        for box in range(400,570,80):
            self.land_list.append(Box(box,180))

        for i in range(250,350,80):
            self.land_list.append(Box(i,400))

        for j in range(40,100,80):
            self.land_list.append(Box1(j,500))

        for sand in range(760,800,80):
            self.land_list.append(Box2(sand,370))

        self.physic = arcade.PhysicsEnginePlatformer(self.boy,self.land_list,gravity_constant=0.6)
        self.physic_list = []
        self.start_time = time.time()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.wid,self.hei,self.background)
        for land in self.land_list:
            land.draw()
        self.boy.draw()
        for i in self.enemy_list:
            i.draw()
        try:self.keys.draw()
        except:pass
        self.lock.draw()
        arcade.draw_text("Health: ",10,668,arcade.color.RED,18,bold=True)
        arcade.draw_xywh_rectangle_filled(100,660,self.boy.health,30,arcade.color.YELLOW)
        if self.boy.health == 0:
            arcade.draw_lrwh_rectangle_textured(0,0,self.wid,self.hei,self.background_lost)
            arcade.draw_text("Game Over",150,330,arcade.color.WHITE_SMOKE,70,bold=True)
            time.sleep(1)
            arcade.exit()
        if arcade.check_for_collision(self.boy,self.lock) and  len(self.boy.pocket_list) ==1:
            arcade.draw_lrwh_rectangle_textured(0,0,self.wid,self.hei,self.background_win)
            arcade.draw_text("You Win",230,340,arcade.color.COOL_BLACK,70,bold=True,italic=True)
            time.sleep(1)
            arcade.exit()
            
    def on_update(self, delta_time: float):
        self.end_time = time.time()
        self.enemy = Enemy()
        if self.end_time - self.start_time > random.randint(3,6):
            self.enemy_list.append(self.enemy)
            self.physic_list.append(arcade.PhysicsEnginePlatformer(self.enemy,self.land_list,gravity_constant=0.5))
            self.start_time = time.time()
        self.physic.update()
        for i in self.physic_list:
            i.update()
        self.boy.update_animation()
        for enemy in self.enemy_list:
            enemy.update_animation()
        try:
            if arcade.check_for_collision(self.boy,self.keys):
                self.boy.pocket_list.append(self.keys)
                del self.keys
        except:pass

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.boy,enemy):
                self.enemy_list.remove(enemy)
                self.boy.health -= 40
        
    def on_key_press(self,key,modifiers):
        if key== arcade.key.RIGHT:
            self.boy.change_x = 1 * self.boy.speed
        elif key== arcade.key.LEFT:
            self.boy.change_x = -1 * self.boy.speed
        elif key== arcade.key.UP:
            if self.physic.can_jump():
                self.boy.change_y = 5.5 * self.boy.speed

    def on_key_release(self,key,modifiers):
        self.boy.change_x = 0        


Game()
arcade.run()