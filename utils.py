import time
import pyautogui as pag
from configs import BASE_DIR, configure_argument


def create_folder(folder_name):
    """Создаёт папку в которой хранится результат."""
    dir = BASE_DIR / folder_name
    dir.mkdir(exist_ok=True)
    return dir


def analogue_press(key, sleep=None):
    """Имитирует зажимание и отпускание клавиши с промежутком времени."""
    pag.keyDown(key)
    if sleep is not None:
        time.sleep(sleep)
    pag.keyUp(key)


def getting_arguments():
    """Получает аргументы из консоли"""
    arg = configure_argument()
    args = arg.parse_args()
    path_to_game = args.path
    result = [path_to_game, 'results', 'f1']
    if args.output_path is not None:
        result[1] = args.output_path
    if args.key is not None:
        result[2] = args.key
    return result
