import pygame
from dataclasses import dataclass
from platformers.assets.sprites import Button


@dataclass
class LanguageFx:
    martyspeech_fx: pygame.mixer.Sound
    coin_fx: pygame.mixer.Sound
    jump_fx: pygame.mixer.Sound
    game_over_fx: pygame.mixer.Sound


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
