import os
from os import system
from fontTools import ttLib

def chooseDefaultFont(HOME):
	print('Which of these fonts would you like to use as your default monospace font?')
	fonts = []

	for font in os.listdir(f'{HOME}/.local/share/fonts/'):
		try:
			ttFont = ttLib.TTFont(f'{HOME}/.local/share/fonts/{font}')
			fontName = ttFont['name'].getDebugName(1)
			if not fontName in fonts:
				fonts.append(fontName)
		except:
			continue

	for font in range(0, len(fonts)):
		print(f'{font + 1}) {fonts[font]}')

	return fonts[getUserChoice(1, len(fonts)) - 1]

def patchFont(HOME):
	system('echo -n "Installing fontforge... " && sudo apt install python3-fontforge -y > /dev/null 2>&1 && echo Done')
	system(f'cd {HOME}/.ossetup/ && echo -n "Downloading font-patcher... " && wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip -q && mkdir fontPatcher && unzip -q FontPatcher.zip -d fontPatcher/ && rm -f FontPatcher.zip && echo Done')
	system(f'mkdir {HOME}/.ossetup/fonts/patched')
	files = os.listdir(f'{HOME}/.ossetup/fonts/')

	system('echo -n "Patching font/s; this may take a few minutes... "')
	for file in files:
		if file.endswith('otf') or file.endswith('ttf'):
			system(f'python3 {HOME}/.ossetup/fontPatcher/font-patcher {HOME}/.ossetup/fonts/"{file}" -s -c -q --fontawesome --fontawesomeextension --fontlogos --octicons --codicons --powersymbols --pomicons --powerline --powerlineextra --material --weather -out {HOME}/.ossetup/fonts/patched/ > /dev/null 2>&1')
	system('echo Done!')

	system(f'echo "Removing font-patcher... " && cd {HOME}/.ossetup/ && rm -rf fontPatcher/ && sudo apt remove python3-fontforge -y > /dev/null 2>&1 && echo Done')
	if not os.path.exists(f'{HOME}/.local/share/fonts/'):
		system(f'mkdir {HOME}/.local/share/fonts/')
	system(f'echo -n "Installing patched fonts... " && cp -r {HOME}/.ossetup/fonts/patched/ {HOME}/.local/share/fonts/ && echo Done!')

def installFont(HOME):
	if not os.path.exists(f'{HOME}/.local/share/fonts/'):
		system(f'mkdir {HOME}/.local/share/fonts/')
	system(f'echo -n "Installing fonts... " && cp -r {HOME}/.ossetup/fonts/ {HOME}/.local/share/fonts/ && echo Done!')

# this method gets user choice within a number range
def getUserChoice(low, hi):
	while True:
		userChoice = int(input(f'Choose an option [{low}-{hi}]: '))
		if userChoice >= low and userChoice <= hi:
			return userChoice
		else:
			print('Invalid option, please try again.')
