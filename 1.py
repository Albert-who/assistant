from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

def set_volume(volume_level):
    # Получаем доступ к аудио-устройству (в данном случае, к динамикам)
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    audio_volume = cast(interface, POINTER(IAudioEndpointVolume))
    # Устанавливаем громкость на определенный уровень (0.0 - 1.0)
    audio_volume.SetMasterVolumeLevelScalar(volume_level, None)

# Установка громкости (значение от 0.0 до 1.0)
set_volume(0.5)  # Настройте значение по вашему усмотрению

def set_brightness(brightness):
    # Устанавливаем яркость экрана (значение от 0 до 100)
    sbc.set_brightness(brightness)

# Установка яркости (значение от 0 до 100)
set_brightness(50)  # Настройте значение по вашему усмотрению