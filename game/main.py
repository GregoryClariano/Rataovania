import pygame
from game.core.game_manage import GameManage


def main():

    pygame.init()

    game = GameManage()

    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
