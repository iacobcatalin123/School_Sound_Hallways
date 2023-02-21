from os import listdir
from os.path import isfile, join
from playsound import playsound
import datetime
import random

SONG_PATH = "./music"

SONG_TIMES = {
    # "8:50", "9:50", "10:50", "11:50", "12:50", "14:00", "15:00", "16:00", "17:00", "18:00"
    "hour": [8, 9, 10, 11, 12, 14, 15, 16, 17, 18],
    "minute": [50, 50, 50, 50, 50, 0, 0, 0, 0, 0]
}

BREAK_TIMES = {
    # "9:00", "10:00", "11:00", "12:00", "13:00", "14:10", "15:10", "16:10", "17:10", "18:10"
    "hour": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
    "minute": [0, 0, 0, 0, 0, 10, 10, 10, 10, 10]
}

songs = [f for f in listdir(SONG_PATH) if isfile(join(SONG_PATH, f))]

def play_song(song):
    playsound(SONG_PATH + "/" + song)


def main():
    while True:
        minute = int(datetime.datetime.now().strftime("%M"))#  1
        hour = int(datetime.datetime.now().strftime("%H"))#  1
        if hour in SONG_TIMES["hour"] and minute in SONG_TIMES["minute"]: # daca ora si minutul sunt in lista de ore si minute
            play_song(random.choice(songs))
        elif hour in BREAK_TIMES["hour"] and minute in BREAK_TIMES["minute"]: # daca ora si minutul sunt in lista de ore si minute din break
            play_song("bell.mp3")
        else:
            pass


main()