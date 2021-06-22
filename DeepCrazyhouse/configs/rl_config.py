"""
@file: rl_config.py
Created on 01.04.2021
@project: CrazyAra
@author: queensgambit, maxalexger

Configuration file for Reinforcement Learning
"""
from dataclasses import dataclass


@dataclass
class RLConfig:
    """Dataclass storing the options (except UCI options) for executing reinforcement learning."""
    arena_games: int = 100
    binary_dir: str = f'/data/RL/'
    binary_name: str = f'MultiAra'
    nb_nn_updates: int = 10
    nn_update_files: int = 10
    precision: str = f'float16'

    # Replay Memory
    rm_nb_files: int = 5
    rm_fraction_for_selection: float = 0.05

    uci_variant: str = f'3check'


@dataclass
class UCIConfig:
    """
    Dataclass which contains the UCI Options that are used during Reinforcement Learning.
    The options will be passed to the binary before game generation starts.
    """
    Allow_Early_Stopping: bool = False
    Batch_Size: int = 8

    Centi_CPuct_Init: int = 250
    Centi_Dirichlet_Alpha: int = 20
    Centi_Dirichlet_Epsilon: int = 25
    Centi_Epsilon_Checks: int = 0
    Centi_Epsilon_Greedy: int = 0
    Centi_Node_Temperature: int = 100
    Centi_Q_Value_Weight: int = 100
    Centi_Q_Veto_Delta: int = 40

    Centi_Quick_Dirichlet_Epsilon: int = 0
    Centi_Quick_Probability: int = 0
    Centi_Quick_Q_Value_Weight: int = 0
    Quick_Nodes: int = 0

    Centi_Random_Move_Factor: int = 0
    Centi_Resign_Probability: int = 0
    Centi_Resign_Threshold: int = 0
    Centi_U_Init_Divisor: int = 100

    Fixed_Movetime: int = 1000
    Centi_Virtual_Loss: int = 100
    MCTS_Solver: bool = True
    Milli_Policy_Clip_Thresh: int = 0
    Move_Overhead: int = 0

    Nodes: int = 800
    Centi_Node_Random_Factor: int = 10

    Reuse_Tree: str = False
    Search_Type: str = f'mcgs'
    Selfplay_Chunk_Size: int = 128
    Selfplay_Number_Chunks: int = 640
    Simulations: int = 3200
    SyzygyPath: str = f''
    Timeout_MS: int = 0
    Use_NPS_Time_Manager: bool = False

    # Initial book moves
    MaxInitPly: int = 30
    MeanInitPly: int = 8
    Centi_Raw_Prob_Temperature: int = 5

    # Initial temperature moves (after init book moves)
    Centi_Temperature: int = 80
    Centi_Temperature_Decay: int = 92
    Centi_Quantile_Clipping: int = 0
    Temperature_Moves: int = 15


@dataclass
class UCIConfigArena:
    """
    This class overrides the UCI options from the UCIConfig class for the arena tournament.
    All other options will be taken from the UCIConfig class.
    """
    Centi_Temperature: int = 60



