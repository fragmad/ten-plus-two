import time
import notify2
import simpleaudio as sa

WORK_TIME = 600
BREAK_TIME = 120
REPITITIONS = 5

bell_sound = sa.WaveObject.from_wave_file('./assets/Zen Temple Bell-SoundBible.com-2070036999.wav')
play_bell = bell_sound.play()
play_bell.wait_done()

notify2.init("ten-plus-two")
ten_up = notify2.Notification("Ten Minutes Up!",
                              "Two Minute Break",
                              "notification-message-im")

break_over = notify2.Notification("Break Over!",
                                  "Ten Minutes Work",
                                  "notification-message-im")


start = notify2.Notification("Start!",
                             "Ten Minutes Work",
                             "notification-message-im")

start.show()

for count in range(REPITITIONS):
    time.sleep(WORK_TIME)
    ten_up.show()
    play_bell = bell_sound.play()
    play_bell.wait_done()

    time.sleep(BREAK_TIME)
    break_over.show()
    play_bell = bell_sound.play()
    play_bell.wait_done()
    print(f"Repetition {count} completed.")

