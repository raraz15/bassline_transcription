import os

# HERE WE DEFINE THE DIRECTORIES AND THE CONSTANTS THAT WE USE THROUGHOUT THE PROJECT


LIBRARY_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_DIR = os.path.dirname(LIBRARY_DIR)

DATA_DIR = os.path.join(ROOT_DIR, 'data')
METADATA_DIR = os.path.join(DATA_DIR, 'metadata')
AUDO_DIR = os.path.join(DATA_DIR, 'audio_clips')
OUTPUT_DIR = os.path.join(DATA_DIR, 'outputs')


FS = 44100 # Sampling rate

# Some Sub-Bass Frequencies in Hz
F_B0 = 30.87  
F_C1 = 32.7 

F_B2 = 123.47 
F_C3 = 130.81

# Frequency Range of Interest
F_MIN = F_B0
F_MAX = F_C3

T_MAX = 1/F_MIN # Longest Period
FRAME_LEN = int(2*T_MAX*FS) # Frame Length

CUTOFF_FREQ = F_MAX