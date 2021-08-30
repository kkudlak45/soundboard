import winsound
import os
from playsound import playsound

path = 'sounds'
files = os.listdir(path)

def showSongs():
	print("Songs:\n")
	print("0 - exit")
	for i in range(len(files)):
		print(str(i+1) + " - " + files[i])

def playSong(index):
	if (index < 1 or index > len(files)):
		print("\nInvalid input")
		return

	song = files[index-1]
	contents = song.split(".")
	if (contents[len(contents)-1] == "mp3"):
		playsound('sounds/' + song)
	elif (contents[len(contents)-1] == "wav"):
		winsound.PlaySound('sounds/' + song, winsound.SND_FILENAME)
	else:
		print("invalid file format")


while True:
	showSongs()

	inp = input("\nWhat to play? ")

	try:
		inp = int(inp)
		if (inp == 0):
			break
		playSong(inp)
	except ValueError:
		print("\nInvalid Input")

	print("\n\n\n")