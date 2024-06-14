#automation
import time
import winsound
import pygame
# List of alarm times in HH:MM format
alarm_times = ["21:21","09:00", "12:30"]
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("constellation.wav")

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M")
        
        if current_time == alarm_time:
            print(f"Alarm! It's {alarm_time} now.")
            start_time = time.time()  # Record the start time
            alarm_sound.play()  # Play the loaded sound
            while time.strftime("%H:%M") == alarm_time:
                pass  # Wait until the alarm time is over
            alarm_sound.stop()  # Stop the sound
            break
        time.sleep(15)  # Check every minute

for alarm_time in alarm_times:
    set_alarm(alarm_time)
