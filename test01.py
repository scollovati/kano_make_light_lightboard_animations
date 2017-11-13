#!/usr/bin/env python
# This file needs to be prepended to tutorial files, for
# them to work

import os
import sys

from kano.utils import get_user_unsudoed, get_home_by_username
DIR_PATH = os.path.join(
    get_home_by_username(get_user_unsudoed()), 'make-light'
)

if __name__ == '__main__' and __package__ is None:
    if DIR_PATH != '/usr':
        sys.path.insert(1, DIR_PATH)

from make_light.boards.base.aliases import *
from time import *
import time
from datetime import datetime
import datetime
from random import *
import random
from math import *
import math
import os

debug = False
simulation = False
token = ''

if 'POWERUP_DEBUG' in os.environ:
    simulation = True
    debug = True
elif 'POWERUP_TEST' in os.environ:
    simulation = True
elif 'POWERUP_MAKE' in os.environ:
    device = os.environ['POWERUP_MAKE']

if 'API_TOKEN' in os.environ:
    token = os.environ['API_TOKEN']

if simulation:
    from make_light.boards.available_boards.lightboard.simulation_board import \
        KanoLightBoard
    board = KanoLightBoard(debug=debug)
else:
    from make_light.boards.available_boards.lightboard.physical_board import \
        KanoLightBoardPhysical
    board = KanoLightBoardPhysical()

light = board
light.clear()
light.reset_exports()


while True:
	
	# animazione stupenda
	for x in range(WIDTH):
		for y in range(HEIGHT):
			light.on((x, y), x / 8.0)
	sleep(1)
	for x in range(WIDTH):
		for y in range(HEIGHT):
			light.off((x, y))
	sleep(1)
	#L
	light.on(B1,B2,B3,B4,B5,B6,C6,D6)
	#A
	light.on(F1,F2,F3,F4,F5,F6,G1,G3,G4,H1,H2,H3,H4,H5,H6,)
	#B
	light.on(B8,B9,B10,B11,B12,B13,B14,C8,C11,C14,D9,D10,D12,D13)
	#S
	light.on(F8,F9,F10,F11,F14,G8,G11,G14,H8,H11,H12,H13,H14)
	sleep(1)
	# Spengo LABS, non so come mai ma light.off(all) non e' affidabile
	light.clear()
	
	# E ora tocca a Pac-Man animato!!
	light.circle(12, E8, on)
	light.triangle(F8, H5, H11, off)
	sleep(.5)
	light.triangle(F8, H5, H11, on)
	sleep(.5)
	light.triangle(F8, H5, H11, off)
	sleep(.5)
	light.triangle(F8, H5, H11, on)
	sleep(.5)
	light.triangle(F8, H5, H11, off)
	sleep(.5)
	light.triangle(F8, H5, H11, on)
	sleep(.5)
	# Spengo Pac-Man
	light.clear()

# emoji
#light.on(D5)
#light.on(D6)
#light.on(D7)
#light.on(F5)
#light.on(F6)
#light.on(F7)
#light.on(C9,D10,E10,F10,G9)

# The blank line above is intentional, in case the user did not leave one at the
# end of their code. Add any relevant jobs below, to be run after user code.
