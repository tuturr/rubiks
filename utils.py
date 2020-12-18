import argparse
import cube
import move
import sys

import visual as visu
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def arg_parse_options():
	"""Parsing arguments"""
	parser = argparse.ArgumentParser()
	parser.add_argument("mix", action="store", help="melange du cube")
	parser.add_argument("-v", "--visu", action="store_true", help="trigger visual")
	options = parser.parse_args()
	return options

def	select_move_function_to_call(move_id, cube):
	repeat = 1 #nombre de repetitions du move
	nb_letter = 0
	lst_valid_elems = ['F', 'L', 'R', 'B', 'U', 'D', "'"]
	#-----------------------------------------------------------------------------
	# Petit parsing de check de validite de la string mix
	for c in move_id:
		if c.isdigit() and c == "2":
			repeat = int(c)
		elif c not in lst_valid_elems:
			print("{} is not a valid mix char, please enter a valid mix.".format(c))
			sys.exit()
		elif c.isalpha():
			nb_letter += 1
		if nb_letter > 1:
			print("Error in mix parameter, please enter a valid mix.")
			sys.exit(0)
	if nb_letter == 0:
		print("Error in mix parameter, please_enter a valid mix.")
		sys.exit(0)
	#
	#-----------------------------------------------------------------------------
	if "F" in move_id:
		for loop in range(repeat):
			cube = move.move_F(cube, False) if "'" in move_id else move.move_F(cube, True)
	elif "R" in move_id:
		for loop in range(repeat):
			cube = move.move_R(cube, False) if "'" in move_id else move.move_R(cube, True)
	elif "B" in move_id:
		for loop in range(repeat):
			cube = move.move_B(cube, False) if "'" in move_id else move.move_B(cube, True)
	elif "L" in move_id:
		for loop in range(repeat):
			cube = move.move_L(cube, False) if "'" in move_id else move.move_L(cube, True)
	elif "U" in move_id:
		for loop in range(repeat):
			cube = move.move_U(cube, False) if "'" in move_id else move.move_U(cube, True)
	elif "D" in move_id:
		for loop in range(repeat):
			cube = move.move_D(cube, False) if "'" in move_id else move.move_D(cube, True)
	return cube.cube

def	shuffle_cube(mix, c):
	c.main_walk = mix
	moves = mix.split(' ')
	for i in range(len(moves)):
		c.cube = select_move_function_to_call(moves[i], c)
	return c
