from difficulty import Difficulty
from game_manager import GameManager
import pygame
import argparse

def parse_difficulty(difficulty: str) -> Difficulty:
    if difficulty == "easy":
        return Difficulty.EASY
    elif difficulty == "medium":
        return Difficulty.MEDIUM
    elif difficulty == "hard":
        return Difficulty.HARD
    else:
        return Difficulty.EASY

parser = argparse.ArgumentParser(description="Run the game with a specified difficulty")
parser.add_argument('-d', '--difficulty', type=str, choices=['easy', 'medium', 'hard'], help="The difficulty of the game")
args = parser.parse_args()

difficulty = parse_difficulty(args.difficulty)
pygame.init()
game_manager = GameManager(difficulty)
game_manager.run_game()
