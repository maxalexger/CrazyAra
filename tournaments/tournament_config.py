from cutechesstournament import Engine, TournamentMode

# =========== CONSTANTS ========== #

MULTIARA_GPU = 1

ARA_BINARY_NAME = f'MultiAra'
FAIRY_NNUE = {
    f'kingofthehill': f'kingofthehill-581cd1c0b2e5.nnue'
}


# ========== LOCAL ========== #

FAIRY_ENGINE_LOCAL = Engine(
    name=f'FairyStockfish',
    shortname=f'FairySF',
    binary_dir=f'/home/maxalex/Documents/Engines/fairy-stockfish/',
    binary_name=f'fairy-stockfish',
    version='13.1'
)

ARA_ENGINE_SL7_LOCAL = Engine(
    name=f'MultiAra-SL7',
    shortname=f'AraSL7',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/home/maxalex/Documents/Engines/MultiAraSL7/',
    model_dir=f'/home/maxalex/Documents/Engines/MultiAraSL7/model/',
    version=f'supervised'
)


ARA_ENGINE_UP10_LOCAL = Engine(
    name=f'MultiAra10',
    shortname=f'Ara10',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/home/maxalex/Documents/Engines/MultiAra-10updates/',
    model_dir=f'/home/maxalex/Documents/Engines/MultiAra-10updates/model/',
    version=f'Update10'
)

ARA_ENGINE_UP10_FROM0_LOCAL = Engine(
    name=f'MultiAra10From0',
    shortname=f'Ara10From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/home/maxalex/Documents/Engines/MultiAra-10updates-from0/',
    model_dir=f'/home/maxalex/Documents/Engines/MultiAra-10updates-from0/model/',
    version=f'Update10From0',
)


# ========== SERVER ========== #

FAIRY_ENGINE = Engine(
    name=f'FairyStockfish',
    shortname=f'FairySF',
    binary_dir=f'/data/RL/engines/',
    binary_name=f'fairy-stockfish',
    version='13.1',
    cli_options=[['Threads', '4'],
                 ['Hash', '2048']]
)

ARA_ENGINE_UP10 = Engine(
    name=f'MultiAra10',
    shortname=f'Ara10',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-10updates/',
    version=f'Update10',
    cli_options=[['First_Device_ID', f'{MULTIARA_GPU}'],
                 ['Last_Device_ID', f'{MULTIARA_GPU}']]
)

ARA_ENGINE_UP10_FROM0 = Engine(
    name=f'MultiAra10From0',
    shortname=f'Ara10From0',
    binary_name=ARA_BINARY_NAME,
    binary_dir=f'/data/RL/engines/MultiAra-10updates-from0/',
    version=f'Update10From0',
    cli_options=[['First_Device_ID', f'{MULTIARA_GPU}'],
                 ['Last_Device_ID', f'{MULTIARA_GPU}']]
)

# ========== BOOKS ========== #

BOOKS = {
    f'3check': f'3check.epd',
    f'atomic': f'atomic.epd',
    f'crazyhouse': f'crazyhouse_cp_130.epd',
    f'antichess': f'giveaway.epd',
    f'giveaway': f'giveaway.epd',
    f'horde': f'horde.epd',
    f'kingofthehill': f'kingofthehill.epd',
    f'racingkings': f'racingkings.epd'
}

# ========== TOURNAMENTMODES ========== #

RAPID_MODE = TournamentMode(
    name=f'rapid',
    time_control=f'10+0.1'
)

LONG_MODE = TournamentMode(
    name=f'long',
    time_control=f'60+0.6'
)

FIXED_MODE = TournamentMode(
    name=f'fixed',
    fixed_movetime_sec=5
)
