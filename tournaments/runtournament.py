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
from datetime import datetime

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
    WORKING_DIR = f'/home/maxalex/Documents/Cutechess-Tournaments/'
else:
    BOOKS_PATH = f'/data/RL/books/'
    EXPORT_DIR = f'/data/RL/tournaments/'
    CLI_PATH = f'/data/RL/cutechess-cli/cutechess-cli'
    WORKING_DIR = f'/data/RL/' # only used for logs atm


setup = {
    0: [
        ['Proxy Line for local runs']
    ],
    1: [
        ['atomic', [ARA_ENGINE_UP30, FAIRY_ENGINE_NNUE], FAST_MODE],
        ['atomic', [ARA_ENGINE_UP30, FAIRY_ENGINE_NNUE], LONG_MODE],
    ],
    4: [
        ['kingofthehill', [ARA_ENGINE_UP60_FROM0_EXTSCHED, ARA_ENGINE_UP70_FROM0_EXTSCHED], FAST_MODE],
        ['kingofthehill', [ARA_ENGINE_UP60_FROM0_EXTSCHED, ARA_ENGINE_UP70_FROM0_EXTSCHED], LONG_MODE],
        ['kingofthehill', [ARA_ENGINE_UP70_FROM0_EXTSCHED, ARA_ENGINE_SL7], LONG_MODE],
    ],
    3: [
        ['kingofthehill', [ARA_ENGINE_UP60_NOEXPLOINC, FAIRY_ENGINE_NNUE], FAST_MODE],
        ['kingofthehill', [ARA_ENGINE_UP60_NOEXPLOINC, FAIRY_ENGINE_NNUE], LONG_MODE],
    ],
    2: [
        ['3check', [ARA_ENGINE_UP40, FAIRY_ENGINE_NNUE], FAST_MODE],
        ['3check', [ARA_ENGINE_UP40, FAIRY_ENGINE_NNUE], LONG_MODE],
    ],
    5: [
        ['kingofthehill', [ARA_ENGINE_UP70_FROM0_EXTSCHED, FAIRY_ENGINE], FAST_MODE],
        ['kingofthehill', [ARA_ENGINE_UP70_FROM0_EXTSCHED, FAIRY_ENGINE], LONG_MODE],
        ['kingofthehill', [ARA_ENGINE_UP70_FROM0_EXTSCHED, ARA_ENGINE_SL7], FAST_MODE],
    ],
    6: [
        ['racingkings', [ARA_ENGINE_UP10, FAIRY_ENGINE_NNUE], FAST_MODE],
        ['racingkings', [ARA_ENGINE_UP10, FAIRY_ENGINE_NNUE], LONG_MODE],
    ]
}

for i, s in enumerate(setup[args.gpu]):

    # ------ Select ------- #
    if args.local:
        event_name = None
        uci_variant = 'kingofthehill'
        engines = [ARA_ENGINE_UP10_LOCAL, FAIRY_ENGINE_NNUE_LOCAL]
        mode = RAPID_MODE
    else:
        event_name = None
        uci_variant = s[0]
        engines = s[1]
        mode = s[2]

    # ------ Log ------- #

    engine_str = engines[0].name
    for e in engines[1:]:
        engine_str += ' vs. ' + e.name
    with open(f'{WORKING_DIR}/gpus.log', 'a+') as f:
        f.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}: '
                f'GPU {args.gpu:2}: {uci_variant} - {engine_str} - {mode.name} [{i+1}/{len(setup[args.gpu])}]\n')

    # ------ Execute ------- #

    for engine in engines:
        # insert gpu-id dynamically
        if not args.local and (engine.binary_name == 'MultiAra' or engine.binary_name == 'CrazyAra'):
            engine.cli_options = [['Threads', '3'],
                                  ['First_Device_ID', f'{args.gpu}'],
                                  ['Last_Device_ID', f'{args.gpu}']]
        elif not args.local and engine.name == 'FairyStockfishNNUE':
            engine.cli_options = [['Threads', '4'],
                                  ['Hash', '2048'],
                                  ['Use NNUE', 'true'],
                                  ['EvalFile', f'{FAIRY_NNUE[uci_variant]}']]
        engine.initialize(uci_variant)

    book = None
    if uci_variant in BOOKS.keys():
        book = BOOKS_PATH + BOOKS[uci_variant]
    ct = CutechessTournament(CLI_PATH, EXPORT_DIR, uci_variant, engines, mode, book, event_name, args.local)
    ct.run()

    rtpt.step()
