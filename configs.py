import argparse
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

BASE_DIR = Path(__file__).parent
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DT_FORMAT = '%Y-%m-%d_%H-%M-%S'


def configure_argument():
    parser = argparse.ArgumentParser(description='Тестирование kkrieger.')
    parser.add_argument(
        'path',
        help='Путь к игре'
    )
    parser.add_argument(
        '-o',
        '--output-path',
        help='Путь для вывода данных'
    )
    parser.add_argument(
        '-k',
        '--key',
        help='Клавиша для активации FPS Monitor'
    )
    return parser


def configure_logging():
    log_dir = BASE_DIR / 'Logs'
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'parser.log'

    rotating_handler = RotatingFileHandler(
        log_file, maxBytes=10**6, backupCount=5
    )
    logging.basicConfig(
        datefmt=DT_FORMAT,
        format=LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler())
    )
