#Countdown timer project
#User will set a time in seconds for the timer to count down

import time
def countdown_timer_project():
    while True:
        print("How long should the timer last in seconds? ")
        timer_count = int(input("Time (s): "))

        for x in range(timer_count, 0 , -1):
            seconds = x % 60
            minutes = int(x/60) % 60
            hours = int(x/3600)
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)


        print("Time is up!")

countdown_timer_project()
            
