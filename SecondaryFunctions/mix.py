import random
import os
import sys
sys.path.insert(0, "../cubik")
from cubik import *
import re
from random import randint

class Mix():
    def runMix(self, lst_moves, cube):
        """Run mix move by move"""
        for move in lst_moves:
            if move == "F":
                cube.move_front()
            elif move == "F'":
                cube.move_front_counter()
            elif move == "F2":
                cube.move_f2()
            elif move == "B":
                cube.move_back()
            elif move == "B'":
                cube.move_back_counter()
            elif move == "B2":
                cube.move_b2()
            elif move == "D":
                cube.move_down()
            elif move == "D'":
                cube.move_down_counter()
            elif move == "D2":
                cube.move_d2()
            elif move == "L":
                cube.move_left()
            elif move == "L'":
                cube.move_left_counter()
            elif move == "L2":
                cube.move_l2()
            elif move == "R":
                cube.move_right()
            elif move == "R'":
                cube.move_right_counter()
            elif move == "R2":
                cube.move_r2()
            elif move == "U":
                cube.move_up()
            elif move == "U'":
                cube.move_up_counter()
            elif move == "U2":
                cube.move_u2()
        return cube

    def valid(self, lst):
        for move in lst:
            if len(move) > 2:
                return False
            tmp = re.sub(r"[FRLUBD'2]", "", move)
            if len(tmp) > 0:
                return False
            check = re.compile(r"(F|R|L|U|B|D)('|2)") if len(move) == 2 else re.compile(r"(F|R|L|U|B|D)")
            if check.search(move) is None:
                return False
        return True

    def create(self):
        moves = ["F", "R", "L", "U", "B", "D", "F'", "R'", "L'", "U'", "B'", "D'", "F2", "R2", "L2", "U2", "B2", "D2"]
        lst = []
        i = 0
        scramble_len = randint(15,35)
        while i <= scramble_len:
            lst.append(moves[randint(0,17)])
            i += 1
        print("A random scramble of {} moves is generated, here it is:".format(len(lst)))
        for move in lst:
            print(move, end=' ')
        print()
        return lst
