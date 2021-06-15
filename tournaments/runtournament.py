import shutil
import datetime
import os
import shlex
from subprocess import Popen, PIPE
from cutechesstournament import CutechessTournament, Engine
from tournament_config import *

# ----- Parameter ------- #
mode = 'local'

if mode == 'local':
    BOOKS_PATH = f'/home/maxalex/Git/books/'
    EXPORT_DIR = f'/home/maxalex/Documents/Cutechess-Tournaments/'
    CLI_PATH = f'/home/maxalex/Git/cutechess/projects/cli/cutechess-cli'
else:
    BOOKS_PATH = f'/data/RL/books/'
    EXPORT_DIR = f'/data/RL/results/'
    CLI_PATH = f'/data/RL/cutechess-cli/cutechess-cli'

# ------ Select ------- #
event_name = f'AtomicUp10From0vsUpdate10'
uci_variant = f'atomic'
games = 2
rounds = 1
engines = [ARA_ENGINE_UP10_LOCAL, ARA_ENGINE_UP10_FROM0_LOCAL]
mode = RAPID_MODE

# ------ Execute ------- #

for engine in engines:
    engine.initialize(uci_variant)
book = None
if uci_variant in BOOKS.keys():
    book = BOOKS_PATH + BOOKS[uci_variant]
ct = CutechessTournament(CLI_PATH, EXPORT_DIR, uci_variant, engines, mode, games, rounds, book, event_name)
ct.run(testing=False)

# ------- Uploading ------- #

upload_cmd = f'rclone copy {ct.tournament_dir} Google-Drive:/MA-Chess-Variants/Tournaments/{ct.tournament_name}'
ct.exec_bash_command(upload_cmd)