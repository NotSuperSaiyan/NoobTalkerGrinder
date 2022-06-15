from pynput.keyboard import *
import time
import random

keyboard = Controller()
time.sleep(2)

for i in range(5):
	keyboard.type("plz beg")
	keyboard.press(Key.enter)
	time.sleep(3.5)

	keyboard.type("plz fish")
	keyboard.press(Key.enter)
	time.sleep(3.5)

	keyboard.type("plz hunt")
	keyboard.press(Key.enter)
	time.sleep(3.5)

	keyboard.type("plz search")
	keyboard.press(Key.enter)
	time.sleep(2.5)
	keyboard.type(random.choice(["tree","shop","shoe","home","discord"]))
	keyboard.press(Key.enter)
	time.sleep(3.5)

	keyboard.type("plz dep max")
	keyboard.press(Key.enter)
	time.sleep(3.5)

	keyboard.type("plz bal")
	keyboard.press(Key.enter)
	time.sleep(25)