import argparse
from copy import deepcopy
import sys

def arg_parse():
    """Parsing arguments for mix"""
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mix", required=False, help="cube shuffle")
    parser.add_argument("-e", "--explain", action="store_true", help="Get more explanation about steps")
    options = parser.parse_args()
    return options

def check_back_state(cubFace, color):
	if cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color and cubFace[1][0] == color and cubFace[2][1] == color:
		return (4, 0)
	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (3, 0)
	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[2][1] == color:
		return (3, 1)
	elif cubFace[2][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (2, 0)
	elif cubFace[1][0] == color and cubFace[1][1] == color and cubFace[2][1] == color:
		return (2, 1)
	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][0] == color:
		return (2, 2)
	elif cubFace[0][1] == color and cubFace[1][1] == color and cubFace[1][2] == color:
		return (2, 3)
	elif cubFace[1][1] == color:
		return (1, 0)
	return False, False

def append_list(lst_moves, to_add):
    """Append a list after a first one"""
    for elem in to_add:
        lst_moves.append(elem)
    return lst_moves

def optimize_solution(lst_moves):
    index = 0
    while index < len(lst_moves):
        if lst_moves[index:index+4] == ["D","D","D","D"]:
            for i in range(4):
                lst_moves.pop(index)
            #lst_moves.pop(index)
            #lst_moves.pop(index)
            #lst_moves.pop(index)
            #lst_moves.pop(index)
        elif lst_moves[index:index+3] == ["D","D","D"]:
            lst_moves[index] = "D'"
            lst_moves.pop(index + 1)
            lst_moves.pop(index + 1)
        elif lst_moves[index:index+2] == ["D","D"]:
            lst_moves[index] = "D2"
            lst_moves.pop(index + 1)
        index += 1
    return lst_moves
