import pandas as pd
import time
import datetime


class _GetchUnix:
    # from https://code.activestate.com/recipes/134892/
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def logging():
    path = 'logs/keylog/'
    filename = f"{time.strftime('%Y-%m-%d %H-%M-%S')}.csv"
    path_to_file = path + filename
    db = []
    getch = _GetchUnix()
    print('Процесс...')
    while True:
        key = getch()
        if key == 'c':
            break
        else:
            db.append((datetime.datetime.now(), key))
    df = pd.DataFrame(db, columns=['time', 'click'])
    print(df)
    df.to_csv(path_to_file, index=False)
    print(f"\nSaved to {filename}")

if __name__ == "__main__":
    logging()
