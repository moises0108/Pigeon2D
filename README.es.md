<center><img src="Pigeon2d.png"></center>

# Paloma2D

[![Version](https://img.shields.io/pypi/v/Pigeon2D)](https://pypi.org/project/Pigeon2D/)![Lines](https://img.shields.io/tokei/lines/github/desvasicek/Pigeon2D)![Files](https://img.shields.io/github/directory-file-count/desvasicek/Pigeon2D)![Last Commit](https://img.shields.io/github/last-commit/desvasicek/Pigeon2D)![Size](https://img.shields.io/github/languages/code-size/desvasicek/Pigeon2D)[![Hits](https://hits.sh/github.com/desvasicek/Pigeon2D/hits.svg)](https://github.com/desvasicek/Pigeon2D)

![Current](https://img.shields.io/badge/currently-in%20progress-red)[![Help wanted](https://img.shields.io/badge/-help--wanted-yellow)](https://github.com/desvasicek/Pigeon2D/pulls)

Un motor de juego de Python para pygame.

<!--STARTS_HERE_QUOTE_README-->

<!--ENDS_HERE_QUOTE_README-->

## Cómo

### Sintaxis

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

### Tutorial

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

## Usado en Tutorial

### Activos

Pop Shop Packs creó activos en itch.io (<https://pop-shop-packs.itch.io/>)

### Código de ejemplo

Sin embargo, el código de ejemplo de @desvasicek (yo) no dude en usarlo.

### Código

Código por @desvasicek y está registrado bajo la Licencia MIT ([Léalo aquí](https://github.com/desvasicek/Pigeon2D/blob/main/LICENSE)).
Manejo de hojas de sprites por pygame (<https://www.pygame.org/wiki/Spritesheet>) adaptado a Python 3.9.2 por @desvasicek
