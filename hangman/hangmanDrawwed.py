# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:05:01 2020

@author: CesarGS
"""


def figure(turns):
    if turns == 9:
        print("9 turns left")
        print("  --------  ")
    if turns == 8:
        print("8 turns left")
        print("  --------  ")
        print("     O      ")
    if turns == 7:
        print("7 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
    if turns == 6:
        print("6 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    /       ")
    if turns == 5:
        print("5 turns left")
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    / \     ")
    if turns == 4:
        print("4 turns left")
        print("  --------  ")
        print("   \ O      ")
        print("     |      ")
        print("    / \     ")
    if turns == 3:
        print("3 turns left")
        print("  --------  ")
        print("   \ O /    ")
        print("     |      ")
        print("    / \     ")
    if turns == 2:
        print("2 turns left")
        print("  --------  ")
        print("   \ O /|   ")
        print("     |      ")
        print("    / \     ")
    if turns == 1:
        print("1 turns left")
        print("Last breaths counting, Take care!")
        print("  --------  ")
        print("   \ O_|/   ")
        print("     |      ")
        print("    / \     ")
    if turns == 0:
        print("You loose")
        print("You let a kind man die")
        print("  --------  ")
        print("     O_|    ")
        print("    /|\      ")
        print("    / \     ")
        