import os
from os import system

def patchFont():
    # install font tools
	# get font path
	# patch fonts
	# uninstall tools
	system('echo INSTALLING FONTFORGE... && sudo apt-get -qq install python3-fontforge -y && echo \bDone')
	system('cd ~/.ossetup/ && echo DOWNLOADING FONT PATCHER... && wget https://github.com/ryanoasis/nerd-fonts/releases/latest/download/FontPatcher.zip -q && mkdir fontPatcher && unzip FontPatcher.zip -d fontPatcher/ -q && rm -f FontPatcher.zip && echo Done')
	system('mkdir ~/.ossetup/fonts/patched')
	files = os.listdir('/home/papaleo/.ossetup/fonts/')
	print(files)

	for file in files:
		if file.endswith('otf') or file.endswith('ttf'):
			system('python3 ~/.ossetup/fontPatcher/font-patcher ~/.ossetup/fonts/"' + file + '" -s -c --fontawesome --fontawesomeextension --fontlogos --octicons --codicons --powersymbols --pomicons --powerline --powerlineextra --material --weather -out ~/.ossetup/fonts/patched/')

patchFont()