from pygame import mixer
from datetime import datetime
from time import time
def musicloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(10)
    while True:

        a=input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylog.txt","a") as f:

        f.write(f"{msg} - {datetime.now()}\n")


if __name__ == '__main__':
    
    init_water=time()
    init_eyes = time()
    init_exercise = time()
    water_time=5
    eyes_time = 10
    exe_time = 15
    while True:
        if time() - init_water > water_time:
            print("Water Drinking Time   'Please Type 'w' to mark as done'")
            musicloop("rain.mp3","w")
            init_water=time()
            log_now("Drank Water at ")

        if time() - init_eyes > eyes_time:
            print("Eyes Relaxing Time   'Please Type 'e' to mark as done'")
            musicloop("excuse_me_reminder.mp3","e")
            init_eyes=time()
            log_now("Eyes Relaxed at ")

        if time() - init_exercise > exe_time:
            print("Exercise Time:     'Please Type 'ex' to mark as done'")
            musicloop("excuse_me_reminder.mp3","ex")
            init_exercise=time()
            log_now("Did Exercise at ")
