import random

import arcade

import Game


SEED = random.random()

TECTONIC_PLATES = 7
# Amount of plates into which we divide the map.

SUBMERGENCE = 0.5
# Which part of tectonic plates should be oceanic.

N = 3
# You can change this constant.
# It determines an amount of cells on your map (2**N cells on one side).
# Remember that quantity is proportional to the square of edge length.
# Huge values can cause lags and Memory Error (N>3)


def main():
    game = Game.Game(n=N, tectonic_plates_count=TECTONIC_PLATES, submergence=SUBMERGENCE, seed=SEED)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
