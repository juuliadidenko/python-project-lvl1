#!/usr/bin/env python3

from BRAIN_GAMES.engine import start_game
from BRAIN_GAMES.games import gcd


def main():
    start_game(gcd)


if __name__ == '__main__':
    main()
