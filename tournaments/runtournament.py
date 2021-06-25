import shutil
import datetime
import os
import shlex
import sys
from rtpt import RTPT
import argparse
from subprocess import Popen, PIPE
from cutechesstournament import CutechessTournament, Engine
from tournament_config import *


# ----- ARGS ------- #
def parse_args(cmd_args: list):
    parser = argparse.ArgumentParser(description='Run cutechess tournament')
    parser.add_argument("-gpu", type=int, default=1,
                        help="GPU to use for tournament. (default: 1)")
    parser.add_argument("--local", default=False, action="store_true",
                        help="If we use local or server mode. (default: False)")

    return parser.parse_args(cmd_args)


args = parse_args(sys.argv[1:])

# ----- RTPT ------- #

rtpt = RTPT(name_initials='MG',
                 experiment_name=f'MultiAraTournaments',
                 max_iterations=10)
rtpt.start()

# ----- Parameter ------- #

if args.local:
    BOOKS_PATH = f'/home/maxalex/Git/books/'
    EXPORT_DIR = f'/home/maxalex/Documents/Cutechess-Tournaments/'
    CLI_PATH = f'/home/maxalex/Git/cutechess/projects/cli/cutechess-cli'
else:
    BOOKS_PATH = f'/data/RL/books/'
    EXPORT_DIR = f'/data/RL/tournaments/'
    CLI_PATH = f'/data/RL/cutechess-cli/cutechess-cli'


# variants = ['antichess', 'atomic', 'crazyhouse', 'kingofthehill', 'racingkings', 'horde', '3check', 'chess960']
# modes = [FAST_MODE, LONG_MODE]
# _engines = [[ARA_ENGINE_UP20, ARA_ENGINE_UP30]]

setup = [
    ['3check', [ARA_ENGINE_SL7, ARA_ENGINE_UP10], FAST_MODE],
    ['3check', [ARA_ENGINE_SL7, ARA_ENGINE_UP10], LONG_MODE],
    ['3check', [ARA_ENGINE_UP10, ARA_ENGINE_UP20], FAST_MODE],
    ['3check', [ARA_ENGINE_UP10, ARA_ENGINE_UP20], LONG_MODE],
    ['crazyhouse', [ARA_ENGINE_SL7, ARA_ENGINE_UP10], FAST_MODE],
    ['crazyhouse', [ARA_ENGINE_SL7, ARA_ENGINE_UP10], LONG_MODE],
    ['crazyhouse', [ARA_ENGINE_UP10, ARA_ENGINE_UP20], FAST_MODE],
    ['crazyhouse', [ARA_ENGINE_UP10, ARA_ENGINE_UP20], LONG_MODE],
    ['atomic', [ARA_ENGINE_SL7, ARA_ENGINE_UP10], FAST_MODE],
    ['atomic', [ARA_ENGINE_SL7, ARA_ENGINE_UP10], LONG_MODE],
]


for s in setup:

    # ------ Select ------- #

    event_name = None
    uci_variant = s[0]
    engines = s[1]
    mode = s[2]

    # ------ Execute ------- #

    for engine in engines:
        # insert gpu-id dynamically
        if not args.local and engine.binary_name == 'MultiAra':
            engine.cli_options = [['Threads', '3'],
                                  ['First_Device_ID', f'{args.gpu}'],
                                  ['Last_Device_ID', f'{args.gpu}']]
        engine.initialize(uci_variant)

    book = None
    if uci_variant in BOOKS.keys():
        book = BOOKS_PATH + BOOKS[uci_variant]
    ct = CutechessTournament(CLI_PATH, EXPORT_DIR, uci_variant, engines, mode, book, event_name, args.local)
    ct.run()

    rtpt.step()
