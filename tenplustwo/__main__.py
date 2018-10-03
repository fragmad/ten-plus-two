import argparse
import time
import notify2
import simpleaudio as sa

parser = argparse.ArgumentParser()
parser.add_argument("-w","--work", help="time to work in minutes",
                    default=10, type=int)
parser.add_argument("-b","--rest", help="time to break in minutes",
                    default=2, type=int)
parser.add_argument("-r","--reps", help="number of repetitions to complete before exiting",
                    default=5, type=int)

args = parser.parse_args()

WORK_TIME = args.work * 60
BREAK_TIME = args.rest * 60
REPITITIONS = args.reps * 60

start_message = "{} Minutes Work".format(args.work)
break_message = "{} Minutes Rest".format(args.rest)
break_over = "Break Over!".format(args.reps)

notify2.init("ten-plus-two")
ten_up = notify2.Notification("Ten Minutes Up!",
                                break_message,
                              "notification-message-im")

break_over = notify2.Notification("Break Over!",
                                  break_over,
                                  "notification-message-im")


start = notify2.Notification("Start!",
                             start_message,
                             "notification-message-im")

start.show()

bell_sound = sa.WaveObject.from_wave_file('.//assets/Zen Temple Bell-SoundBible.com-2070036999.wav')
play_bell = bell_sound.play()
play_bell.wait_done()

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

