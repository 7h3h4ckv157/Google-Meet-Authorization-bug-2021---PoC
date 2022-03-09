import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        p = 'Position of X: ' + str(x).rjust(4) + '\t Position of Y: ' + str(y).rjust(4); print(p, end='')
        print('\b' * len(p), end='', flush=True)

except KeyboardInterrupt:
    print('\n')
