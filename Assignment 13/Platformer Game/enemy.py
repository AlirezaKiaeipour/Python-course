import random
import arcade

class Enemy(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()

        self.stand_right_textures = [arcade.load_texture(":resources:images/animated_characters/zombie/zombie_idle.png")]
        self.stand_left_textures = [arcade.load_texture(":resources:images/animated_characters/zombie/zombie_idle.png",mirrored=True)]

        self.walk_right_textures = [arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk0.png"),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk1.png"),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk2.png"),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk3.png"),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk4.png"),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk5.png"),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk6.png"),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk7.png")]

        self.walk_left_textures = [arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk0.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk1.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk2.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk3.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk4.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk5.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk6.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/zombie/zombie_walk7.png",mirrored=True)]

        self.width = 100
        self.height = 100
        self.center_x = random.randint(100,700)
        self.center_y = 800
        self.speed = 4
        self.change_x = random.choice([-1,1]) * self.speed
