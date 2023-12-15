from dataclasses import dataclass
from enum import Enum

import pygame
from pygame import mixer


@dataclass
class PlatformerConfig:
    screen_width: int = 1000
    screen_height: int = 1000
    fps: int = 60
    tile_size: int = 50
    max_levels: int = 7
    white: tuple = (255, 255, 255)
    blue: tuple = (0, 0, 255)
    world_data: list = None
    font: pygame.font = pygame.font.SysFont('Bauhaus 93', 70)
    font_score: pygame.font = pygame.font.SysFont('Bauhaus 93', 30)


class Colours(Enum):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)


class Language(Enum):
    ENGLISH = "English"
    HINDI = "hindi"
    BANGLA = "bangla"


class LevelState(Enum):
    START = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
    EXIT = 5


class PlatformerState(Enum):
    MAIN_MENU = 1
    PLAYING_LEVEL = 2
    QUESTION = 3


class CollisionType(Enum):
    BLOB = 1
    LAVA = 2
    EXIT = 3
    NONFATAL = 4
    COIN = 5


class PlayerEvent(Enum):
    JUMP = 1
    NOT_JUMPED = 2
    LEFT = 3
    RIGHT = 4
    NONE = 5


@dataclass
class LanguageFx:
    martyspeech_fx: pygame.mixer.Sound
    coin_fx: pygame.mixer.Sound
    jump_fx: pygame.mixer.Sound
    game_over_fx: pygame.mixer.Sound


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self, screen):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        # draw button
        screen.blit(self.image, self.rect)
        return action


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y, image):
        super().__init__()
        self.image = pygame.transform.scale(image, (PlatformerConfig.tile_size, PlatformerConfig.tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (PlatformerConfig.tile_size, int(PlatformerConfig.tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (PlatformerConfig.tile_size // 2, PlatformerConfig.tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(image, (PlatformerConfig.tile_size, PlatformerConfig.tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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


class World:
    def __init__(self, world_data, language: Language, fx: LanguageFx, images: LanguageImages):
        # TODO: Add LanguageFx and LanguageImages
        self.coin_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()
        self.blob_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.tile_list = []
        self.world_data = world_data
        self.images = images
        self.fx = fx
        self.player = Player(100, PlatformerConfig.screen_height - 130, language)
        row_count = 0
        tile_size = PlatformerConfig.tile_size
        dirt_img = pygame.image.load(f'{language.value}/img/dirt.png')
        grass_img = pygame.image.load(f'{language.value}/img/grass.png')
        enemy_img = pygame.image.load(f'{language.value}/img/blob.png')
        for row in world_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 15, enemy_img)
                    self.blob_group.add(blob)
                if tile == 4:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0, self.images.platform)
                    self.platform_group.add(platform)
                if tile == 5:
                    platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1, self.images.platform)
                    self.platform_group.add(platform)
                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2), self.images.lava_img)
                    self.lava_group.add(lava)
                if tile == 7:
                    coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2),
                                self.images.coin_img)
                    self.coin_group.add(coin)
                if tile == 8:
                    exit_tile = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2), self.images.exit)
                    self.exit_group.add(exit_tile)
                col_count += 1
            row_count += 1

    def draw(self, screen):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
        self.platform_group.draw(screen)
        self.blob_group.draw(screen)
        self.coin_group.draw(screen)
        self.lava_group.draw(screen)
        self.exit_group.draw(screen)

    def handle_collisions(self) -> CollisionType:

        player = self.player

        # check for collision with enemies
        if pygame.sprite.spritecollide(player, self.blob_group, False):
            return CollisionType.BLOB

        # check for collision with lava
        if pygame.sprite.spritecollide(player, self.lava_group, False):
            return CollisionType.LAVA

        # check for collision with exit
        if pygame.sprite.spritecollide(player, self.exit_group, False):
            return CollisionType.EXIT

        # check for collision with boundary
        for tile in self.tile_list:
            # check for collision in x direction
            if tile[1].colliderect(player.rect.x + player.dx, player.rect.y, player.width,
                                   player.height):
                player.dx = 0
            # check for collision in y direction
            if tile[1].colliderect(player.rect.x, player.rect.y + player.dy, player.width,
                                   player.height):
                # check if below the ground i.e. jumping
                if player.vel_y < 0:
                    player.dy = tile[1].bottom - player.rect.top
                    player.vel_y = 0
                # check if above the ground i.e. falling
                elif player.vel_y >= 0:
                    player.dy = tile[1].top - player.rect.bottom
                    player.vel_y = 0
                    player.in_air = False

        # check for collision with platforms
        for platform in self.platform_group:
            # collision in the x direction
            if platform.rect.colliderect(player.rect.x + player.dx, player.rect.y, player.width, player.height):
                player.dx = 0
            # collision in the y direction
            if platform.rect.colliderect(player.rect.x, player.rect.y + player.dy, player.width, player.height):
                # check if below platform
                if abs((player.rect.top + player.dy) - platform.rect.bottom) < player.col_thresh:
                    player.vel_y = 0
                    player.dy = platform.rect.bottom - player.rect.top
                # check if above platform
                elif abs((player.rect.bottom + player.dy) - platform.rect.top) < player.col_thresh:
                    player.rect.bottom = platform.rect.top - 1
                    player.in_air = False
                    player.dy = 0
                # move sideways with the platform
                if platform.move_x != 0:
                    player.rect.x += platform.move_direction

        # update player coordinates
        player.rect.x += player.dx
        player.rect.y += player.dy
        if pygame.sprite.spritecollide(player, self.coin_group, True):
            return CollisionType.COIN
        return CollisionType.NONFATAL


class Platformer:
    """ Interface for different platformer languages. SHOULD NOT BE INSTANTIATED DIRECTLY"""

    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()
        pygame.display.set_caption('Omilia')
        # define game variables
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((PlatformerConfig.screen_width, PlatformerConfig.screen_height),
                                              pygame.RESIZABLE)
        self.level_state: LevelState = LevelState.START
        self.world: World | None = None
        self.fx = self.load_fx()
        self.images = self.load_images()
        self.buttons = self.create_buttons()
        self.platformer_state = PlatformerState.MAIN_MENU
        self.score = 0

    def draw_text(self, text, font, text_colour, x, y):
        img = font.render(text, True, text_colour)
        self.screen.blit(img, (x, y))

    def reset_world(self, level) -> World:
        pass

    def load_fx(self) -> LanguageFx:
        pass

    def load_images(self) -> LanguageImages:
        pass

    def create_buttons(self) -> Buttons:
        pass

    def run(self):
        run_window = True
        current_level = 0
        while run_window:
            self.clock.tick(PlatformerConfig.fps)

            # if self.platformer_state == PlatformerState.MAIN_MENU:
            #     if self.buttons.exit_button.draw(self.screen):
            #         run_window = False
            #     if self.buttons.start_button.draw(self.screen):
            #         self.platformer_state = PlatformerState.PLAYING_LEVEL
            if self.platformer_state == PlatformerState.MAIN_MENU:
                self.fx.martyspeech_fx.play()
                self.platformer_state = PlatformerState.PLAYING_LEVEL

            if self.platformer_state == PlatformerState.PLAYING_LEVEL:
                self.platformer_state = self.play_level(current_level)

            if self.platformer_state == PlatformerState.QUESTION:
                self.platformer_state = self.play_question()
                current_level += 1
                # TODO: implement question

    def play_level(self, level):
        self.world = self.reset_world(level)
        level_time = 0
        self.level_state = LevelState.PLAYING
        platformer_state = PlatformerState.PLAYING_LEVEL
        while self.level_state == LevelState.PLAYING:
            self.screen.blit(self.images.bg_img, (0, 0))
            self.screen.blit(self.images.sun_img, (100, 100))
            self.clock.tick(PlatformerConfig.fps)
            self.world.draw(self.screen)
            self.screen.blit(self.world.player.image, self.world.player.rect)
            self.draw_text('X ' + str(self.score), PlatformerConfig.font_score, Colours.WHITE.value,
                           PlatformerConfig.tile_size - 10, 10)
            self.world.blob_group.update()
            self.world.platform_group.update()
            level_time += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.level_state = LevelState.GAME_OVER
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            self.handle_keypress()
            collision = self.world.handle_collisions()
            match collision:
                case CollisionType.BLOB:
                    self.fx.game_over_fx.play()
                    self.level_state = LevelState.GAME_OVER
                    self.score = 0
                case CollisionType.LAVA:
                    self.fx.game_over_fx.play()
                    self.level_state = LevelState.GAME_OVER
                    self.score = 0
                case CollisionType.EXIT:
                    self.level_state = LevelState.EXIT
                    platformer_state = PlatformerState.QUESTION
                case CollisionType.COIN:
                    self.fx.coin_fx.play()
                    self.score += 1
                case CollisionType.NONFATAL:
                    pass
            pygame.display.update()
        return platformer_state

    def play_question(self) -> PlatformerState:
        return PlatformerState.PLAYING_LEVEL
        pass

    # TODO: implement question

    def handle_keypress(self):
        self.world.player.reset_movement()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.world.player.can_jump():
            self.fx.jump_fx.play()
            self.world.player.jump()
        if not keys[pygame.K_SPACE]:
            self.world.player.jumped = False
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.world.player.left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.world.player.right()
        if (keys[pygame.K_LEFT] is False or keys[pygame.K_a]) and (keys[pygame.K_RIGHT] is False or keys[pygame.K_d]):
            self.world.player.reset_counter()
        self.world.player.animate()


class Player:
    def __init__(self, x, y, langauge: Language):
        self.language = langauge
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'{self.language.value}/img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load(f'{self.language.value}/img/ghost.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
        self.dx = 0
        self.walk_cooldown = 5
        self.col_thresh = 20
        self.dy = 0

    def reset(self, x, y):
        self.__init__(x, y, self.language)

    def reset_movement(self):
        self.dx = 0
        self.dy = 0

    def reset_counter(self):
        self.counter = 0
        self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        if self.direction == -1:
            self.image = self.images_left[self.index]

    def can_jump(self):
        return not self.jumped and not self.in_air

    def jump(self):
        if self.can_jump():
            self.vel_y = -15
            self.jumped = True

    def left(self):
        self.dx -= 5
        self.counter += 1
        self.direction = -1

    def right(self):
        self.dx += 5
        self.counter += 1
        self.direction = 1

    def animate(self):
        if self.counter > self.walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        self.dy += self.vel_y
        self.in_air = True
