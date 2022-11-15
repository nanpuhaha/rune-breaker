import os
import re


# Classification
INPUT_SHAPE = (60, 60, 1)
CLASSES = ['down', 'left', 'right', 'up']

# Directories
DATA_DIR = './data/'

SAMPLES_DIR = f'{DATA_DIR}samples/'
TRAINING_DIR = f'{DATA_DIR}training/'
VALIDATION_DIR = f'{DATA_DIR}validation/'
TESTING_DIR = f'{DATA_DIR}testing/'
LABELED_DIR = f'{DATA_DIR}labeled/'
PREPROCESSED_DIR = f'{DATA_DIR}preprocessed/'
SCREENSHOTS_DIR = f'{DATA_DIR}screenshots/'

MODEL_DIR = './model/'


# Functions
def get_files(directory):
    result = []

    for name in os.listdir(directory):
        path = directory + name

        if os.path.isfile(path):
            result.append((path, name))
        else:
            result.extend(get_files(f'{path}/'))

    return result


def arrow_labels(name):
    tokens = re.split('_', name)
    arrow_direction, arrow_type = tokens[1], tokens[0]

    return arrow_direction, arrow_type


def create_directories():
    directories = [
        SCREENSHOTS_DIR,
        LABELED_DIR,
        PREPROCESSED_DIR,
        SAMPLES_DIR
    ]

    for d in [TRAINING_DIR, VALIDATION_DIR, TESTING_DIR]:
        directories.extend(d + c + '/' for c in CLASSES)
    for d in directories:
        os.makedirs(d, exist_ok=True)
