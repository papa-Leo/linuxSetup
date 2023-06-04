import os
from os import system

def patchFont():
    # install font tools
	# get font path
	# patch fonts
	# uninstall tools
	system('echo Installing fontforge... && sudo apt install python3-fontforge -y > /dev/null 2>&1 && echo Done')
	system('cd ~/.ossetup/ && echo Downloading font-patcher... && wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip -q && mkdir fontPatcher && unzip -q FontPatcher.zip -d fontPatcher/ && rm -f FontPatcher.zip && echo Done')
	system('mkdir ~/.ossetup/fonts/patched')
	files = os.listdir('/home/papaleo/.ossetup/fonts/')

	print('Patching font/s; this may take a few minutes...')
	for file in files:
		if file.endswith('otf') or file.endswith('ttf'):
			system('python3 ~/.ossetup/fontPatcher/font-patcher ~/.ossetup/fonts/"' + file + '" -s -c -q --fontawesome --fontawesomeextension --fontlogos --octicons --codicons --powersymbols --pomicons --powerline --powerlineextra --material --weather -out ~/.ossetup/fonts/patched/ > /dev/null 2>&1')
	
	system('echo Removing font-patcher && cd ~/.ossetup/ && rm -rf fontPatcher/ && sudo apt remove python3-fontforge -y > /dev/null 2>&1')
	print('Done!')

patchFont()