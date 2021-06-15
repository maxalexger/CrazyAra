import dataclasses

import sys
import shutil
import time
import subprocess
import shlex
import os
import datetime
from dataclasses import dataclass
import json

from subprocess import Popen, PIPE
from typing import List


@dataclass
class Engine:
    name: str
    shortname: str
    version: str
    binary_name: str
    binary_dir: str
    cli_options: List[List[str]] = None

    def initialize(self, uci_variant: str) -> None:
        if self.cli_options:
            for option in self.cli_options:
                assert len(option) == 2, f'{self.name}: Please provide List[List[str, str]] as cli_options param'

        print(f'\n----- Initializing {self.name} binary------\n')
        os.chdir(self.binary_dir)
        proc = Popen([os.path.join(self.binary_dir, self.binary_name)], stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
        proc.stdin.write(f'setoption name uci_variant value {uci_variant}\n'.encode())
        proc.stdin.flush()
        if self.cli_options:
            for option in self.cli_options:
                proc.stdin.write(f'setoption name {option[0]} value {option[1]}\n'.encode())
        proc.stdin.flush()
        proc.stdin.write(b'isready\n')
        proc.stdin.flush()
        while True:
            line = proc.stdout.readline()
            if line == b'':
                error = proc.stderr.readline()
                if error != b'':
                    while error != b'':
                        print(error.decode().rstrip(f'\n'))
                        error = proc.stderr.readline()
                    break

            line = line.decode().rstrip(f'\n')
            print(line)
            if line == 'readyok':
                break

        proc.kill()
        time.sleep(1)


@dataclass
class TournamentMode:
    name: str
    time_control: str = None
    fixed_movetime_sec: float = None


class CutechessTournament:
    def __init__(self, cli_path: str, export_dir: str, uci_variant: str, engines: List[Engine],
                 mode: TournamentMode, games: int, rounds: int, opening_book_path: str = None, event_name: str = None):
        self.cli_path = cli_path
        self.export_dir = export_dir
        self.uci_variant = uci_variant
        self.engines = engines
        self.mode = mode
        self.games = games
        self.rounds = rounds
        self.opening_book_path = opening_book_path
        self.event_name = event_name

        self.tournament_name = None
        self.tournament_dir = None
        self.cli_command = None
        self.results_file_name = None
        self.statistics = None

        for engine in engines:
            if engine.cli_options:
                for option in engine.cli_options:
                    assert len(option) == 2, f'{engine.name}: Please provide List[List[str, str]] as cli_options param'

        assert (mode.fixed_movetime_sec is None) ^ (mode.time_control is None), \
            f'Do not use time control & fixed move time together!'

    def run(self, testing=False):
        print(f'\n----- Setup ------\n')
        self._create_tournament_name()
        self._create_tournament_dir(testing)
        self._create_cutechess_cmd()
        self.results_file_name = os.path.join(self.tournament_dir, f'{self.tournament_name}_results.txt')

        print(f'\n----- Tournament Information ------\n')
        print(f'* {self.rounds} rounds with {self.games} games')
        print(f'* Mode = {self.mode.name}')
        print(f'* Using opening book') if self.opening_book_path else print(f'* Using NO opening book')

        print(f'\n----- Running Tournament ------\n')
        self._executing_cli_command()

        print(f'\n----- Statistics & after match tasks -----\n')
        self._getting_statistics()
        self._export_to_json()

    def _create_tournament_name(self):
        print(f'* Creating tournament name')
        tournament_name = self.uci_variant
        tournament_name += f'-{datetime.datetime.today().strftime("%Y%m%d-%H%M")}'
        engines_str = f'{self.engines[0].shortname}'
        for engine in self.engines[1:]:
            engines_str += f'-{engine.shortname}'
        tournament_name += f'-{engines_str}'
        tournament_name += f'-{self.rounds}x{self.games}'
        tournament_name += f'-{self.mode.name}'

        if not self.event_name:
            self.event_name = f'{engines_str}-{self.mode.name}'
        self.tournament_name = tournament_name

    def _create_tournament_dir(self, debug):
        print(f'* Creating tournament directory')
        self.tournament_dir = os.path.join(self.export_dir, self.tournament_name)
        if os.path.exists(self.tournament_dir):
            if debug:  # Overwrite the folder
                pass
            else:
                raise FileExistsError('The tournament folder already exists')
        else:
            os.mkdir(self.tournament_dir)

    def _create_cutechess_cmd(self):
        print(f'* Creating cutechess command')
        cc_cmd = f'{self.cli_path} -variant {self.uci_variant} -event {self.event_name} ' \
                 f'-rounds {self.rounds}  -games {self.games} -wait 1000 ' \
                 f'-pgnout {self.tournament_name}.pgn -epdout {self.tournament_name}.epd ' \
                 f'-site TU-Darmstadt -recover -resultformat wide2 ' \
                 f'-draw movenumber=40 movecount=5 score=20 ' \
                 f'-resign movecount=5 score=900 twosided=true '
        if self.opening_book_path:
            cc_cmd += f'-openings file={self.opening_book_path} format=epd order=sequential plies=5 -repeat '
        for engine in self.engines:
            cc_cmd += f'-engine name={engine.name} dir={engine.binary_dir} cmd={engine.binary_name} '
            if engine.cli_options:
                options = engine.cli_options
                assert type(options) == list, f'{engine.name}: Please provide List[List[str, str]] as options parameter'
                for option in options:
                    key = option[0].strip().replace(f' ', f'\\ ')
                    cc_cmd += f'option.{key}={option[1].strip()} '

        cc_cmd += f'-each proto=uci '
        if self.mode.time_control:
            cc_cmd += f'tc={self.mode.time_control} '
        if self.mode.fixed_movetime_sec:
            cc_cmd += f'st={self.mode.fixed_movetime_sec} '

        # Write cutechess command to file
        print(f'* Writing cutechess command to file')
        cmd_file = open(os.path.join(self.tournament_dir, f'{self.tournament_name}_cli_cmd.txt'), 'w')
        cmd_file.write(cc_cmd)
        cmd_file.close()

        self.cli_command = cc_cmd

    def _executing_cli_command(self, ) -> None:
        assert self.tournament_dir is not None and self.tournament_name is not None and self.cli_command is not None
        os.chdir(self.tournament_dir)
        results_file = open(self.results_file_name, 'w')
        proc = Popen(shlex.split(self.cli_command), stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=False)
        proc.stdin.flush()

        while True:
            line = proc.stdout.readline()
            if line == b'':
                error = proc.stderr.readline()
                if error != b'':
                    while error != b'':
                        print(error.decode().rstrip(f'\n'))
                        error = proc.stderr.readline()
                    break
            line = line.decode()
            results_file.write(line)
            print(line.rstrip(f'\n'))
            if line == 'Finished match\n':
                break

        proc.kill()
        results_file.close()
        time.sleep(1)

    def _getting_statistics(self) -> None:
        print(f'* Getting statistics')
        results_file = open(self.results_file_name)
        lines = results_file.readlines()
        idx = None
        for i, l in enumerate(reversed(lines)):
            if l.startswith('Score of '):
                idx = len(lines) - i - 1
        lines = lines[idx:-1]

        stats = {}
        for line in lines:
            if line.startswith('Score of '):
                idx = line.index('vs')
                idx2 = line.index(':')
                idx3 = line.index('[')
                stats['engineA'] = line[9:idx-1]
                stats['engineB'] = line[idx+3:idx2]
                stats['win_lose_draw'] = list(map(int, line[idx2+1:idx3].split('-')))
            if 'playing White: ' in line:
                idx = line.index(':')
                idx2 = line.index('[')
                stats['playing_white'] = list(map(int, line[idx+1:idx2].split('-')))
            if 'playing Black: ' in line:
                idx = line.index(':')
                idx2 = line.index('[')
                stats['playing_black'] = list(map(int, line[idx+1:idx2].split('-')))
            if line.startswith('Elo difference'):
                line = line[line.index(':')+2:]
                stats['elo_diff'] = float(line[:line.index(' ')])  # can be '-inf', '+inf' or 'float'
                line = line[line.index('+/-')+4:]
                stats['elo_dev'] = float(line[:line.index(',')])  # can be 'nan' or 'float'
                line = line[line.index(':')+2:]
                stats['los'] = float(line[:line.index(' ')])
                line = line[line.index(':')+2:]
                stats['draw_ratio'] = float(line[:line.index(' ')])
        self.statistics = stats

    def _export_to_json(self):
        print(f'* Exporting to JSON')
        json_obj = {'engines': [dataclasses.asdict(x) for x in self.engines],
                    'uci_variant': self.uci_variant, 'mode': dataclasses.asdict(self.mode), 'games': self.games,
                    'rounds': self.rounds, 'event_name': self.event_name, 'cli_command': self.cli_command,
                    'statistics': self.statistics}
        if self.opening_book_path:
            json_obj['opening_book'] = os.path.basename(self.opening_book_path)

        with open(os.path.join(self.tournament_dir, f'{self.tournament_name}_stats.json'), 'w') as file:
            json.dump(json_obj, file)

    @staticmethod
    def exec_bash_command(upload_cmd: str):
        print(f'* Executing \'{upload_cmd}\' ... ', end='')
        subprocess.check_call(shlex.split(upload_cmd))
        print(f'Done!')




