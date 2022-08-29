import time

from init_driver_selenium import init_webdriver
from selenium.webdriver.common.by import By
import winsound
from playsound import playsound
from gtts import gTTS


def status_update(url):
    driver = init_webdriver()
    driver.set_window_size(1920, 1080)
    driver.get(url)
    time.sleep(1)
    status = driver.find_element(By.CLASS_NAME, 'status-update').text
    return status


def play_sound(text_val):
    # It is a text value that we want to convert to audio
    # text_val = 'All the best for your exam.'

    # Here are converting in English Language
    language = 'en'

    # Passing the text and language to the engine,
    # here we have assign slow=False. Which denotes
    # the module that the transformed audio should
    # have a high speed
    obj = gTTS(text=text_val, lang=language, slow=True)

    # Here we are saving the transformed audio in a mp3 file named
    # exam.mp3
    obj.save("exam.mp3")

    # Play the exam.mp3 file
    playsound("exam.mp3")


if __name__ == '__main__':
    url = 'https://status.escapefromtarkov.com/'
    try:
        status = status_update(url)
    except:
        status = 'Read Error'

    play_sound(status)
    # if status == 'Servers on update':
    #     winsound.Beep(2500, 1100)
