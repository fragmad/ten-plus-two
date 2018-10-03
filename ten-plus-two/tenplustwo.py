import argparse
import time
import notify2
import simpleaudio as sa

class TenPlusTwo():
    def __init__(self, work, rest, reps):
        self.work = work
        self.pause = rest
        self.reps = reps

        self.work_time = work * 60
        self.rest_time = rest * 60
        self.reps = reps * 60

        self.start_message = "{} Minutes Work".format(work)
        self.break_message = "{} Minutes Rest".format(rest)
        self.break_over = "Break Over!".format(reps)

    def work_rest_loop(self):
        notify2.init("ten-plus-two")
        ten_up = notify2.Notification("Ten Minutes Up!",
                                      self.break_message,
                                      "notification-message-im")

        break_over = notify2.Notification("Break Over!",
                                          self.break_over,
                                          "notification-message-im")


        start = notify2.Notification("Start!",
                                     self.start_message,
                                     "notification-message-im")

        start.show()

        bell_sound = sa.WaveObject.from_wave_file('.//assets/Zen Temple Bell-SoundBible.com-2070036999.wav')
        play_bell = bell_sound.play()
        play_bell.wait_done()

        for count in range(self.reps):
            time.sleep(self.work_time)
            ten_up.show()
            play_bell = bell_sound.play()
            play_bell.wait_done()

            time.sleep(self.rest_time)
            break_over.show()
            play_bell = bell_sound.play()
            play_bell.wait_done()
            print("Repetition {} completed.".format(count))
