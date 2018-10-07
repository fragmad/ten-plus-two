import time
import notify2
import simpleaudio as sa

class TenPlusTwo():
    def __init__(self, work=10, rest=2, reps=5, remind=False):
        self.work = work
        self.pause = rest
        self.reps = reps
        self.remind = remind

        self.work_time = work * 60
        self.rest_time = rest * 60
        self.reps = reps * 60

        self.start_time =  time.time()
        self.half_time = self.start_time + self.work_time / 2
        self.three_quarter_time = self.start_time + ((self.work_time / 4) * 3)
        self.end_time = self.start_time + self.work_time

        self.start_message = "{} Minutes Work".format(work)
        self.break_message = "{} Minutes Rest".format(rest)
        self.break_over = "Break Over!".format(reps)
        self.half_message = "{} Minutes Left".format(self.work_time / 2)
        self.three_quarter_message = "{} Minutes Left".format(self.work_time / 4)

    def work_rest_loop(self):
        notify2.init("ten-plus-two")
        ten_up = notify2.Notification("Time Up!",
                                      self.break_message,
                                      "notification-message-im")

        break_over = notify2.Notification("Break Over!",
                                          self.break_over,
                                          "notification-message-im")


        half_way = notify2.Notification("Half Way!",
                                        self.half_message,
                                        "notification-message-im")


        three_quarters = notify2.Notification("Three Quarters Done!",
                                              self.three_quarter_message,
                                             "notification-message-im")

        start = notify2.Notification("Start!",
                                     self.start_message,
                                     "notification-message-im")

        start.show()

        bell_sound = sa.WaveObject.from_wave_file('.//assets/Zen Temple Bell-SoundBible.com-2070036999.wav')
        bell_sound.play()


        for count in range(self.reps):
            self.start_time =  time.time()
            self.half_time = self.start_time + self.work_time / 2
            self.three_quarter_time = self.start_time + ((self.work_time / 4) * 3)
            self.end_time = self.start_time + self.work_time
            half_time_passed = False
            three_quarters_time_passed = False

            while time.time() <= self.end_time:
                time.sleep(15)
                print(time.time())

                if time.time() >= self.half_time and not half_time_passed:
                    half_time_passed = True
                    half_way.show()

                if time.time() >= self.three_quarter_time and not three_quarters_time_passed:
                    three_quarters_time_passed = True
                    three_quarters.show()

            ten_up.show()
            bell_sound.play()

            time.sleep(self.rest_time)
            break_over.show()
            bell_sound.play()
            print("Repetition {} completed.".format(count))
