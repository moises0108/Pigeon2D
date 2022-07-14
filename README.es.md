<center><img src="Pigeon2d.png"></center>

# Paloma2D

[![Version](https://img.shields.io/pypi/v/Pigeon2D)](https://pypi.org/project/Pigeon2D/)![Lines](https://img.shields.io/tokei/lines/github/desvasicek/Pigeon2D)![Files](https://img.shields.io/github/directory-file-count/desvasicek/Pigeon2D)![Last Commit](https://img.shields.io/github/last-commit/desvasicek/Pigeon2D)![Size](https://img.shields.io/github/languages/code-size/desvasicek/Pigeon2D)[![Hits](https://hits.sh/github.com/desvasicek/Pigeon2D/hits.svg)](https://github.com/desvasicek/Pigeon2D)[![Documentation Status](https://readthedocs.org/projects/pigeon2d/badge/?version=latest)](https://pigeon2d.readthedocs.io/en/latest/?badge=latest)

![Current](https://img.shields.io/badge/currently-in%20progress-red)[![Help wanted](https://img.shields.io/badge/-help--wanted-yellow)](https://github.com/desvasicek/Pigeon2D/pulls)

Un motor de juego de Python para pygame.

# Tabla de contenido

-   [paloma2d](#pigeon2d)
-   [Tabla de contenido](#table-of-contents)
    -   [Instalación](#installation)
        -   [Instalar](#install)
        -   [Mejora](#upgrade)
        -   [Instale la última versión de Pygame](#install-pygame-newest-version)
    -   [Cómo](#how-to)
        -   [Sintaxis](#syntax)
        -   [Tutorial](#tutorial)
    -   [Usado en Tutorial](#used-in-tutorial)
        -   [Activos](#assets)
        -   [Código de ejemplo](#example-code)
        -   [Código](#code)
-   [¡Gracias!](#thank-you)
    -   [Colaboradores](#collaborators)
    -   [Colaboradores](#contributors)
        -   [contribuyendo](#contributing)
    -   [Bichos 🐛️](#bugs)
    -   [Ideas 💡️](#ideas)

## Instalación

⚠️ Cuando instala el paquete usando pip, instala pygame 1.9.2, que se puede usar, pero se recomienda al menos pygame 2.1.2. ⚠️

### Instalar

```bash
$ pip install Pigeon2d
```

### Mejora

```bash
$ pip install -U Pigeon2d
```

### Instale la última versión de Pygame

```bash
$ pip install -U pygame
```

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

# ¡Gracias!

## Colaboradores

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

## Colaboradores

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

## Astrónomos

-   **@Global**
-   **@Moosems**
-   **@cergotv12**
-   **@merkfam**

### contribuyendo

Para comenzar,[**crear una solicitud de extracción**](https://github.com/desvasicek/Pigeon2D/pulls)o[**pídeme que te permita el acceso de colaboración**](https://github.com/desvasicek/Pigeon2D/discussions/2)

## Bichos 🐛️

Por favor[**crear un problema**](https://github.com/desvasicek/Pigeon2D/issues)

## Ideas 💡️

Por favor[**Comunicate conmigo**](https://github.com/desvasicek/Pigeon2D/discussions/1)
