import Pigeon2d as p
game = p.Game()
sprite = p.resize_image(p.spritesheet("assets/Pigeons/Original Diminsions/Pigeon Sprite Sheet.png").image_at((0, 16, 16, 16)))
player = p.Sprite(game, sprite, pos=(20, 20))
while True:
    game.update()
