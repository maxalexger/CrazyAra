from cutechesstournament import Engine, TournamentMode

# =========== CONSTANTS ========== #

ARA_BINARY_NAME = f'MultiAra'
FAIRY_NNUE = {
    f'3check': f'3check-bba0afd355bd.nnue',
    f'atomic': f'atomic-6afe873e5ac3.nnue',
    f'kingofthehill': f'kingofthehill-581cd1c0b2e5.nnue',
    f'racingkings': f'racingkings-9ef6dd7cfdfb.nnue'
}


# ========== LOCAL ========== #

FAIRY_ENGINE_LOCAL = Engine(
    name=f'FairyStockfish',
    shortname=f'FairySF',
    binary_dir=f'/home/maxalex/Documents/Engines/fairy-stockfish/',
    binary_name=f'fairy-stockfish',
    version='13.1'
)


FAIRY_ENGINE_NNUE_LOCAL = Engine(
    name=f'FairyStockfishNNUE',
    shortname=f'FairySF-NNUE',
    binary_dir=f'/home/maxalex/Documents/Engines/fairy-stockfish/',
    binary_name=f'fairy-stockfish',
    version='13.1-NNUE',
    cli_options=[['Use NNUE', 'true'],
                 ['EvalFile', 'kingofthehill-581cd1c0b2e5.nnue']]
)

ARA_ENGINE_SL7_LOCAL = Engine(
    name=f'MultiAra-SL7',
    shortname=f'AraSL7',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/home/maxalex/Documents/Engines/MultiAraSL7/',
    version=f'supervised'
)


ARA_ENGINE_UP10_LOCAL = Engine(
    name=f'MultiAra10',
    shortname=f'Ara10',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/home/maxalex/Documents/Engines/MultiAra-10updates/',
    version=f'Update10'
)

ARA_ENGINE_UP20_LOCAL = Engine(
    name=f'MultiAra20',
    shortname=f'Ara20',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/home/maxalex/Documents/Engines/MultiAra-20updates/',
    version=f'Update20'
)

ARA_ENGINE_UP10_FROM0_LOCAL = Engine(
    name=f'MultiAra10From0',
    shortname=f'Ara10From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/home/maxalex/Documents/Engines/MultiAra-10updates-from0/',
    version=f'Update10From0',
)

ARA_ENGINE_RACING_LOCAL = Engine(
    name=f'MultiAraRacing',
    shortname=f'AraRacing',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/home/maxalex/Documents/Engines/MultiAraRacing/',
    version=f'AraRacing',
)



# ========== SERVER ========== #

FAIRY_ENGINE = Engine(
    name=f'FairyStockfish',
    shortname=f'FairySF',
    binary_dir=f'/data/RL/engines/Fairy-Stockfish/',
    binary_name=f'fairy-stockfish',
    version='13.1',
    cli_options=[['Threads', '4'],
                 ['Hash', '2048']]
)


FAIRY_ENGINE_NNUE = Engine(
    name=f'FairyStockfishNNUE',
    shortname=f'FairySFNNUE',
    binary_dir=f'/data/RL/engines/Fairy-Stockfish/',
    binary_name=f'fairy-stockfish',
    version='13.1-NNUE'
)

ARA_ENGINE_UP10 = Engine(
    name=f'MultiAra10',
    shortname=f'Ara10',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-10updates/',
    version=f'Update10'
)

ARA_ENGINE_UP10_RACINGMIRRORED = Engine(
    name=f'MultiAra10RacingMirrored',
    shortname=f'Ara10RaceMirr',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-RacingMirrored-10updates/',
    version=f'Update10RacingMirrored'
)

ARA_ENGINE_UP10_ALPHA60 = Engine(
    name=f'MultiAra10Alpha60',
    shortname=f'Ara10Alpha60',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-alpha60-10updates/',
    version=f'Update10Alpha60'
)

ARA_ENGINE_UP20 = Engine(
    name=f'MultiAra20',
    shortname=f'Ara20',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-20updates/',
    version=f'Update20'
)
ARA_ENGINE_UP30 = Engine(
    name=f'MultiAra30',
    shortname=f'Ara30',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-30updates/',
    version=f'Update30'
)
ARA_ENGINE_UP30_MCTS = Engine(
    name=f'MultiAra30MCTS',
    shortname=f'Ara30MCTS',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-30updates/',
    version=f'Update30MCTS'
)
ARA_ENGINE_UP40 = Engine(
    name=f'MultiAra40',
    shortname=f'Ara40',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-40updates/',
    version=f'Update40'
)
ARA_ENGINE_UP50 = Engine(
    name=f'MultiAra50',
    shortname=f'Ara50',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-50updates/',
    version=f'Update50'
)
ARA_ENGINE_UP50_STATIC_TC_LONG = Engine(
    name=f'MultiAra50TCLong',
    shortname=f'Ara50TCLong',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-50updates/',
    version=f'Update50TCLong',
    time_control=f'60+0.6'
)
ARA_ENGINE_UP60 = Engine(
    name=f'MultiAra60',
    shortname=f'Ara60',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-60updates/',
    version=f'Update60'
)

ARA_ENGINE_UP60_NOEXPLOINC = Engine(
    name=f'MultiAra60NoExploInc',
    shortname=f'Ara60NoExInc',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-noexploinc-60updates/',
    version=f'Update60NoExploInc'
)

ARA_ENGINE_UP10_FROM0 = Engine(
    name=f'MultiAra10From0',
    shortname=f'Ara10From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-10updates/',
    version=f'Update10From0'
)

ARA_ENGINE_UP20_FROM0 = Engine(
    name=f'MultiAra20From0',
    shortname=f'Ara20From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-20updates/',
    version=f'Update20From0'
)
ARA_ENGINE_UP30_FROM0 = Engine(
    name=f'MultiAra30From0',
    shortname=f'Ara30From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-30updates/',
    version=f'Update30From0'
)
ARA_ENGINE_UP30_FROM0_EXTSCHED = Engine(
    name=f'MultiAra30From0ExtSched',
    shortname=f'Ara30From0ExtSched',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-extSched-30updates/',
    version=f'Update30From0ExtSched'
)
ARA_ENGINE_UP40_FROM0_EXTSCHED = Engine(
    name=f'MultiAra40From0ExtSched',
    shortname=f'Ara40From0ExtSched',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-extSched-40updates/',
    version=f'Update40From0ExtSched'
)
ARA_ENGINE_UP50_FROM0_EXTSCHED = Engine(
    name=f'MultiAra50From0ExtSched',
    shortname=f'Ara50From0ExtSched',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-extSched-50updates/',
    version=f'Update50From0ExtSched'
)
ARA_ENGINE_UP60_FROM0_EXTSCHED = Engine(
    name=f'MultiAra60From0ExtSched',
    shortname=f'Ara60From0ExtSched',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-extSched-60updates/',
    version=f'Update60From0ExtSched'
)
ARA_ENGINE_UP40_FROM0 = Engine(
    name=f'MultiAra40From0',
    shortname=f'Ara40From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-40updates/',
    version=f'Update40From0'
)
ARA_ENGINE_UP50_FROM0 = Engine(
    name=f'MultiAra50From0',
    shortname=f'Ara50From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-50updates/',
    version=f'Update50From0'
)
ARA_ENGINE_UP60_FROM0 = Engine(
    name=f'MultiAra60From0',
    shortname=f'Ara60From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-60updates/',
    version=f'Update60From0'
)

ARA_ENGINE_UP10_FROM0_LR04 = Engine(
    name=f'MultiAra10From0LR04',
    shortname=f'Ara10From0LR04',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-from0-LR04-10updates/',
    version=f'Update10From0LR04'
)

ARA_ENGINE_SL7 = Engine(
    name=f'MultiAra-SL7',
    shortname=f'AraSL7',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAraSL7/',
    version=f'supervised'
)

CRAZYARA96_ENGINE = Engine(
    name=f'CrazyAra96',
    shortname=f'Crazy96',
    binary_name='CrazyAra',
    binary_dir=f'/data/RL/engines/CrazyAra96/',
    version=f'Crazy96'
)

# ========== BOOKS ========== #

BOOKS = {
    f'3check': f'3check.epd',
    f'atomic': f'atomic.epd',
    f'crazyhouse': f'crazyhouse_cp_130.epd',
    f'antichess': f'suicide.epd',
    f'horde': f'horde.epd',
    f'kingofthehill': f'kingofthehill.epd',
    f'racingkings': f'racingkings.epd'
}

# ========== TOURNAMENTMODES ========== #

RAPID_MODE = TournamentMode(
    name=f'rapid',
    rounds=50,
    time_control=f'10+0.1'
)

FAST_MODE = TournamentMode(
    name=f'fast',
    rounds=150,
    games=2,
    time_control=f'10+0.1'
)

MEAN_MODE = TournamentMode(
    name=f'mean',
    rounds=50,
    games=2,
    time_control=f'30+0.3'
)

LONG_MODE = TournamentMode(
    name=f'long',
    rounds=50,
    games=2,
    time_control=f'60+0.6'
)

FIXED_MODE = TournamentMode(
    name=f'fixed',
    rounds=50,
    games=2,
    fixed_movetime_sec=5
)
