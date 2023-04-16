import random
from typing import Tuple

import pygame


class DiceRoll:
    __roll: Tuple[int, int]
    __total: int

    def __init__(self, roll: Tuple[int, int]):
        self.__roll = roll
        self.__total = roll[0] + roll[1]

    def get(self) -> Tuple[int, int]:
        return self.__roll

    def total(self) -> int:
        return self.__total

class Dice:
    __current_roll: DiceRoll
    __dice_faces: dict
    def roll(self):
        self.__current_roll = DiceRoll((random.randint(1, 6), random.randint(1, 6)))
        self.__load_dice_faces()

    def __load_dice_faces(self):
        self.__dice_faces = {
            1: [(50, 50)],
            2: [(25, 25), (75, 75)],
            3: [(25, 25), (50, 50), (75, 75)],
            4: [(25, 25), (75, 25), (25, 75), (75, 75)],
            5: [(25, 25), (75, 25), (50, 50), (25, 75), (75, 75)],
            6: [(25, 25), (75, 25), (25, 50), (75, 50), (25, 75), (75, 75)]
        }

    def roll(self):
        self.__current_roll = DiceRoll((random.randint(1, 6), random.randint(1, 6)))

    def current(self) -> DiceRoll:
        return self.__current_roll

    def draw(self, screen, x, y):
        face = self.__current_roll.total()
        dot_positions = self.__dice_faces.get(face, [])
        for dot_x, dot_y in dot_positions:
            dot_rect = pygame.Rect(x + dot_x - 5, y + dot_y - 5, 10, 10)
            pygame.draw.ellipse(screen, (0, 0, 0), dot_rect)