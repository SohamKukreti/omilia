import pygame
from dataclasses import dataclass
from platformers.assets.sprites import Button


@dataclass
class LanguageFx:
    martyspeech_fx: pygame.mixer.Sound
    coin_fx: pygame.mixer.Sound
    jump_fx: pygame.mixer.Sound
    game_over_fx: pygame.mixer.Sound
    bg_music_path: str
    option_sound: pygame.mixer.Sound
    correct_sound: pygame.mixer.Sound
    wrong_sound: pygame.mixer.Sound
    question_bg_music: str




@dataclass
class Buttons:
    start_button: Button
    exit_button: Button
    restart_button: Button


@dataclass
class LanguageImages:
    sun_img: pygame.Surface
    bg_img: pygame.Surface
    restart_img: pygame.Surface
    start_img: pygame.Surface
    exit_img: pygame.Surface
    martyspeech_img: pygame.Surface
    coin_img: pygame.Surface
    lava_img: pygame.Surface
    exit: pygame.Surface
    platform: pygame.Surface
    dirt_img: pygame.Surface
    grass_img: pygame.Surface
    enemy_img: pygame.Surface
    dead_img: pygame.Surface
    prof_slide: pygame.Surface

    """dirt_img = pygame.image.load(f'{language.value}/img/dirt.png')
        grass_img = pygame.image.load(f'{language.value}/img/grass.png')
        enemy_img = pygame.image.load(f'{language.value}/img/blob.png')"""
