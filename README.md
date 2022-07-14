<center><img src="Pigeon2d.png"></center>


# Pigeon2D
[![Version](https://img.shields.io/pypi/v/Pigeon2D)](https://pypi.org/project/Pigeon2D/)
![Lines](https://img.shields.io/tokei/lines/github/desvasicek/Pigeon2D)
![Files](https://img.shields.io/github/directory-file-count/desvasicek/Pigeon2D)
![Last Commit](https://img.shields.io/github/last-commit/desvasicek/Pigeon2D)
![Size](https://img.shields.io/github/languages/code-size/desvasicek/Pigeon2D)
[![Hits](https://hits.sh/github.com/desvasicek/Pigeon2D/hits.svg)](https://github.com/desvasicek/Pigeon2D)
[![Documentation Status](https://readthedocs.org/projects/pigeon2d/badge/?version=latest)](https://pigeon2d.readthedocs.io/en/latest/?badge=latest)

![Current](https://img.shields.io/badge/currently-in%20progress-red)
[![Help wanted](https://img.shields.io/badge/-help--wanted-yellow)](https://github.com/desvasicek/Pigeon2D/pulls)

A python game engine for pygame.

# Table of Contents

- [Pigeon2d](#pigeon2d)
- [Table of Contents](#table-of-contents)
	- [Installation](#installation)
		- [Install](#install)
		- [Upgrade](#upgrade)
		- [Install Pygame Newest Version](#install-pygame-newest-version)
	- [How To](#how-to)
		- [Syntax](#syntax)
		- [Tutorial](#tutorial)
	- [Used in Tutorial](#used-in-tutorial)
		- [Assets](#assets)
		- [Example Code](#example-code)
		- [Code](#code)
- [Thank You!](#thank-you)
	- [Collaborators](#collaborators)
	- [Contributors](#contributors)
		- [Contributing](#contributing)
	- [Bugs 🐛️](#bugs)
	- [Ideas 💡️](#ideas)

## Installation

⚠️ When you install the package using pip it installs pygame 1.9.2, which is usable, but pygame 2.1.2 at least is reccomended. ⚠️

### Install

```bash
$ pip install Pigeon2d
```

### Upgrade

```bash
$ pip install -U Pigeon2d
```

### Install Pygame Latest Version

```bash
$ pip install -U pygame
```

## How To

### Syntax

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

# Thank You!
## Collaborators

<!-- readme: collaborators -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/desvasicek">
            <img src="https://avatars.githubusercontent.com/u/84301435?v=4" width="100;" alt="desvasicek"/>
            <br />
            <sub><b>Des</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: collaborators -end -->

## Contributors

<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/desvasicek">
            <img src="https://avatars.githubusercontent.com/u/84301435?v=4" width="100;" alt="desvasicek"/>
            <br />
            <sub><b>Des</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->

## Stargazers

- __@ahribellah__
- __@Moosems__
- __@cergotv12__
- __@merkfam__

### Contributing

To start, [**create a pull request**](https://github.com/desvasicek/Pigeon2D/pulls) or [**ask me to allow you collaboration access**](https://github.com/desvasicek/Pigeon2D/discussions/2)

## Bugs 🐛️

Please [**create an issue**](https://github.com/desvasicek/Pigeon2D/issues)

## Ideas 💡️

Please [**communicate with me**](https://github.com/desvasicek/Pigeon2D/discussions/1)
