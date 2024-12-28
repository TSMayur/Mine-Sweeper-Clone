import sys
from game import Game
import tkinter
def main():
    size =(10,10)
    prob = 0.1

    g = Game(size, prob)
    g.run()

if __name__ == '__main__':
    main()

    