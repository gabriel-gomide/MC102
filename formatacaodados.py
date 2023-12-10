import pyautogui
import time
# Espera alguns segundos antes de começar, para que você tenha tempo de trazer o Fityk para frente
time.sleep(5)

# Obter as coordenadas dos elementos de interesse
print("Posicione o cursor do mouse sobre o elemento e aguarde alguns segundos...")
time.sleep(5)
current_position = pyautogui.position()
print(f"Coordenadas do elemento: {current_position}")



