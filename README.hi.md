<center><img src="Pigeon2d.png"></center>

# कबूतर2डी

[![Version](https://img.shields.io/pypi/v/Pigeon2D)](https://pypi.org/project/Pigeon2D/)![Lines](https://img.shields.io/tokei/lines/github/desvasicek/Pigeon2D)![Files](https://img.shields.io/github/directory-file-count/desvasicek/Pigeon2D)![Last Commit](https://img.shields.io/github/last-commit/desvasicek/Pigeon2D)![Size](https://img.shields.io/github/languages/code-size/desvasicek/Pigeon2D)[![Hits](https://hits.sh/github.com/desvasicek/Pigeon2D/hits.svg)](https://github.com/desvasicek/Pigeon2D)

![Current](https://img.shields.io/badge/currently-in%20progress-red)[![Help wanted](https://img.shields.io/badge/-help--wanted-yellow)](https://github.com/desvasicek/Pigeon2D/pulls)

पायगम के लिए एक अजगर खेल इंजन।

## कैसे

### वाक्य - विन्यास

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

### ट्यूटोरियल

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

## ट्यूटोरियल में प्रयुक्त

### संपत्ति

पॉप शॉप पैक्स द्वारा itch.io पर एसेट बनाए गए थे ([हत्तपः://पॉप-शॉप-पैक्स.इतच्.ीो/](https://pop-shop-packs.itch.io/))

### उदाहरण कोड

@desvasicek (me) द्वारा उदाहरण कोड हालांकि इसका उपयोग करने के लिए स्वतंत्र महसूस करें।

### कोड

@desvasicek द्वारा कोड और एमआईटी लाइसेंस के तहत पंजीकृत है ([इसे यहां पढ़ें](https://github.com/desvasicek/Pigeon2D/blob/main/LICENSE))
pygame द्वारा स्प्राइटशीट हैंडलिंग ([हत्तपः://ववव.पैगामे.ऑर्ग/विकी/स्प्रिटेशित](https://www.pygame.org/wiki/Spritesheet)) @desvasicek . द्वारा पायथन 3.9.2 के लिए अनुकूलित
