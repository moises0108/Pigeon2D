<center><img src="Pigeon2d.png"></center>

# 鴿子2D

[![Version](https://img.shields.io/pypi/v/Pigeon2D)](https://pypi.org/project/Pigeon2D/)![Lines](https://img.shields.io/tokei/lines/github/desvasicek/Pigeon2D)![Files](https://img.shields.io/github/directory-file-count/desvasicek/Pigeon2D)![Last Commit](https://img.shields.io/github/last-commit/desvasicek/Pigeon2D)![Size](https://img.shields.io/github/languages/code-size/desvasicek/Pigeon2D)[![Hits](https://hits.sh/github.com/desvasicek/Pigeon2D/hits.svg)](https://github.com/desvasicek/Pigeon2D)

![Current](https://img.shields.io/badge/currently-in%20progress-red)[![Help wanted](https://img.shields.io/badge/-help--wanted-yellow)](https://github.com/desvasicek/Pigeon2D/pulls)

pygame的python遊戲引擎。

## 如何

### 句法

```python
# Game

Game(title, GRAVITY, FRICTION, ACCELERATION)
.update(fill)

# Sprite (pygame.sprite.Sprite)

Sprite(surface, image, pos, playerobj)
.move()
.draw()

# spritesheet (object)

spritesheet(filename)
.image_at(rectangle, colorkey)
.images_at(rects, colorkey)
.load_strip(rect, image_count, colorkey)

# SpriteStripAnim (object)

SpriteStripAnim(filename, rect, count, colorkey, loop, frames)
.iter()
.next()

```

### 教程

```python
# import module
import Pigeon2d as p
# initialize Game() object
game = p.Game()
# load image
image = p.resize_image(p.spritesheet("assets/Pigeons/Original Diminsions/Pigeon Sprite Sheet.png").image_at((0, 16, 16, 16)))
# initialize player Sprite() object
player = p.Sprite(game, image, pos=(20, 20))
# game loop
while True:
    game.update()

```

    pygame 1.9.6
    Hello from the pygame community. https://www.pygame.org/contribute.html

## 用於教程

### 資產

資產由 Pop Shop Packs 在 itch.io 上製作（<https://pop-shop-packs.itch.io/>)

### 示例代碼

@desvasicek（我）的示例代碼儘管可以隨意使用。

### 代碼

@desvasicek 編寫的代碼，並在 MIT 許可證下註冊（[在這裡閱讀](https://github.com/desvasicek/Pigeon2D/blob/main/LICENSE)）。
pygame 處理 Spritesheet (<https://www.pygame.org/wiki/Spritesheet>) 由@desvasicek 改編為 Python 3.9.2
