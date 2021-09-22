import time
import random
from arcade.sprite_list.spatial_hash import check_for_collision
from enemy import Bird, Onecoc, Threecac, Twocac
from player import Player
from land import Land
import arcade

class Game(arcade.View):
    def __init__(self):
        self.wid = 800
        self.hei = 700
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        self.jump = arcade.load_sound(":resources:sounds/jump3.wav")
        self.lose = arcade.load_sound(":resources:sounds/hurt3.wav")
        self.background = arcade.load_texture("black.png")
        self.player  = Player()
        self.land_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()
        self.max_score = 0
        self.count = 0
        for land in range(0,801,80):
            self.land_list.append(Land(land,5))
        self.physic = arcade.PhysicsEnginePlatformer(self.player,self.land_list,gravity_constant=0.5)
        self.start_time = time.time()
        self.bird_time = time.time()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        for land in self.land_list:
            land.draw()
        
        for enemy in self.enemy_list:
            enemy.draw()

        if self.player.score > 1500:
            arcade.set_background_color(arcade.color.BLACK)
        elif self.player.score > 2500:
            arcade.set_background_color(arcade.color.WHITE_SMOKE)

            
        arcade.draw_text(f"Score: {self.player.score}",630,670,arcade.color.RED,20)
        arcade.draw_text(f"Max Score: {max(max_list)}",20,670,arcade.color.RED,20)
        
        for enemy in self.enemy_list:
            if check_for_collision(self.player,enemy):
                arcade.play_sound(self.lose)
                arcade.draw_lrwh_rectangle_textured(0,0,self.wid,self.hei,self.background)
                arcade.draw_text("Game Over",230,400,arcade.color.WHITE_SMOKE,50,bold=True)
                arcade.draw_text("Press *Space* to play agane",230,350,arcade.color.WHITE_SMOKE,20)
                max_list.append(self.player.score)
                time.sleep(2)
                


    def on_update(self, delta_time: float):
        self.player.score +=0.5
        self.end_time = time.time()
        self.one_cac = Onecoc(self.wid)
        self.two_cac = Twocac(self.wid)
        self.bird = Bird(self.wid)
        self.three_cac = Threecac(self.wid)
        if self.end_time - self.start_time > random.randint(3,5) and self.player.score > 1000:
            self.count +=1
            self.enemy_list.append(random.choice([self.one_cac,self.two_cac,self.three_cac,self.bird]))
            for enemy in self.enemy_list:
                enemy.control_speed(self.player.control_speed)
                if self.count % 5 ==0:
                    self.player.control_speed +=0.1
            self.start_time = time.time()
        elif self.end_time - self.start_time > random.randint(3,5) and self.player.score < 1000:
            self.count +=1
            self.enemy_list.append(random.choice([self.one_cac,self.two_cac,self.three_cac]))
            for enemy in self.enemy_list:
                enemy.control_speed(self.player.control_speed)
                if self.count % 5 ==0:
                    self.player.control_speed +=0.1
            self.start_time = time.time()
       
        self.physic.update()
        self.player.update_animation()
        for enemy in self.enemy_list:
            enemy.update_animation()

        for enemy in self.enemy_list:
            enemy.move()

    def on_key_press(self,key,modifiers):
        
        if key== arcade.key.UP:
            if self.physic.can_jump():
                self.player.change_y = 13
                arcade.play_sound(self.jump)
        if key== arcade.key.SPACE:
            self.window.show_view(Game())
        

    def on_key_release(self,key,modifiers):
        self.player.change_x =0    

max_list = [0]
window = arcade.Window(800,700,"T-Rex")
game = Game()
window.show_view(game)
arcade.run()