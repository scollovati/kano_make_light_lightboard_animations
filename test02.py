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
	sleep(.5)
	light.scroll('Labs & Camps')
	
# The blank line above is intentional, in case the user did not leave one at the
# end of their code. Add any relevant jobs below, to be run after user code.
