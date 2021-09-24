from bird import Bird
import time
import random
from arcade.sprite_list.spatial_hash import check_for_collision
from cac import Onecoc, Threecac, Twocac
from player import Player
from land import Land
import arcade

class Game(arcade.View):
    def __init__(self):
        self.wid = 800
        self.hei = 700
        self.speed = 3
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.jump = arcade.load_sound(":resources:sounds/jump3.wav")
        self.background = arcade.load_texture("img/black.png")
        self.player  = Player()
        self.land_list = arcade.SpriteList()
        self.cac_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        self.max_score = 0
        self.count = 0
        for land in range(0,801,80):
            self.land_list.append(Land(land,5))
        self.physic = arcade.PhysicsEnginePlatformer(self.player,self.land_list,gravity_constant=0.5)
        self.start_cac_time = time.time()
        self.start_bird_time = time.time()
        self.cloud = arcade.Sprite("img/cloud.png")
        self.cloud.width = 100
        self.cloud.height = 100
        self.cloud.center_x = 400
        self.cloud.center_y = 550

        self.cloud1 = arcade.Sprite("img/cloud.png")
        self.cloud1.width = 100
        self.cloud1.height = 100
        self.cloud1.center_x = 600
        self.cloud1.center_y = 450

        self.cloud2 = arcade.Sprite("img/cloud.png")
        self.cloud2.width = 100
        self.cloud2.height = 100
        self.cloud2.center_x = 130
        self.cloud2.center_y = 380
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.cloud.draw()
        self.cloud1.draw()
        self.cloud2.draw()
        
        for land in self.land_list:
            land.draw()
        
        for cac in self.cac_list:
            cac.draw()

        for bird in self.bird_list:
            bird.draw()

        if self.count % 20 == 0:
            arcade.set_background_color(arcade.color.WHITE_SMOKE)
        elif self.count % 10 ==0:
            arcade.set_background_color(arcade.color.BLACK)
         
        arcade.draw_text(f"Score: {self.player.score}",630,670,arcade.color.RED,20)
        arcade.draw_text(f"Max Score: {max(max_list)}",20,670,arcade.color.RED,20)
        
        for cac in self.cac_list:
            if check_for_collision(self.player,cac):
                arcade.draw_lrwh_rectangle_textured(0,0,self.wid,self.hei,self.background)
                arcade.draw_text("Game Over",230,400,arcade.color.WHITE_SMOKE,50,bold=True)
                arcade.draw_text("Press *Space* to Play Agane",230,330,arcade.color.WHITE_SMOKE,20)
                arcade.draw_text("Press *Esc* to Exit Game ",250,280,arcade.color.WHITE_SMOKE,20)
                max_list.append(self.player.score)
                time.sleep(2)

        for bird in self.bird_list:
            if check_for_collision(self.player,bird):
                arcade.draw_lrwh_rectangle_textured(0,0,self.wid,self.hei,self.background)
                arcade.draw_text("Game Over",230,400,arcade.color.WHITE_SMOKE,50,bold=True)
                arcade.draw_text("Press *Space* to play agane",230,330,arcade.color.WHITE_SMOKE,20)
                arcade.draw_text("Press *Esc* to Exit Game ",250,280,arcade.color.WHITE_SMOKE,20)
                max_list.append(self.player.score)
                time.sleep(2)
                
    def on_update(self, delta_time: float):
        self.player.score +=0.5
        self.end_cac_time = time.time()
        self.one_cac = Onecoc(self.wid,self.speed)
        self.two_cac = Twocac(self.wid,self.speed)
        self.three_cac = Threecac(self.wid,self.speed)
        if self.end_cac_time - self.start_cac_time > random.randint(3,6):
            self.cac_list.append(random.choice([self.one_cac,self.two_cac,self.three_cac]))
            self.count +=1
            if self.count % 5 ==0:
                self.speed += 0.5
            self.start_cac_time = time.time()
        
        self.end_bird_time = time.time()
        if self.end_bird_time - self.start_bird_time > 17 and self.player.score > 1000:
            self.bird = Bird(self.wid,self.speed)
            self.bird_list.append(self.bird)
            self.start_bird_time = time.time()
 
        self.physic.update()
        self.player.update_animation()
       
        for bird in self.bird_list:
            bird.update()
            bird.update_animation()
            if bird.center_x < -30:
                self.bird_list.remove(bird)

        for cac in self.cac_list:
            cac.update()
            if cac.center_x < -30:
                self.cac_list.remove(cac)

    def on_key_press(self,key,modifiers):
        
        if key== arcade.key.UP:
            if self.physic.can_jump():
                self.player.change_y = 13
                arcade.play_sound(self.jump)
        if key== arcade.key.SPACE:
            self.window.show_view(Game())
        if key== arcade.key.DOWN:
            self.player.walk_down_textures = [arcade.load_texture("img/down1.png")]
        if key== arcade.key.ESCAPE:
            arcade.exit()
    
    def on_key_release(self,key,_modifiers):
        self.player.walk_down_textures = self.player.stand_right_textures
           
max_list = [0]
window = arcade.Window(800,700,"T-Rex Game")
game = Game()
window.show_view(game)
arcade.run()