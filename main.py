import os
import logging
import datetime as dt
import pyautogui as pag
from configs import configure_logging, DT_FORMAT
from utils import analogue_press, create_folder, getting_arguments
import time


def launch_game(path_to_game):
    """Запускает игру и пропускает заставку."""
    os.startfile(path_to_game)
    time.sleep(25)
    logging.info('Игра запустилась')

    analogue_press('enter')
    logging.info('Пропущена заставка')


def take_screen(file_name, folder_name):
    """Делает скриншот и сохраняет его в папку."""
    now = dt.datetime.now().strftime(DT_FORMAT)
    file_name = f'{file_name}_{now}.png'
    save_path = folder_name / file_name

    pag.screenshot(save_path)
    logging.info(f'Скриншот сохранён в {save_path}')
    time.sleep(2)


def fps_tracker(key):
    """Собирает статистику, во время движения персонажа."""
    analogue_press(key)
    analogue_press('w', 5)
    analogue_press(key)
    logging.info('Статистика собрана')


def close_game(path_to_game):
    """Закрывает игру."""
    file_name = path_to_game.split('/')[-1]
    os.system(f'taskkill /im {file_name}')
    logging.info('Игра закрыта')


def main():
    configure_logging()
    path_to_game, path_to_output, key = getting_arguments()
    folder = create_folder(path_to_output)

    launch_game(path_to_game)

    take_screen('screen_after_launch', folder)

    time.sleep(5)
    analogue_press('enter')
    time.sleep(2)

    fps_tracker(key)
    take_screen('screen_after_fps_traking', folder)
    close_game(path_to_game)


if __name__ == '__main__':
    main()
