# Pigeon2D
![Version](https://img.shields.io/pypi/v/Pigeon2D)
![Lines](https://img.shields.io/tokei/lines/github/desvasicek/Pigeon2D)
![Files](https://img.shields.io/github/directory-file-count/desvasicek/Pigeon2D)
![Last Commit](https://img.shields.io/github/last-commit/desvasicek/Pigeon2D)
![Size](https://img.shields.io/github/languages/code-size/desvasicek/Pigeon2D)

![Current](https://img.shields.io/badge/currently-in%20progress-red)

A python game engine for pygame.

[![Help wanted](https://img.shields.io/github/labels/desvasicek/Pigeon2D/help-wanted)](https://github.com/desvasicek/Pigeon2D/pulls)
## How To

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
```
pygame 1.9.6
Hello from the pygame community. https://www.pygame.org/contribute.html
```

## Used in Tutorial
### Assets
Assets were made on itch.io by Pop Shop Packs (https://pop-shop-packs.itch.io/)
### Example Code
Example code by @desvasicek (me) feel free to use it though.
### Code
Code by @desvasicek and is registered under the MIT License ([Read it here](https://github.com/desvasicek/Pigeon2D/blob/main/LICENSE)).
Spritesheet handling by pygame (https://www.pygame.org/wiki/Spritesheet) adapted to Python 3.9.2 by @desvasicek
