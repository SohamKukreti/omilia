from platformers.platformer import Platformer, World, Player, PlatformerConfig, LanguageFx, LanguageImages, Buttons, Button, Language
from os import path
import pickle
import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_group, x, y):
        super().__init__(coin_group)
        self.image = pygame.image.load('English/img/coin.png')


class EnglishPlatformer(Platformer):
    def __init__(self):
        super().__init__()
        init_level = 0
        if path.exists(f'English/level{init_level}_data'):
            pickle_in = open(f'English/level{init_level}_data', 'rb')
            world_data = pickle.load(pickle_in)
        else:
            raise Exception(f'Could not load level{init_level}_data from file')
        self.world = World(world_data, Language.ENGLISH)
        pygame.mixer.music.load("English/img/music.wav")
        pygame.mixer.music.play(-1)

    def reset_world(self, level):
        self.world.player.reset(100, PlatformerConfig.screen_height - 130)
        del self.world

        # load in level data and create world
        if path.exists(f'English/level{level}_data'):
            pickle_in = open(f'English/level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)
        else:
            raise Exception(f'Could not load level{level}_data from file')
        self.world = World(world_data, Language.ENGLISH)

        # create dummy coin for showing the score
        score_coin = Coin(self.world.coin_group, PlatformerConfig.tile_size // 2, PlatformerConfig.tile_size // 2)
        self.world.coin_group.add(score_coin)
        return self.world

    def load_fx(self) -> LanguageFx:
        return LanguageFx(
            pygame.mixer.Sound("English/img/martySpeech.wav"),
            pygame.mixer.Sound('English/img/coin.wav'),
            pygame.mixer.Sound('English/img/jump.wav'),
            pygame.mixer.Sound('English/img/game_over.wav'),
        )

    def load_images(self) -> LanguageImages:
        return LanguageImages(
            pygame.image.load('English/img/sun.png'),
            pygame.image.load('English/img/bgimg.png'),
            pygame.image.load('English/img/restart_btn.png'),
            pygame.image.load('English/img/start_btn.png'),
            pygame.image.load('English/img/exit_btn.png'),
            pygame.image.load("English/img/martyspeechimg.png")
        )

    def create_buttons(self) -> Buttons:
        return Buttons(
            start_button=Button(
                PlatformerConfig.screen_width // 2 - 350,
                PlatformerConfig.screen_height // 2,
                self.images.start_img
            ),
            restart_button=Button(
                PlatformerConfig.screen_width // 2 - 50,
                PlatformerConfig.screen_height // 2 + 100,
                self.images.restart_img
            ),
            exit_button=Button(
                PlatformerConfig.screen_width // 2 + 150,
                PlatformerConfig.screen_height // 2,
                self.images.exit_img
            ),
        )
